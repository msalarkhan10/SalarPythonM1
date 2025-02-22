from datetime import date
def CalculateAge(birthday):
    birthday = birthday.split('/')
    today = date.today()
    age = today.year - int(birthday[2])
    if today.month < int(birthday[1]) or today.day < int(birthday[0]):
        age = age - 1
    return age
def DrawDiamond():   
    height = 4
    
    # This for loop prints the first half of the diamond
    for i in range(height):
        print(" " * (height - i) + "*" * (i * 2 + 1))
    
    #This for loop prints the second half of the diamond
    for i in range(1, height):
        print(" " * (i + 1) + "*" * (2 * height - i * 2 - 1)) 
print("Welcome to python chatbot :D")
while True:
    print("Hi what is your name?")
    name=input()
    if len(name)< 2:
        print("Too short ")
        name=input()
    elif len(name)> 10:
        print("Your name is too long write your correct name")
        name=input()
    print("Ok your name is",name)
    print("What is your birthday, write it in this format DD/MM/YYYY")
    birthday=input()
    print("Your birthday is ",birthday)
    age=CalculateAge(birthday)
    print("your age is",age)
    print("The numbers of letters in salar are ",len(name))
    print("Do you perfer Diamond shape or Rectangle shape? enter the shape you want")
    shape=input()
    if shape == "Diamond" or shape == "diamond":
        DrawDiamond()
    elif shape == 'Rectangle' or shape == "rectangle":
        for i in range(5):
            print("*" * 4)
    print("Is there anyone else who wishes to use the chatbot? Yes or No?")
    user=input()
    if user == "yes" or user == "Yes":
        continue
    else:
        break

