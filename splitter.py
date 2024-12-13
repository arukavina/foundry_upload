import os
import math


def split_text_file(file_path, num_parts=20):
    if not os.path.isfile(file_path):
        print("File does not exist.")
        return

    # Read the file content
    with open(file_path, 'r') as file:
        lines = file.readlines()

    if len(lines) < 2:
        print("File has less than two rows. Unable to split.")
        return

    # Extract the header
    header = lines[:2]

    # Calculate the size of each part (excluding the header repetition)
    total_lines = len(lines) - 2
    lines_per_part = math.ceil(total_lines / num_parts)

    # Directory and base filename
    directory, base_filename = os.path.split(file_path)
    name, ext = os.path.splitext(base_filename)

    # Split and write each part
    for i in range(num_parts):
        start_index = 2 + i * lines_per_part
        end_index = start_index + lines_per_part
        part_lines = lines[start_index:end_index]

        if not part_lines:
            break

        # Create the part filename
        part_filename = os.path.join(directory, f"{name}_part{i + 1}{ext}")

        # Write the header and part lines
        with open(part_filename, 'w') as part_file:
            part_file.writelines(header + part_lines)

        print(f"Part {i + 1} written to {part_filename}")

# Run
split_text_file('C:\\Users\\arukavina\\file.ext', 20)
