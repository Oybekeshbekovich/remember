#Python writing files(.txt , .json, .csv)
text_data="Salom"
file_path="C:/Users/user/Desktop/you_tube/remamber.txt"

try:
    with open(file_path,"w") as file:
        file.write(text_data)
        file.write("\n")
        print(f"txt file saved to {file_path}")
except FileNotFoundError:
    print("File not found")
#json
import json

text_data={
    'Javohir':'55',
    'Sanjar':'22',
    'Abbos':'14'
}
file_path="C:/Users/user/Desktop/you_tube/remamber.txt"

try:
    with open(file_path,"w") as file:
        json.dump(text_data,file,indent=4)
        print(f"txt file saved to {file_path}")
except FileNotFoundError:
    print("File not found")
#csv
import csv
employees=[['Name','age','Job'],
           ['Ixtiyor',19,'Manager'],
           ['Aziz',20,'Shef'],
           ['Jamshid',22,'Officer'],]
file_path="C:/Users/user/Desktop/you_tube/remamber.txt"

try:
    with open(file_path,"w",newline='') as file:
        writer = csv.writer(file)
        for employee in employees:
            writer.writerow(employee)
        print(f"txt file saved to {file_path}")
except FileNotFoundError:
    print("File not found")
