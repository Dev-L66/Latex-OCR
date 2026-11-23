from config import  get_client
from prompts import LATEX_OCR_PROMPT


def extract_latex(encoded_image: str, mime_type: str):

        client = get_client()
        model = "qwen/qwen3.8-27b"

        messages = [
            {
                "role": "system",
                "content": LATEX_OCR_PROMPT
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Extract the mathematical equation from this image."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:{mime_type};base64,{encoded_image}"
                        }
                    }
                ]
            }
        ]

        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0
        )

        return response.choices[0].message.content

