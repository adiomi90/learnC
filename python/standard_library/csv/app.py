import csv

with open(r"python\standard_library\csv\data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["transactions_id", "product_id","price"])
    writer.writerow([1000, 1, 5])
    writer.writerow([1000, 5, 50])
    writer.writerow([1000, 11, 51])
    writer.writerow([1000, 3, 55])


    #reader = csv.reader(file)
    #print(list(reader))