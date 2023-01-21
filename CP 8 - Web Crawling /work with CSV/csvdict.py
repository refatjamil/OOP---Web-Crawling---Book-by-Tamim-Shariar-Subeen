import csv

fields_names = ["Name", "Author", "Publisher", "Price"]
book1 = {"Name": "Computer Programming, Part 1", "Author":"Tamim Shahriar Subeen", "Publisher":"Onnorokom Prokashoni", "Price":"240.00"}
book2 = {"Name": "Computer Programming, Part 2", "Author":"Tamim Shahriar Subeen", "Publisher":"Dimik Prokashoni", "Price":"240.00"}
book3 = {"Name": "Learn Programming in python", "Author":"Tamim Shahriar Subeen", "Publisher":"Dimik Prokashoni", "Price":"200.00"}

book_list = [book1, book2, book3]

with open("bool_list.csv", "w") as csvf:
    csv_writer = csv.DictWriter(csvf, fieldnames=fields_names)
    csv_writer.writeheader()
    csv_writer.writerows(book_list)