print("Insturctions: Type in items. Type DONE when finished!")
#create list
shopping_list = []


#infinite loop to accept words into variable and store in list
while True:
    new_item = input('> ')

    # if word is 'DONE', break
    if new_item.upper() == "DONE":
        break
    #else append word to list
    shopping_list.append(new_item)

#print list
for item in list:
    print(item)
