# Verified ID Filter

This repository contains a Python script that filters and compares ID strings between two lists. The script performs the following steps:

1. **Filters Verified Rows in List 1:**  
   It reads `list1.txt`, which is a tab-delimited file where each row may contain multiple columns. Only rows that include the word **"Verified"** in any column are considered, and from these rows, the first column (assumed to be the ID) is extracted.

2. **Compares Against List 2:**  
   It then reads `list2.txt`, a file where each line contains one ID. The script compares the verified IDs from `list1.txt` with the IDs in `list2.txt` and outputs those IDs that are not present in `list2.txt`.

## File Formats

### list1.txt

Each row in `list1.txt` is tab-delimited and may include multiple columns. The last column (or one of the columns) contains a comment, such as `Verified`. Only rows with "Verified" will be processed.  
Below is an example of the expected format:
72623017959621858	73818668470905844	74945461596862189		Verified
72552580630186885	74029912142432118	74029912142432118		Verified

- **Note:** In the above example, the first ID from the third and fifth rows will be extracted because those rows contain the word "Verified".

### list2.txt

Each line in `list2.txt` should contain a single ID string. For example:
74170580844197357
74522287126102257
73889105867455772
74100349538930991
74451849461141067

## How to Run

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
   cd <repository_directory>

2.Prepare Your Input Files:
--Place your list1.txt and list2.txt files in the repository directory.
--Ensure that the files follow the format described above.
3.Run the Script:
Execute the Python script using the command:
```python compare_ids.py list1.txt list2.txt```
The script will output the verified IDs from list1.txt that are not present in list2.txt.


