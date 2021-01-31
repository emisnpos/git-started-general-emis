def get_hello_message():
    name = input("What's your name? ")
    if name != "":
        return 'Hello, ' + name + '!'
    else:
        return 'Hello, World!'
        
def say_hello():   
    message = get_hello_message()
    print(message)

say_hello()
