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


image = "./ai-lab/images/pizza_slice.png"
# print(encode_image_to_base64(image))


# A function that queries openai vision model with. This function
# accepts client, image, prompt, model and max_tokens as parameters.
def query_openai_vision_model(client, image, prompt, model="gpt-4o", max_tokens=100):
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
            model=model, messages=messages, max_tokens=max_tokens
        )
        return response
    except Exception as e:
        print(f"{e}")
    return None


food_recognition_prompt = """
Context: You are a nutrition expert analyzing food images to provide accurate nutritional information.
Instruction: Analyze the food item in the image and provide estimated nutritional information based on your knowledge.
Input: An image of a food item
Output: 
Provide the following estimated nutritional information for a typical serving size or per 100g:
- food_name (string)
- serving_description (string, e.g., '1 slice', '100g', '1 cup')
- calories (float)
- fat_grams (float)
- sugar_grams (float)
- fibre_grams (float)
- protein_grams (float)
- confidence_level (string: 'High', 'Medium', or 'Low')

**IMPORTANT:** Respond ONLY with a single JSON object containing these fields. Do not include any other text, explanations, or apologies. The JSON keys must match exactly: "food_name", "serving_description", "calories", "fat_grams", "protein_grams", "confidence_level". If you cannot estimate a value, use `null`.

Example valid JSON response:
{
  "food_name": "Banana",
  "serving_description": "1 medium banana (approx 118g)",
  "calories": 105.0,
  "fat_grams": 0.4,
  "sugar_grams": 0.1,
  "fibre_grams": 0.6,
  "protein_grams": 1.3,
  "confidence_level": "High"
}
"""


print("Querying OpenAI Vison...")
openai_description = query_openai_vision_model(
    client,
    image,
    food_recognition_prompt,
)

print(openai_description.choices[0].message.content)



for model in client.models.list():

    print(model.id)