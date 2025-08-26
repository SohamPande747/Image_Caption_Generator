import os
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv


# Configure Gemini
# --- Load env and validate API key ---

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError(
        "GOOGLE_API_KEY not found in environment. "
        "Set it in a .env file or as a system environment variable."
    )


genai.configure(api_key=GOOGLE_API_KEY)


# Load model
model = genai.GenerativeModel("gemini-2.5-flash")



def generate_image_caption(image_path, model):
    """
    Opens an image from the given path and generates a caption using Gemini.
    
    Args:
        image_path (str): Path to the image file.
        model: Gemini generative model object.
        
    Returns:
        str: Generated caption.
    """
    try:
        # Load the image
        image = Image.open(image_path)

        # Generate caption
        response = model.generate_content(
            ["Write a short caption for this image.", image]
        )

        # Extract text safely
        if response.candidates:
            caption = response.candidates[0].content.parts[0].text
        else:
            caption = "No caption generated."
        return caption

    except Exception as e:
        return f"Error generating caption: {e}"




# Example usage
image_path = "/home/soham-pande/Public/Learning_Computers/image_caption_generator/Images/10815824_2997e03d76.jpg"
caption = generate_image_caption(image_path, model)
print("Caption:", caption)