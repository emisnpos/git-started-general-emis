print("Üdvözlöm! \n Ebbe a programba elvégezhet bármely matematikai számítást, \n Adja meg elöszőr az első számot, majd  következőt és végül a müveletet. ")

a = int(input("Adjon meg egy számot! "))
b = int(input("Adjon meg a második számot! "))
     
c = input("Adja meg a müveletet (+, -, *, /,)! ")

def x():
    if c == "+":
        print(a + b) 
    if c == "-":
        print(a - b) 
    if c == "*":
        print(a *b) 
    if c == "/":
        print(a / b) 

print("Tehát az Ön által kivánt müvelet nem más mint: ")
print( a, c, b, sep="")
print("Azaz: ")  
x()

# hello