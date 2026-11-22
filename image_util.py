import base64
import mimetypes
from pathlib import Path



def image_path(path:str):

    if not path:
        raise ValueError("No image path found.")
    
    filepath = Path(path)

    if not filepath.exists():
        raise ValueError("Path not found.")

    allowed_extensions = [".png", ".jpg", ".jpeg", ".webp"]

    if filepath.suffix.lower() not in allowed_extensions:
        raise ValueError("Unsupported image format")

    mime_type, _ = mimetypes.guess_type(filepath)

    if not mime_type:
        raise ValueError("Could not determine image MIME type.")
      
    with open(filepath, "rb") as img:
        image = img.read()
        encoded_image = base64.b64encode(image).decode("utf-8")

    return encoded_image, mime_type