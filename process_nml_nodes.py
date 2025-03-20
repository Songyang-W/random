'''
example: python process_nml_nodes.py Merging-2.nml -c 100 -o selected_dendrite_75297030305563708.csv --zmin 1500 --zmax 3400
'''

import xml.etree.ElementTree as ET
import random
import csv
import argparse

def parse_nml(file_path):
    """
    Parse the NML file and return a list of node elements.
    Handles XML namespaces if present.
    """
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Extract namespace if present
        namespace = ''
        if '}' in root.tag:
            namespace = root.tag.split('}')[0] + '}'

        # Find all node elements
        nodes = root.findall('.//{}node'.format(namespace))
        return nodes, namespace
    except ET.ParseError as e:
        print(f"Error parsing NML file: {e}")
        return [], ''
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return [], ''

def select_random_nodes(nodes, count=30):
    """
    Randomly select 'count' number of nodes from the list.
    If there are fewer nodes than 'count', return all nodes.
    """
    if len(nodes) < count:
        print(f"Warning: Only {len(nodes)} nodes available. Returning all nodes.")
        return nodes
    return random.sample(nodes, count)

def process_coordinates(selected_nodes, z_min=1500, z_max=3400):
    """
    Extract x, y, z coordinates from selected nodes,
    apply z-coordinate condition (1500 <= z <= 3400),
    divide x and y by 8, round them to the nearest integer,
    and return a list of tuples.
    """
    processed_coords = []
    for node in selected_nodes:
        try:
            x = int(node.get('x'))
            y = int(node.get('y'))
            z = int(node.get('z'))
            
            # Apply z-coordinate condition
            if not (z_min <= z <= z_max):
                continue  # Skip nodes outside the z range
            
            # Divide x and y by 8 and round to nearest integer
            x_processed = round(x / 8)
            y_processed = round(y / 8)
            
            processed_coords.append((x_processed, y_processed, z))
        except (TypeError, ValueError) as e:
            print(f"Error processing node ID {node.get('id')}: {e}")
            continue
    return processed_coords

def write_coordinates_to_csv(coordinates, output_file='processed_coordinates.csv'):
    """
    Write the list of coordinate tuples to a CSV file.
    """
    try:
        with open(output_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['x', 'y', 'z'])  # Header
            writer.writerows(coordinates)
        print(f"Coordinates successfully written to {output_file}")
    except IOError as e:
        print(f"Error writing to file {output_file}: {e}")

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description='Process NML node coordinates with z-coordinate condition.')
    parser.add_argument('nml_file', help='Path to the NML file.')
    parser.add_argument('-c', '--count', type=int, default=30, help='Number of nodes to select.')
    parser.add_argument('-o', '--output', help='Output CSV file to save coordinates (optional).')
    parser.add_argument('--zmin', type=int, default=1500, help='Minimum z-coordinate value (inclusive).')
    parser.add_argument('--zmax', type=int, default=3400, help='Maximum z-coordinate value (inclusive).')

    args = parser.parse_args()

    # Step 1: Parse NML and get all nodes
    all_nodes, namespace = parse_nml(args.nml_file)
    if not all_nodes:
        return  # Exit if parsing failed or no nodes found

    # Step 2: Randomly select nodes
    selected_nodes = select_random_nodes(all_nodes, count=args.count)

    # Step 3: Process coordinates with z-coordinate condition
    coordinates = process_coordinates(selected_nodes, z_min=args.zmin, z_max=args.zmax)

    # Check if any coordinates meet the condition
    if not coordinates:
        print(f"No nodes found with z-coordinate between {args.zmin} and {args.zmax}.")
        return

    # Step 4: Output the coordinates
    if args.output:
        write_coordinates_to_csv(coordinates, output_file=args.output)
    else:
        print("Processed Coordinates (x,y,z):")
        for coord in coordinates:
            print(f"{coord[0]},{coord[1]},{coord[2]}")

if __name__ == "__main__":
    main()
