# Custom Caesar Cipher:
#     Shifts each character in a string by a fixed number of positions in the alphabet (e.g., a Caesar cipher).
#     Accepts both the string and the shift value as inputs.
#     Example: Input: "abc", Shift: 2 → Output: "cde".


string=input('Enter string and shift value separated by space (eg. " abc 2 ") : ',)
string,shift=string.split()
resultant=''
for i in string:
    
    if (i.isupper()):
        resultant+= chr((ord(i)-65+ int(shift)) %26+65)
    else:
        resultant+= chr((ord(i)-97+ int(shift)) %26+97)
    
print(resultant)
