from image_util import image_path
from latex_ocr import extract_latex


def main():
    encoded_image, mime_type = image_path("equation.png")
    latex_result = extract_latex(encoded_image, mime_type)
    print(latex_result)


if __name__ == "__main__":
    main()
