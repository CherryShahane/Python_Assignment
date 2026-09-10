'''
 2. AI Auto-Correct Consecutive Word Remover

An AI-powered typing assistant often captures duplicate consecutive words while converting speech into text.

The company wants a Python program that removes only consecutive duplicate words while preserving the original sentence structure.

### Input:

text
hello hello hello team meeting meeting started


### Output:

text
hello team meeting started
'''
n=input("enter string")
word=n.split()
i=0
check=""
while i<len(word):
    j=0
    f=0
    while j<i:
        if word[i]==word[j]:
            f=1
            break
        j+=1
    if f==0:
        check=check+" "+word[i]

    i+=1
print(check)

