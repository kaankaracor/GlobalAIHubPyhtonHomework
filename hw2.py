liste = []

first_name = input("Please enter your first name:")
liste.append(first_name)
last_name = input("Please enter your last name:")
liste.append(last_name)
age = int(input("Please enter your age:"))
liste.append(age)
date_of_birth = int(input("Please enter your year of birth:"))
liste.append(date_of_birth)

for i in liste:
    print("First name:{}\nLast name:{}\nAge:{}\nYear of birth:{}".format(first_name,last_name,age,date_of_birth))
    if(int(liste[2]) < 18 and int(liste[2]) > 0 ):
        print("You can't go out because it's too dangerous!!")
        break

    elif(int(liste[2]>=18)):
        print("You can go out the street.")
        break

    else:
        print("The age value is impossible!")
        break

