def push(num,n):
    num.append(n)
    return num

def Pop(num):
    if isEmpty(num):
        print('stack is empty')
    else:
        num.pop()
        return num

def isEmpty(num):
    if not num:
        return True
    else:
        return False
num=[]
push(num,2)
push(num,3)
push(num,4)
push(num,5)
Pop(num)
Pop(num)
Pop(num)
Pop(num)
Pop(num)
print(num)