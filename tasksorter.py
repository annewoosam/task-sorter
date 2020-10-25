print("create a quick, no duplicate, alphabetical to-do-list by entering items then hitting enter when done.")
todo_list=[]
while True:
    add_item=input("add item>")
    if add_item.lower()!="":
        todo_list.append(add_item.lower())
        
        todo_list=set(todo_list)
        print( "\noriginal order - no duplicates\n")
        print(todo_list)
        
        todo_list=list(todo_list)
        print("\nduplicates removed and sorted\n")
        print(sorted(todo_list))
    else:
        print("\nYour final list is:\n")
        print(sorted(todo_list))
        break
    