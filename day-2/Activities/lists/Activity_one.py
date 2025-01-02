# Write programs using list methods:
#     Add/remove elements dynamically.

def activity_one():
    list=[]
    while(True):
        print("""
                Enter 1 to add Elements in list
                Enter 2 to removing an element
                Enter 3 to print the list
                Enter 0 to quit
                
              """)
        value = int(input())
        if value == 1:
            element = input('Enter Element to add : ')
            list.append(element)
        elif value == 2:
            try:
                element =input('Enter Element to remove : ')
                list.remove(element)
            except ValueError:
                print('No Element Found with your match : ')
        elif value == 3:
            print()
            print(list)
        else:
            break
        
activity_one()