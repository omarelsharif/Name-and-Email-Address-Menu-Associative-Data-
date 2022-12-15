

# Omar El-Sharif

'''This project collects customer information by keeping names
and email addresses in a dictionary as key-value pairs.
It displays a menu that lets the user look up a person’s email address,
add a new name and email address, change an existing email address,
and delete an existing name and email address.
The program saves the data stored in a dictionary
to a file when the user exits the program.
Each time the program starts,
it retrieves the data from the file and stores it in a dictionary.
'''



def loaddata():
    filename = "book.txt" 
    file1 = open(filename,"r")
    file = file1.read()
    file = file.split(" ")
    book = {}
    x = len(file)

   
    for i in range(0, x-1,2):
        z = file[i] 
        book[z] = file[i+1]
    
    return (book)



def exportdata(book):

    blank = "" 

    file1 = open("book.txt", "w")

    for word in book:
        blank += word
        blank += " "
        blank += book[word]
        blank += " "
    file1.write(blank)
    file1.close()
    print("Information saved")
    


def one(book):
    name = input("Enter name: ")
    if name not in book:
        print("The specified name was not found")
    else:
        print("Name: ", name)
        print("Email:", book[name])

def two(book):

    name = input("Enter name: ")
    address = input("Enter an email address: ")
    if name in book:
        print("That name already exists")
    else:
        book[name] = address
        print("Name and address have been added") 

    return (book)



def three(book):
    name = input("Enter name: ")
    address = input("Enter the new address: ")  
    book[name] = address
    print("Information updated")
    
    return (book)



def four(book):
    name = input("Enter name: ")
    if name not in book:
        print("The specified name was not found")
    else:
        del book[name]  
        print("Information deleted")
    
    
    return (book)


def menu(): 
    print(' ') 
    print("Menu")
    print("-----------------------------")
    print("1. Look up an email address")
    print("2. Add a new name and email address")
    print("3. Change an existing email address")
    print("4. Delete a name and email address")
    print("5. Quit the program")
    print(" ")



def main():
    
    choice = 0
    #book ={}
    book = loaddata() 
    while choice!="5":
        menu()
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            one(book)
        elif choice == "2":
            book = two(book)
        elif choice == "3":
            book = three(book)
        elif choice == "4":
            book = four(book)

        elif choice== "5":
            exportdata(book)  
            
        else:
            print("Try again. Invalid input.")
    #print(book)

    

main() 
