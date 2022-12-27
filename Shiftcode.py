import sys
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v",\
    "w","y","z"]

def data():


    message = input("Enter a message: ")
    message = message.lower()
    num = int(input("Enter between (1-26): "))
    while num >26 or num == 0:
        num = int(input("Enter between (1-26): "))
    all = (message,num)
    return all

def code(message,num):
    nword = ""
    for x in message:
    
        y = alphabet.index(x)
        y = y + num
        if y > 24:
            y = y-24
        char = alphabet[y]
        nword = nword + char
    print(nword)
    
def decode(message,num):
    nword = ""
    for x in message:
        
        y = alphabet.index(x)
        y = y - num
        if y < 0:
            y = y + 24
        char =alphabet[y]
        nword = char + nword
        nword1 = nword[::-1]
        print(nword1)

  
    
        

def main():
    again= "y"
    while again == "y":
        print("1) Make a code")
        print("2)Decode a message")
        print("3)Quit")
        choose = int(input("Enter your choice: "))
        if choose == 1:
            message,num = data()
            code(message,num)
        elif choose == 2:
            message,num = data()
            decode(message,num)
        elif choose  == 3:
            sys.exit()
        else:
            print("Incorrect Selection")
main()


    

    
        
    



