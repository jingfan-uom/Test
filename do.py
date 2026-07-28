import csv


if __name__ == "__main__":
    data_path = "/Users/user/Test/Iris.csv"

    with open(data_path, 'r', newline='') as input_data:
        reader = csv.DictReader(input_data)

        for row in reader:
            print(row)
