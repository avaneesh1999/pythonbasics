string=input("enter the string:")
substring=input("enter the substring:")
count=0
for i in range(0,len(string)):
    if string[i]==substring[0]:
        if string[i:i+len(substring)]==substring:
            count=count+1

print(count)