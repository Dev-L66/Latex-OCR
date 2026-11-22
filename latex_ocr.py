from config import client, model


def extract_latex(encoded_image:str, mime_type):
    system_prompt = """ 
                   You're an expert mathematical OCR system.
                   Analyze the provided mathematical equation image.
                   Convert the equation into Latex code.

                   Rules:
                  1. Extract mathematical equations into valid LaTeX.
                  2. Preserve mathematical symbols, fractions,
                     subscripts and superscripts.
                  3. If no mathematical equation is present,
                     return exactly: NO_EQUATION_FOUND
                  4. Do not guess or invent equations.
                  5. Return only LaTeX code or NO_EQUATION_FOUND.
                   """


    messages = [{"role":"system", 
                "content": system_prompt},
                {"role":"user", 
                 "content":[
                     {"type":"text", "text": "Extract the mathematical equation from this image."},
                     {"type": "image_url", 
                      "image_url": {
                       "url": f"data:{mime_type};base64,{encoded_image}"
                        }}]}]

    response = client.chat.completions.create(model = model, messages = messages, temperature=0)

    return response.choices[0].message.content
