import sys


alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v",\
    "w","y","z"]



def data():
    message = input("Enter a word: ")
    message = message.lower()
    num = int(input("Enter a number: "))
    while num >26 or num == 0:
        num = int(input("Enter a number: "))
    all = (message,num)
    return all

def code(message,num):
    newword = ""
    for x in message:
        y = alphabet.index(x)
        y = y + num
        if y > 24:
            y = y - 24
        char = alphabet[y]
        newword = newword + char
    print(newword)

def decode(message,num):
    newword = ""
    for x in message:
        y = alphabet.index(x)
        y = y - num
        if y < 0:
            y = y + 24
        char = alphabet[y]
        newword = char + newword
        nword1 = newword[::-1]
    print(nword1)

def main():
    again = "y"
    while again == "y":
        print("1) Make a code")
        print("2) Decde a message")
        print("3)Quit")
        selection = int(input("Enter your selection: "))
        if selection == 1:
            message,num = data()
            code(message,num)
        elif selection == 2:
            message,num = data()
            decode(message,num)
        elif selection == 3:
            sys.exit()
main()

        
