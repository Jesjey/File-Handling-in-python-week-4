#Question 2
def read_file_with_error_handling():
    # Ask the user for a filename
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, "r") as file:
            content = file.read()
            print("\n✅ File Contents:\n")
            print(content)

    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"⚠️ Error: You do not have permission to read '{filename}'.")
    except Exception as e:
        print(f"⚡ An unexpected error occurred: {e}")


# --- Main Program ---
if __name__ == "__main__":
    read_file_with_error_handling()