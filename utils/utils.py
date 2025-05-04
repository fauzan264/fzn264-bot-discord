import csv
import random

dir = "./data/"
def load_file():
    csv_file = "quotes.csv"
    
    with open(dir+csv_file, "r") as file:
        csv_reader = csv.DictReader(file)
        rows = [row['quotes'] for row in csv_reader]
        return random.choice(rows)