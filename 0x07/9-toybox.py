#!/usr/bin/python
"""A module that creates a toy box"""


class ToyBox:
    def __init__(self, color="red", size="medium", toy_count=5):
        self.color = color
        self.size = size
        self.toy_count = toy_count

    def add_toy(self):
        self.toy_count += 1
        print("A toy was added!")

    def describe_box(self):
        print(f"This is a {self.color} {self.size} toy box with {self.toy_count} toys.")



if __name__ =="__main__":
    box = ToyBox("blue", "large", 10)
    box.describe_box()     
    box.add_toy()         
    box.add_toy()          
    box.describe_box()   

