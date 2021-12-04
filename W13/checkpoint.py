message = input('What is your message: ')

def display_regular(string):
    print(string)
    
def display_uppercase(string):
    uppercase = string.upper()
    print(uppercase)

def display_lowercase(string):
    lowercase = string.lower()
    print(lowercase)

def main():
    display_regular(message)
    display_uppercase(message)
    display_lowercase(message)

main()