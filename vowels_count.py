# Enter your code here. Read input from STDIN. Print output to STDOUT
vowels = ['a','e','i','o','u']
usr = input().lower()
count = 0
for i in usr:
    if i in vowels:
        count+=1
        
if count == 0:
    print("No vowels were found.")
else:
    print(f"Total number of vowels: {count}")
