def convert_spaces(input_path, output_path, replacement_char='_'):
    try:
        # Open the input file
        with open(input_path, 'r') as infile:
            # Read the content of the file
            content = infile.read()

        # Replace spaces with the specified character
        converted_content = content.replace(' ', replacement_char)

        # Open the output file and write the converted content
        with open(output_path, 'w') as outfile:
            outfile.write(converted_content)

        print(f"Spaces converted and saved to {output_path} with replacement character '{replacement_char}'.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # Example usage
    input_path = r"C://Users//lagan\OneDrive\Desktop\lagan.txt"
    output_path = r"C://Users//lagan\OneDrive\Desktop\converted_text_Test.txt"
    replacement_char = '_'
    convert_spaces(input_path, output_path, replacement_char)
