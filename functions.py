
def greet():                  # def is used to define a function
    print("good morning")
    print("good evening")
    print("good afternoon")


greet()

def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d

result1,result2 = add_sub(5,4)
print(result1,result2)