n1,n2,n3=map(int,input.split())
stack1=map(int,input().split())[::-1]
stack2=map(int,input().split())[::-1]
stack3=map(int,input().split())[::-1]

s1=sum(stack1)
s2=sum(stack2)
s3=sum(stack3)

while not(s1==s2 and s3==s1):
    if (s1>s2 or s1>s3):
        t=stack1.pop()
        s1-=t
        if (s2>s3 or s2>s1):
             t=stack2.pop()
             s2-=t
        if (s3 >s1 or s3>s2):
            t=stack1.pop()
            s3-=t

print(sum(stack1))
