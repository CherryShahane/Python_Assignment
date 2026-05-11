'''1.
Digit Frequency Balance Analyzer

A data security system analyzes numeric IDs to check digit distribution patterns.

For a given number, the system evaluates how frequently each digit appears.

Write a program to:

Count how many times each digit appears in the number
Display only the digits that appear more than once
Find the total count of repeated digits
Find the digit with maximum frequency
If no digit repeats, print Unique Number
If at least one digit repeats, print Repeated Pattern Detected

Use loops wherever required.

Input:
1223451

Output:
Repeated Digits: 1 2
Total Repeated Count = 4
Max Frequency Digit = 1
Repeated Pattern Detected
n=input ("enter no")
count=0
digit=0
for i in len(str(n)):
    digit =int(i)
    print(digit)'''

n = input("Enter number: ")

total_repeat = 0
max_freq = 0
max_digit = -1
flag = 0  # to check if any digit repeats

print("Repeated Digits:", end=" ")

# check digits from 0 to 9
for i in range(10):
    count = 0

    # count frequency of each digit
    for j in n:
        if int(j) == i:
            count += 1

    # check if repeated
    if count > 1:
        print(i, end=" ")
        total_repeat += count
        flag = 1

        # find max frequency digit
        if count > max_freq:
            max_freq = count
            max_digit = i

print()

# final outputs
if flag == 0:
    print("Unique Number")
else:
    print("Total Repeated Count =", total_repeat)
    print("Max Frequency Digit =", max_digit)
    print("Repeated Pattern Detected")



#Q2
'''2.
Digit Threshold Break Analyzer

A monitoring system analyzes numeric IDs to detect high-value digits. 
The system keeps adding digits one by one, but stops processing as soon as the running sum exceeds a given threshold.

Write a program to:

Accept a number and a threshold value
Traverse digits from right to left
Keep adding digits to a running sum
Display each digit added
The moment sum exceeds the threshold, stop using break
Display:
- Digits processed
- Final sum
- Count of digits processed
If threshold is never exceeded, print Threshold Not Reached

Use loops and break wherever required.

Input:
57294
Threshold = 10

Output:
Digits Processed: 4 9
Sum = 13
Count = 2
Threshold Exceeded

Input:
1234
Threshold = 15

Output:
Digits Processed: 4 3 2 1
Sum = 10
Count = 4
Threshold Not Reached'''
'''n,t=map(int,input("enter no").split())
sum=0
count=0
treshold=0
print("digits processed = ",end=" ")
while n>0:
    rem=n%10
    print(rem,end=" ")
    sum=sum+rem
    count += 1
    n=n//10
    if sum>t:
        treshold = 1
        break
print("sum=",sum)
print("count=",count)
if treshold==1:
    print("treshold exceeded")'''







