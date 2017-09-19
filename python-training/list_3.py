import os

print("Insturctions: Type in items. Type DONE when finished!\n"
      "you can always type HELP.\n")
#create list
shopping_list = []

def clear_screen():
    os.system("cls" if os.name == 'nt' else "clear")


def str_eval(new_item):
    clear_screen()
    if new_item.upper() == "DONE" or new_item.upper() == 'QUIT':
        #end loop and print list
        print_list()
        exit()
    elif new_item.upper() == "SHOW":
        #show list
        print_list()
    elif new_item.upper() == "HELP":
        #print help instructions
        print("DONE to quit, REMOVE to delete an item,"
        " HELP for help, SHOW for current list")
    elif new_item.upper() == "REMOVE":
        remove_from_list()
        #print help instructions
    else:
        add_to_list(new_item)

def remove_from_list():
    print_list()
    what_to_remove = input("What would you like to remove?\n")

    try:
        shopping_list.remove(what_to_remove)
    except ValueError:
        pass
    print_list()


def add_to_list(new_item):

    print_list()

    #determine where in list item should be added
    if len(shopping_list):
        position = input("where shoud I add {}? \n"
                         "Press ENTER to add to the end of the list\n"
                         "> ".format(new_item))
    else:
        position = 0

    try:
        position = abs(int(position))
    except ValueError:
        position = None


    if position is not None:
        shopping_list.insert(position -1, new_item)
    else:
        shopping_list.append(new_item)
        #else append word to list
    print_list()
#print list function
def print_list():
    clear_screen()
    print("Here are the items in your list!")
    index = 1
    for item in shopping_list:
        print("{}. {}".format(index, item))
        index +=1
    print("-"*10)

#infinite loop to accept words into variable and store in list
while True:
    new_item = input('> ')
    str_eval(new_item)
