from http import client
from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv
import base64
#client = OpenAI()

load_dotenv()  # Load environment variables from .env

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")  # Securely load API key

@app.route("/", methods=["GET", "POST"])
def index():
    image_base64 = None
    error = None

    if request.method == "POST":
        user_prompt = request.form["prompt"]
        try:
            client = openai.OpenAI()

            img = client.images.generate(
                model="gpt-image-1-mini",  
                prompt=user_prompt,
                n=1,
                size="512x512",
                #response_format="b64_json"
            )
            image_base64 = img.data[0].b64_json
            image_data = base64.b64encode(
                base64.b64decode(image_base64)
            ).decode("utf-8")
            #image_bytes = base64.b64decode(img.data[0].b64_json)
            """ with open("output.png","wb")as f:
                f.write(image_bytes)"""
        except Exception as e:
            error = f"Error: {str(e)}"
    #return render_template("index.html", result=result)
    return render_template(
        "index.html",
        image_base64=image_base64,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True)  # Run locally for testing

    """img = client.images.generate(
    model="gpt-image-1.5",
    prompt="A cute baby sea otter",
    n=1,
    size="1024x1024"
)

image_bytes = base64.b64decode(img.data[0].b64_json)
with open("output.png", "wb") as f:
    f.write(image_bytes)"""