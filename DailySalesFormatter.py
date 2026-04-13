import csv

output = []

for i in range(3):
    with open("./data/daily_sales_data_" + str(i) + ".csv", "r") as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            if row[0] == "pink morsel":
                sales = round(float(row[1][1:]) * float(row[2]), 2)
                output.append([sales, row[3], row[4]])

with open("./data/output.csv", "w", newline='') as csvfile:
    csvfile.write("Sales,Date,Region\n")
    for row in output:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerow(row)