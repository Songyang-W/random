import random

# Input file with 6470 lines
input_file = "coordinate_in_n.csv"
# Output file with 300 lines
output_file = "selected_coordinates.csv"

# Read all lines from the input file
with open(input_file, 'r') as file:
    lines = file.readlines()

# Filter lines based on the condition
filtered_lines = [line for line in lines if 1450 <= int(line.strip().split(',')[-1]) <= 3650]

# Randomly select 300 lines from the filtered lines
selected_lines = random.sample(filtered_lines, 300)

# Write the selected lines to the output file
with open(output_file, 'w') as file:
    file.writelines(selected_lines)

print(f"300 lines have been saved to {output_file}")
