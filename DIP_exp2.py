from PIL import Image


def convert_image(input_path, output_path, output_format):
    try:

        # Open the input image

        with Image.open(input_path) as img:

            # Convert and save the image to the specified format

            img.save(output_path, format=output_format)

            print(f"Image converted and saved to {output_path} in {output_format} format.")

    except Exception as e:

        print(f"Error: {e}")


if __name__ == "__main__":
    # Example usage
    input_path = "C://Users/lagan/OneDrive/Desktop/input.jpg"
    output_path = "C://Users/lagan/OneDrive/Desktop/output.png"

    output_format = "PNG"

    convert_image(input_path, output_path, output_format)
