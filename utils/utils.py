import csv

dir = "./data/"
def load_file(csv_file):
    print(csv_file)

    with open(dir+csv_file, "r") as file:
        csv_reader = csv.DictReader(file)
        rows = [row for row in csv_reader]
        return rows