'''
4.  Instant Messaging Word Encryption System

A messaging application wants to temporarily encrypt messages during
transmission. The encryption rule is to reverse every word individually
while keeping the word positions unchanged.

Input: Enter message: java is powerful

Output: Encrypted Message: avaj si lufrewop


n=input('Enter message:')
l=n.split()
i=0
while i<len(l):
    words=l[i]
    rev=''
    j=len(words)-1
    while j>=0:
        rev=rev+words[j]
        j-=1
    print(rev,end=' ')
    i+=1
'''
n=input('Enter message:')
l=n.split()
for i in l:
    print(i[::-1],end=' ')