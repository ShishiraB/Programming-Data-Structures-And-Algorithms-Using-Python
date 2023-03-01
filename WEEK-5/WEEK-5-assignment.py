# Create empty dictionaries to store books and borrowers
books = {}
borrowers = {}
# Create an empty list to store checkout data
checkouts = []
# Read input until the start of the books data is found
while input().strip() != "Books":
    pass
# Read book data and add it to the books dictionary
for line in iter(input, "Borrowers"):
    accession_number, title = line.split("~")
    books[accession_number] = title
# Read borrower data and add it to the borrowers dictionary
for line in iter(input, "Checkouts"):
    username, fullname = line.split("~")
    borrowers[username] = fullname
# Read checkout data and add it to the checkouts list
for line in iter(input, "EndOfInput"):
    username, accession_number, due_date = line.split("~")
    checkout_line = f"{due_date}~{borrowers[username]}~{accession_number}~{books[accession_number]}" #Stores in a formatted manner
    checkouts.append(checkout_line)
# Print the checkout data sorted by due date
for checkout in sorted(checkouts):
    print(checkout)