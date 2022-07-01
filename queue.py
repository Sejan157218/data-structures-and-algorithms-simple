import re


num=[]

def enqueue(queue,n):
    queue.append(n)
    return queue;

def dequeue(queue):
    if isEmpty(queue):
        print('Empty queue')
        return False
    else:
      queue.pop(0)  
      return queue


def isEmpty(num):
    if not num:
        return True
    else:
        return False



enqueue(num,2)
enqueue(num,3)
enqueue(num,4)
enqueue(num,5)
print(num)
dequeue(num)
print(num)
dequeue(num)
print(num)
dequeue(num)
print(num)
dequeue(num)
dequeue(num)
dequeue(num)
dequeue(num)

print(num)


