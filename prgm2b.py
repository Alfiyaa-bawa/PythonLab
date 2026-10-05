#square of n numbers 2b
list1=[1,2,3,4,5,6]
list2=[i**2 for i in list1]
print(f"{list2}")



#2c
word=input("Enter a string:")
listVowel=[i for i in word if i in 'aeiouAEIOU']
print(f"vowels are {listVowel}")


#2d
w=input("Enter any string:")
OrdinalVal=[ord(i) for i in w ]
print(OrdinalVal)
