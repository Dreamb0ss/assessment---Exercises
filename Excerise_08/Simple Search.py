names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]  
# list of names

search = input("Enter name to search: ")  
# ask user for a name to search

if search in names:
    print("Name found")  
    # message if the name exists in the list
else:
    print("Name not found")  
    # message if the name does not exist
