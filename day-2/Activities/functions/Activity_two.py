# Functions
# Create a function to find the largest element in a list without using the max() function.

 

        
# Activity 2
def largest(max_list): 
    max_list.sort(reverse=True)
    print('Largest Number in list : ', max_list[0]) 
    
      
largest([1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 20])

