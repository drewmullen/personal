print("Insturctions: Type in items. Type DONE when finished!")
#create list
shopping_list = []

def str_eval(new_item):
    if new_item.upper() == "DONE":
        #end loop and print list
        print_list()
        exit()
    elif new_item.upper() == "SHOW":
        #show list
        print_list()
    elif new_item.upper() == "HELP":
        #print help instructions
        print("DONE to quit, HELP for help, SHOW for current list")
    else:
        add_to_list(new_item)

def add_to_list(new_item):
    #else append word to list
    shopping_list.append(new_item)
    print("Added {}. List now has {} items.".format(new_item, len(shopping_list)))

#print list function
def print_list():
    print("Here are the items in your list!")
    for item in shopping_list:
        print(item)

#infinite loop to accept words into variable and store in list
while True:
    new_item = input('> ')
    str_eval(new_item)
