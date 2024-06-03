import csv


name=[
    {"Fname":"pankaj","Lname":"Lohar"},
    {"Fname":"pankaj","Lname":"Lohar"},
    {"Fname":"pankaj","Lname":"Lohar"},
    {"Fname":"pankaj","Lname":"Lohar"},
    {"Fname":"pankaj","Lname":"Lohar"},
    {"Fname":"pankaj","Lname":"Lohar"},
    {"Fname":"pankaj","Lname":"Lohar"}
]

with open('name.csv',mode='w')as csvfile:
    fieldnames= name[0].keys()
    writer =csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
    for row in name:
        writer.writerow(row)