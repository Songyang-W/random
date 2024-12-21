#!/usr/bin/env python3

import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: n2w.py num1,num2,num3,... or n2w.py num1 num2 num3 ...")
        sys.exit(1)
    
    input_args = sys.argv[1:]
    numbers = []
    
    for arg in input_args:
        # Split by comma if present
        parts = arg.split(',')
        for part in parts:
            part = part.strip()
            if part:  # Avoid empty strings
                try:
                    numbers.append(int(part))
                except ValueError:
                    print(f"Error: '{part}' is not a valid integer.")
                    sys.exit(1)
    
    # Process the numbers: multiply the first two by 8 and leave the rest unchanged
    processed = []
    for i, num in enumerate(numbers):
        if i < 2:
            multiplied = num * 8
            processed.append(str(multiplied))
        else:
            processed.append(str(num))
    
    # Join the processed numbers back into a comma-separated string
    output = ",".join(processed)
    print(output)

if __name__ == "__main__":
    main()
