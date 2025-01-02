# Write programs to:

# Count occurrences of each word in a string and store the results in a dictionary.

def activity_3():
    word = 'Hello how are you Hello '.lower()
    occurences = dict()
    for i in word.split():
        if occurences.get(i):  
            occurences[i] += 1
        else: 
            occurences[i] = 1 
            
      
    print('Activity 3 :')       
    print('Dictionary = ', end='')
    print(occurences)
    
activity_3()