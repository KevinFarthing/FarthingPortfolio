# dict1 = {
#     "name":"kevin",
#     "age": 27,
#     "sex": "M",
# }

# dict2 = {
#     "name":"Megatron",
#     "age":"ancient",
#     "sex":"decepticon",
# }

# class GroceryItem:
#     def __init__(self, name, quantity):
#         self.name=name
#         self.quantity=quantity
    

# from IPython.display import clear_output
# # def show(list1):
# #     print(list1)
# # def help1():
# #     print("#INSTRUCTIONS\n    Enter ADD\n    Enter SHOW\n    Enter HELP\n    Enter CLEAR\n    Enter DELETE\n    Enter DONE")
# # def del_item(list1, item):
# #     if item in list1:
# #         list1.remove(item)
# #     else:
# #         print("that item is not in this list.")
# # def delete_item(list1):
# #     what_clear = input("Which item would you like to clear?").lower()
# #     if what_clear in list1.keys():
# #         list1.pop(what_clear,None)
# #     else:
# #         print("That item is not in your cart")
# # def add_item(list1):
# #     toadd=input("What would you like to add? ")
# #     if toadd in list1.keys():
# #         while True:
# #             what_do = input("this item already exists. Would you like to add an additional? y/n: ").lower()
# #             if what_do == "n":
# #                 break
# #             elif what_do == "y":
# #                 list1[toadd] += 1
# #                 break
# #             else:
# #                 print("Please enter 'y' or 'n'")
# #     else:
# #         list1[toadd] = 1
        
# def main():
#     shopping_list = {}
#     help1()
#     while True:
#         todo = input("What would you like to do? ").lower()
#         if todo =="done":
#             print('Thank you for using my app')
#             break
#         elif todo == "show":
#             show(shopping_list)
#         elif todo == "help":
#             help1()
#         elif todo == "clear":
#             clear_output()
#         elif todo == "delete":
#             delete_item(shopping_list)
#         elif todo == "add":
#             add_item(shopping_list)
#         else:
#             print("Please input a valid command.")

from IPython.display import clear_output
shopping_cart = []
def help1():
    print("#INSTRUCTIONS\n    Enter ADD\n    Enter SHOW\n    Enter HELP\n    Enter CLEAR\n    Enter DELETE\n    Enter DONE")
    
class Grocery:
    def __init__(self, name, quantity=1):
        self.name=name
        self.quantity=quantity
        
    def add(self,to_add=1):
        self.quantity+=to_add
        #only adds if it's already initialized
        
    def remove(self,to_remove=1):
        self.quantity-=to_remove
        #add a bit in the main() that removes the object from shopping_cart if item.quantity==0
        
def y_n():
    com = ""
    while com != "y" and com != "n":
        com = input("Would you like to continue? y/n").lower
    return com=="y"

def show(list1):
    for each in list1:
        print(str(each.name) + ": " + str(each.quantity))
        

def main():
    shopping_list = []
    help1()
    while True:
        todo = input("What would you like to do? ").lower()
        if todo =="done":
            show(shopping_list)
            print('Thank you for using my app')
            break
        elif todo == "show":
            show(shopping_list)
        elif todo == "help":
            help1()
        elif todo == "clear":
            clear_output()
        elif todo == "add":
            to_add = str(input("What would you like to add: ")).lower()
            how_many = int(input("How many: "))
            present = False
            for each in shopping_list:
                if each.name == to_add:
                    print(f"There are already {each.quantity} {each.name} in your shopping list.")
                    present = True
                    if y_n():
                        each.add(how_many)
            if not present:
                shopping_list.append(Grocery(to_add,how_many))
                
                
           
        elif todo == "delete":
            to_remove = str(input("What would you like to remove: ")).lower()
            present = False
            for each in shopping_list:
                if each.name == to_remove:
                    shopping_list.remove(each)
            if not present:
                shopping_list.append(Grocery(to_add,how_many))
                
                
        else:
            print("Please input a valid command.")
    
            
main()