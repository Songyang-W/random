#!/usr/bin/env python3

import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: w2s.py num1,num2,num3,...")
        sys.exit(1)
    
    input_str = sys.argv[1]
    # Split the input by comma and remove any surrounding whitespace
    numbers_str = [num.strip() for num in input_str.split(',')]
    
    try:
        # Convert all inputs to integers
        numbers = [int(num) for num in numbers_str]
    except ValueError:
        print("Error: All inputs must be integers.")
        sys.exit(1)
    
    # Process the numbers: divide the first two by 2(since the segmentation is 15nm/pxl and raw EM is 7.5nm/pxl) and round down
    processed = []
    for i, num in enumerate(numbers):
        if i < 2:
            divided = num // 8
            processed.append(str(divided))
        else:
            processed.append(str(num))
    
    # Join the processed numbers back into a comma-separated string
    output = ",".join(processed)
    print(output)

if __name__ == "__main__":
    main()

