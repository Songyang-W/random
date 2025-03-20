import sys

def load_list2(file_path):
    """Load IDs from list 2, one per line (removing any extra quotes)."""
    with open(file_path, 'r') as f:
        # Remove whitespace and any extraneous quotes
        return {line.strip().strip("'") for line in f if line.strip()}

def load_verified_ids(file_path):
    """
    Load the verified IDs from list 1.
    Each line is assumed to be tab-delimited.
    Only lines containing the word "Verified" are processed.
    The first column is taken as the ID.
    """
    verified_ids = []
    with open(file_path, 'r') as f:
        for line in f:
            # Check if the line has the comment "Verified"
            if "Verified" in line:
                # Split the line by tab
                parts = line.strip().split('\t')
                if parts:
                    # Remove extraneous quotes and whitespace from the first id
                    verified_ids.append(parts[0].strip().strip("'"))
    return verified_ids

def main():
    if len(sys.argv) < 3:
        print("Usage: python script.py list1.txt list2.txt")
        sys.exit(1)

    list1_file = sys.argv[1]
    list2_file = sys.argv[2]

    # Load IDs from list2 and verified IDs from list1
    list2_ids = load_list2(list2_file)
    verified_ids = load_verified_ids(list1_file)

    # Filter: only include verified ids that are not in list2
    missing_ids = [id_str for id_str in verified_ids if id_str not in list2_ids]

    print("Verified IDs not found in list2:")
    for id_str in missing_ids:
        print("'"+id_str)

if __name__ == '__main__':
    main()
