import fitz
import re
import csv
import os

# specify the path to the PDF file
pdf_path = "/Users/mm527x/Documents/Therapy/kammer.pdf"

# specify the path to the output CSV file
csv_path = os.path.expanduser("emails3.csv")

# open the PDF
with fitz.open(pdf_path) as doc:
    emails = []
    for page in doc:
        # get the text on the page
        text = page.get_text()

        # find all email addresses on the page
        email_list = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)

        # add the email addresses to the list
        emails += email_list

# write the emails to the CSV file
with open(csv_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Emails'])
    for email in emails:
        writer.writerow([email])

print(f"{len(emails)} email addresses were found and saved to {csv_path}")
