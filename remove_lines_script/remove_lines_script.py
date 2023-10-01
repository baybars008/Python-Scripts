# This script removes all lines up to a specified line number from a text file and writes the rest to a new file.

def remove_lines(input_file, output_file, line_number):
    # Reads the input file and stores the lines in a list.
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # Displays an error message and exits if an invalid line number is provided.
    if line_number < 1 or line_number > len(lines):
        print("Invalid line number.")
        return

    # Retrieves lines up to the specified line number.
    new_lines = lines[line_number:]

    # Writes the remaining lines to a new file.
    with open(output_file, 'w') as f:
        f.writelines(new_lines)

    # Notifies the user that lines up to the specified line number have been removed.
    print(f"Lines up to {line_number} have been removed.")

if __name__ == "__main__":
    # Takes the input file name, output file name, and the line number to be removed from the user.
    input_file = "text_file.txt"  # You can change the name of the input file.
    output_file = "new_text_file.txt"  # You can change the name of the output file.
    line_number = int(input("Up to which line should be removed? "))

    # Calls the remove_lines function to perform the operation.
    remove_lines(input_file, output_file, line_number)