import csv

# take user input for PRN
PRN = input("Enter PRN: ")
Merchant2=""
AMOUNT=0
flag=0
Balance=0
# open csv file and check if PRN is found and active
with open('data2.csv', mode='r') as file:
    reader = csv.reader(file)
    rows = list(reader)
    for row in rows:
        if row[1] == PRN:
            flag=1
            if row[4] == 'Inactive':
                print("User inactive")
                exit()
            elif row[4] == 'Active':
                # take user input for Amount
                Merchant=input("Enter Merchant Name: ")
                Merchant2=Merchant
                Amount = int(input("Enter amount: "))
                AMOUNT=Amount
                if(Amount < 0):
                    print("Invalid Amount")
                    exit()
                if Amount > int(row[2]):
                    print("Insufficient balance")
                    exit()
                else:
                    # take user input for PIN
                    PIN = input("Enter PIN: ")
                    if PIN == row[3]:
                        # subtract entered amount from balance and update csv
                        new_balance = int(row[2]) - Amount
                        Balance=new_balance
                        row[2] = str(new_balance)
                        with open('data2.csv', mode='w', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerows(rows)
                        print("New balance:", new_balance)
                        # Open the file in append mode

                    else:
                        print("Wrong PIN")
                        exit()

if(flag ==0):
    print("PRN not found")
    exit()
# prompt the user for new values
# create a list of the new row values
new_row = [PRN, Merchant2, AMOUNT, Balance]

# open the CSV file in append mode
with open('transaction.csv', 'a', newline='') as file:

    # create a CSV writer object
    writer = csv.writer(file)

    # append the new row to the file
    writer.writerow(new_row)
    exit()
# if PRN is not found in csv file

