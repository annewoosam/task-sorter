print("create a quick, no duplicate, alphabetical shopping list by entering items then hitting enter when done.")
shopping_list=[]
while True:
    add_item=input("add item>")
    if add_item.lower()!="":
        shopping_list.append(add_item.lower())
        
        shopping_list=set(shopping_list)
        print( "\noriginal order - no duplicates\n")
        print(shopping_list)
        
        shopping_list=list(shopping_list)
        print("\nduplicates removed and sorted\n")
        print(sorted(shopping_list))
    else:
        print("\nYour final list is:\n")
        print(sorted(shopping_list))
        break
    