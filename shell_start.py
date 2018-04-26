import os
import shutil
from os import path
from shutil import make_archive
from zipfile import ZipFile



def main():
    if path.exists("newfile.txt"):
        src = path.realpath("newfile.txt")
        with ZipFile("testzip.zip", "w") as newzip:
            newzip.write("newfile.txt")
            newzip.write("textfile.txt.bak")
        
        
        
        
        
              
if __name__ == "__main__":
  main()
