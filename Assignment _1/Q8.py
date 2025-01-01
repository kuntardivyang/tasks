# Extract Substrings:
# Accepts a string and two characters, start and end.
# Returns the substring between the first occurrence of start and the last occurrence of end.
# Example: Input: "abcdefg", start='b', end='f' → Output: "cde".


string=input('Enter A String ')

start=input('Enter Start Character ')
end=input('Enter End Character ')

start_index=string.find(start)
end_index=string.find(end)


print(string[start_index+1:end_index])