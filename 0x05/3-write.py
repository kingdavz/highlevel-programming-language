#!/usr/bin/python
""""A module that can write a file"""

def writefile(filename, content):
    """A function that write content in a file"""
    file = open(filename, "w")
    file.write(content)
    file.close()



if __name__ == "__main__":
    writefile("example.txt", "python programming is awesome!")
