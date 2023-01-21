import csv

field_names = ["Name", "Author", "Publisher", "Price", "Category"]

book1 = ["computer programming part 1", "tamim shariar subeen", "onnorokom pathshala", "240.00", "programming"]
book2 = ["computer programming part 2", "tamim shariar subeen", "dimik prokashoni", "270.00", "programming"]
book3 = ["lean programming with python", "tamim shariar subeen", "dimik prokashni", "340.00", "programming"]

book_list = [book1, book2, book3]

with open("book.csv", "w") as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=',', quotechar="\"", quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(field_names)
    for book in book_list:
        csv_writer.writerow(book)