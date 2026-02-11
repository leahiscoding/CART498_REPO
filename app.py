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
                        "content": "You are an assistant trained in Carl Jung's analytical psychology. You interpret dreams symbolically, not literally, using Jungian concepts. Your interpretations are reflective and exploratory.",
                    },
                    {
                        "role": "user",
                        "content": f"""
                            Analyze the following dream using Jungian analytical psychology. No follow-up questions.

                            Dream: {user_prompt}

                            Please include:
                            1. Key symbols and figures
                            2. Possible Jungian archetypes involved
                        """,
                    },
                ],
            )
            interpretation = response.output[0].content[0].text

            img = client.images.generate(
                model="gpt-image-1-mini",
                prompt=user_prompt,
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
