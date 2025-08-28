def modify_content(text):
    """
    Modify the file content in a specific way:
    1. Convert all text to uppercase.
    2. Replace the word 'PYTHON' with 'PYTHON 🐍'.
    3. Strip leading and trailing whitespace from each line.
    """
    # Step 1: Convert to uppercase
    text = text.upper()

    # Step 2: Replace 'PYTHON' with 'PYTHON 🐍'
    text = text.replace("PYTHON", "PYTHON 🐍")

    # Step 3: Strip whitespace from each line
    lines = text.splitlines()
    stripped_lines = [line.strip() for line in lines]

    return "\n".join(stripped_lines)


def file_read_write(input_file, output_file):
    try:
        # Step 1: Read from the input file
        with open(input_file, "r") as infile:
            content = infile.read()

        # Step 2: Modify the content
        modified_content = modify_content(content)

        # Step 3: Write to the output file
        with open(output_file, "w") as outfile:
            outfile.write(modified_content)

        print(f"✅ File successfully processed. Modified content written to '{output_file}'")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


# --- Main Program ---
if __name__ == "__main__":
    input_file = "input.txt"    # Replace with your input file
    output_file = "output.txt"  # New file for modified content
    file_read_write(input_file, output_file)
