# List Comprehensions:
# Write a program to:
# Generate a list of squares of all even numbers from 1 to 20 using a list comprehension.
# Create a nested list comprehension to generate a multiplication table (1 to 10).


even_list = [x**2 for x in range(1, 21) if x%2==0]
print("even squares list ", even_list)


table = [(x, i, x*i) for x in range(1, 11) for i in range(1, 11)]

print('↓ Table 1 to 10 ↓')

count=0
for j in table:   
    
    print(str(j),end=' ')
    count+=1
    if count%10==0 and count!=100:
        print(str(j))