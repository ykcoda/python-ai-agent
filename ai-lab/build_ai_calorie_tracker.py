from openai import OpenAI
from dotenv import load_dotenv
from IPython.display import display, Markdown
import os
from PIL import Image
import base64


load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")


client = OpenAI(api_key=openai_api_key)
print("OpenAI client successfully configured")
print(openai_api_key[:8])


# write a function that can encode an image into base64 format
# improve this function by checking if the image path is valid and if the image is an image file
def encode_image_to_base64(image_path):
    if not os.path.exists(image_path):
        print(f"Image path {image_path} does not exist")
        return None
    if not image_path.endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp")):
        print(f"Image path {image_path} is not an image file")
        return None
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")
    except Exception as e:
        print(f"{e}")
    return None


image = "./ai-lab/images/greek_salad.png"
print(encode_image_to_base64(image))


# A function that queries openai vision model with. This function
# accepts client, image, prompt, model and max_tokens as parameters.
def query_openai_vision_model(client, image, prompt, max_tokens=100, model="gpt-4o"):
    """
    Query the OpenAI vision model with the given image, prompt, model and max_tokens.

    Args:
        client: The OpenAI client
        image: The image to query the model with
        prompt: The prompt to query the model with
        max_tokens: The maximum number of tokens to generate
        model: The model to use (default: gpt-4o)
    Returns:
        The response from the model
    """

    # encode the image to base64
    base64_image = encode_image_to_base64(image)

    try:
        # construct the messages payload
        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                    },
                ],
            }
        ]

        response = client.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=max_tokens
        )
        return response
    except Exception as e:
        print(f"{e}")
    return None
