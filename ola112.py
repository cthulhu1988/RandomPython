# OLA112 BY Isaac Callison,  CSCI 1170-007,  Due: 11/08/16
# PROGRAM ID:  consolidate.py / The Consolidation Problem
# AUTHOR: Isaac Callison
# INSTALLATION:  MTSU
# REMARKS:

import os.path

# File name constants
FILE_NAME1  = "store1.dat"
FILE_NAME2  = "store2.dat"
MERGED_FILE = "merged.dat"
REJECT_FILE = "reject.dat"

def main():
    # Open the input files
    if not os.path.isfile(FILE_NAME1) or not os.path.isfile(FILE_NAME2):
        return
    file1  = open(FILE_NAME1,'r')
    file2  = open(FILE_NAME2,'r')
    merged = open(MERGED_FILE, 'w')
    reject = open(REJECT_FILE, 'w')

    # Conflate inventory items from the two input files.
    eof1, sku1, amt1, uom1 = obtain_record(file1)
    eof2, sku2, amt2, uom2 = obtain_record(file2)
    while not eof1 or not eof2:
        pass # ...remove and replace with working code
        # Hint: Pattern your logic around that of $PUB/conflate.py

    # Close all files.
    file1.close()
    file2.close()
    merged.close()
    reject.close()


# Obtain an inventory item from specified file.
def obtain_record(file):
