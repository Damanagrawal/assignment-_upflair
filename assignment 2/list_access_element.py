#Given the list fruits = ['apple', 'banana', 'cherry', 'date'], how would you 
#access the “na” from the ‘banana’? after that change it in upper case like “NA”

fruits = ['apple', 'banana', 'cherry', 'date']
print(fruits[1][4:].upper())

#alternate
# ans = fruits[1].upper()
# print(ans[4:])