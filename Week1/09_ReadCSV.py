import csv

def read_csv_file():
    with open('data/homework_invoices.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        invoice_greater = 0
        Invoice_missing = 0
        total_Invoices = 0

        for row in csv_reader:
            vendor = row['vendor']
            amount = row['amount']
            status = row['status']
            invoice_id = row['invoice_id']

            try:
                if float(amount) > 100000:
                    invoice_greater = invoice_greater +1;
            except ValueError:
                    Invoice_missing = Invoice_missing + 1

            total_Invoices = total_Invoices + 1

        print("Total invoices processed:", total_Invoices)
        print("Invoices with amount greater than 100000:", invoice_greater)
        print("Invoices with missing amounts:", Invoice_missing)

read_csv_file()