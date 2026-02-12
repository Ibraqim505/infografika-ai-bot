import logging
import os
from openai import OpenAI

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)


async def generate_infographic(input_path: str, output_path: str):
    logging.info("Sending image to OpenAI for processing")

    with open(input_path, "rb") as f:
        response = client.images.generate(
            model="gpt-image-1",
            prompt="Create marketplace infographic style, bold benefits text blocks, WB/Ozon style",
            image=f
        )

    image_base64 = response.data[0].b64_json

    import base64
    with open(output_path, "wb") as out:
        out.write(base64.b64decode(image_base64))

    logging.info("Image generated successfully")
