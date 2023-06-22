x = 5
y = 0

try:
    print(x / y)
except ZeroDivisionError:
    print("You cannot divide a number by zero")



#program to read student emotions


#EXERCISE
emotion_dict = {
    1: "I guess something is wrong. Let's have a chat...may be it will make you feel better",
    2: "What is wrong?",
    3: "Not so bad. But you could be better",
    4: "This is slightly below average. Try listening to music",
    5: "This is average. You could be better",
    6: "This is above average. You are doing great",
    7: "This is great. Keep it up",
    8: "This is very great. You are doing very well",
    9: "This is excellent. You are doing excellent",
    10: "This is outstanding. You are outstanding"

}

feeling = input("Give a rating of your feeling in the range 1 to 10: ")

try:
    feeling = int(feeling)    
    if feeling >5:
        print("Number not in range.")
    elif 1 < feeling < 5:
        print(emotion_dict[feeling])
        shared_feeling = input("You can share with me what you're feeling or talk to a friend? ")
        if shared_feeling != "":
            print("Thank you for sharing with me. Let me connect you to a pyschologist for more help")
            print(shared_feeling)
        else:
            exit()
    else:
        print(emotion_dict[feeling])
except ValueError:
    print("Please enter a number in the range 1 to 5.")
    exit()
finally:
    print("Thank you for your participation.")
