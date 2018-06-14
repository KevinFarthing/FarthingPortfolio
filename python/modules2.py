dict1 = {
    "name":"kevin",
    "age": 27,
    "sex": "M",
}

dict2 = {
    "name":"Megatron",
    "age":"ancient",
    "sex":"decepticon",
}

from IPython.display import clear_output
def show(list1):
    print(list1)
def help1():
    print("#INSTRUCTIONS\n    Enter ADD\n    Enter SHOW\n    Enter HELP\n    Enter CLEAR\n    Enter DELETE\n    Enter DONE")
def del_item(list1, item):
    if item in list1:
        list1.remove(item)
    else:
        print("that item is not in this list.")
        
def main():
    shopping_list = {}
    help1()
    while True:
        todo = input("What would you like to do? ").lower()
        clear_output()
        if todo =="done":
            print('Thank you for using my app')
            break
        elif todo == "show":
            show(shopping_list)
        elif todo == "help":
            help1()
        elif todo == "clear":
            what_clear = input("Which item would you like to clear?").lower()
            if what_clear in shopping_list.keys():
                shopping_list.pop(what_clear,None)
            else:
                print("That item is not in your cart")
        elif todo == "delete":
            del_item(shopping_list,input("which item would you like to remove? "))
        elif todo == "add":
            toadd=input("What would you like to add? ")
            if toadd in shopping_list.keys():
                while True:
                    what_do = input("this item already exists. Would you like to add an additional? y/n: ").lower()
                    if what_do == "n":
                        break
                    elif what_do == "y":
                        shopping_list[toadd] += 1
                        break
                    else:
                        print("Please enter 'y' or 'n'")
            else:
                shopping_list[toadd] = 1
        else:
            print("Please input a valid command.")
            
main()