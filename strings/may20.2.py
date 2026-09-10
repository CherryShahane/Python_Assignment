'''
2. Reverse Sentence + Reverse Each Word

Secret Military Communication Decoder
A defense organization stores highly confidential messages in encrypted form.
To decode the message:

1. Reverse the entire sentence.
2. Reverse every individual word.
3. Store the final result back into the original string variable.

You must use the split() method.
Input:


Python is powerful


Output:


lufrewop si nohtyP

'''
n=input("Enter the sentence : ")
words=n.split()
i=len(words)-1
while i>=0:
    word=words[i]
    rev=""
    j=len(word)-1
    while j>=0:
        rev=rev+word[j]
        j=j-1
    print(rev,end=" ")
    i=i-1
