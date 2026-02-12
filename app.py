from flask import Flask, render_template, request
from openai import OpenAI
import os
from dotenv import load_dotenv
import base64

load_dotenv()  # Load environment variables from .env

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/", methods=["GET", "POST"])
def index():
    interpretation = None
    image_base64 = None
    error = None

    if request.method == "POST":
        user_prompt = request.form.get("prompt", "").strip()
        if not user_prompt:
            error = "Please enter a prompt."
            return render_template(
                "index.html",
                image_base64=image_base64,
                result=interpretation,
                error=error,
            )

        try:
            response = client.responses.create(
                model="gpt-4.1-nano",
                temperature=1.2,
                top_p=1.0,
                input=[
                    {
                        "role": "developer",
                        "content": (
                            "You are an assistant trained in Carl Jung's analytical psychology. "
                            "Interpret dreams symbolically, not literally, using Jungian concepts. "
                            "Use clear section headings and be reflective, not deterministic."
                        ),
                    },
                    {
                        "role": "user",
                        "content": f"""
Analyze this dream through a Jungian lens.

Dream:
{user_prompt}

Please structure your answer as:
## Key Symbols
- Main symbolic elements

## Archetypal Dynamics
- Possible archetypes (Shadow, Anima/Animus, Self, Hero, etc.)

## Psychological Meaning
- What unconscious tension or compensation may be present

## Individuation Insight
- What growth this dream may be inviting
                        """,
                    },
                ],
            )
            interpretation = (response.output_text or "").strip()
            if not interpretation:
                interpretation = "No interpretation text was returned."

            image_prompt = f"""
Create a richly detailed, surreal, Jungian dream illustration based on the following dream input:
{user_prompt}

Style direction:
- Symbolic, psychological, and archetypal visual storytelling
- Oneiric atmosphere with layered visual metaphors and ambiguous emotional tone
- Cinematic composition with clear focal hierarchy and strong depth cues
- Fine-art look combining painterly textures with realistic lighting behavior

Visual language:
- Evoke the unconscious through symbolic motifs: thresholds, mirrors, labyrinths, moonlit water, masks, shadow forms, ancient ruins, trees, caves, and celestial geometry
- Use dream logic: impossible architecture, subtle scale distortions, fluid transitions between foreground and background
- Keep symbolism elegant and coherent, not chaotic

Lighting and color:
- Low-key, moonlit, misty nocturnal scene
- Chiaroscuro contrast with soft volumetric fog and rim lighting
- Palette: deep blue-black, muted teal, desaturated indigo, charcoal, with restrained antique-gold accents
- Gentle glow around symbolic elements; avoid oversaturated neon tones

Composition and detail:
- Mid-to-wide cinematic framing with atmospheric perspective
- Intricate textures in fabric, stone, water, skin, and foliage
- Strong sense of layered depth: foreground silhouette, active midground narrative, distant dream horizon
- Include subtle recurring symbols to suggest hidden meaning

Image quality targets:
- Ultra-detailed, high coherence, refined edges, natural gradients, and balanced contrast
- Clean output with no text overlays, no watermark, no logo, no frame, no UI artifacts
- Avoid cartoonish exaggeration; prioritize mature fine-art surrealism

Final intent:
Render a haunting, introspective, emotionally resonant dream tableau that feels timeless, mythic, and psychologically meaningful.
"""

            img = client.images.generate(
                model="gpt-image-1-mini",
                prompt=image_prompt,
                n=1,
                size="1024x1024",
                output_format="jpeg",
                output_compression=20,
            )
            # Normalize base64 to ensure template rendering is robust.
            image_base64 = base64.b64encode(base64.b64decode(img.data[0].b64_json)).decode("utf-8")
        except Exception as e:
            error = f"Error: {str(e)}"

    return render_template(
        "index.html",
        image_base64=image_base64,
        result=interpretation,
        error=error,
    )

if __name__ == "__main__":
    app.run(debug=True)  # Run locally for testing
