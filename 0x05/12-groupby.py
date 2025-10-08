#!/usr/bin/python
"""A module that displlays informatio about specified platform on  csv """
import csv

def dictreader(filename, target):
    """A function that displays information about specified platform on csv """

    with open(filename, encoding="utf-8") as file:
        datas = csv.DictReader(file)
        for data in datas:
            if data['platform'] == target
                with open("games.csv", "a+", encoding="utf-8") as file:
                    csv.writer(file).writerow(data.values())    

if __name__=="__main__":
    dictreader("game_details.csv", "PS3")
    
    