#MEMBERSHIP OPERATORS
word="apple"
text=input('Enter your text:')
if text in word:
    print(f'{text} is in the word')
else:
    print(f'{text} is not in the word')

gradued={
    'Oybek':'A',
    'Abbos':'B',
    'Abror':'C',
}
student=input("Enter your name: ")
if student in gradued:
    print(f"{student} was {gradued[student]} is graduated.")
else:
    print(f"{student} was {gradued[student]} is not graduated.")
email="eshbekovich1@gmail.com"
if "@" in email and "." in email:
    print("email is valid")
else:
    print("email is not valid")
