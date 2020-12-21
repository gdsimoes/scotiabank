#!/usr/bin/env python3

import csv


def add_transfer(transfer, list):
    """
    Add transfer to list
    """

    for month in list:
        if month["date"] == transfer["date"]:
            month["price"] += transfer["price"]
            return

    list.append(transfer)


# global variables
list_of_months = []
keys = ["date", "price"]

# parse the bank file and save the data in list_of_months
with open("pcbanking.ascii") as file:
    reader = csv.reader(file)

    for row in reader:
        # only the first two fields are necessary
        date, price = row[:2]

        # remove day from date and put year in front
        date = date.split('/')[2] + "/" + date.split('/')[0]

        transfer = {"date": date, "price": float(price)}
        add_transfer(transfer, list_of_months)

# generate a report and save it in the 'result.txt' file
with open("result.txt", "w") as file:
    writer = csv.DictWriter(file, fieldnames=keys)
    writer.writeheader()
    writer.writerows(list_of_months)
