from datetime import date
def CalculateAge(birthday):
    birthday = birthday.split('/')
    today = date.today()
    age = today.year - int(birthday[2])
    if today.month < int(birthday[1]) or today.day < int(birthday[0]):
        age = age - 1
    return age

print("Hello World!")
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
