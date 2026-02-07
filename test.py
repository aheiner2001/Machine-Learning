import csv
with open('pizza.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['date'])



        # this is from the git branch test
        print("this is a test branch using git")
print(row)