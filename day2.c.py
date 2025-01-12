#Take a sentence input and print the number of vowels and consonants.
s=input("Enter any sentence: ")
v=["a","e","i","o","u"]
count_v=0
for i in s:
    if i in v:
        count_v+=1
print("Total letters in Sentence: ",s," is: ",len(s))
print("V:",count_v)
print("C:",len(s)-count_v)