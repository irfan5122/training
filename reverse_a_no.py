# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
rev = 0
while n>0:
    rev = rev * 10 + n % 10
    n = n // 10;

print(rev)
