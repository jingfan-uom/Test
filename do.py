import csv


if __name__ == "__main__":
    data_path = "/Users/user/Test/Iris.csv"

    with open(data_path, 'r', newline='') as input_data:
        reader = csv.DictReader(input_data)

        for row in reader:
            print(row)

    def find_a_name(x):
        print("his name is" , x)
    a="jingfan"
    find_a_name(a)


print('player 2')
print('player 2')
print('player 2')
print('player 2')
print('player 2')