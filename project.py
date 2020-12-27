import random

def information():
    i = 0
    name = "KAAN"
    surname = "KARAÇOR"
    while i < 3:
        x = input("Please enter your name:")
        y = input("Please enter your surname:")
        x = x.upper()
        y = y.upper()
        if(x==name and y==surname):
            return print("WELCOME")
        else:
            i+=1
            print("Please check your information!!!\n")
            if(i==3):
                return print("Please try again later")

information()

def take_courses():
    courses = ["math", "physics", "chemistry", "biology", "geometry"]
    print("Courses:%s\nWARNING = Take a minimum of 3 and maximum of 5 lessons! "%courses)
    i = 0
    list = []
    while i < 5:
        a = input("Please select a course you want(if you want to quit or finish your choice press 'q':")

        if(a=="q"):
            break

        list.append(a)

        i += 1


    if (len(list) < 3 ):
        print("You failed in class")

    return list

liste = take_courses()


def choose_lesson(x):
    a = random.choice(x)
    return a

lesson = choose_lesson(liste)


dic_lesson = {"midterm":90,"final":80,"project":100}

def student_grade(dic_lesson):
    note = 3/10*dic_lesson["midterm"] + 5/10*dic_lesson["final"] + 2/10*dic_lesson["project"]
    if(note>90):
        return "AA"
    elif(note> 70 and note< 90):
        return "BB"
    elif (note > 50 and note < 70):
        return "CC"
    elif (note > 30 and note < 50):
        return "DD"
    else:
        return "FF"

grade = student_grade(dic_lesson)
print("Kaan Karaçor got %s from %s class"%(grade,lesson))
