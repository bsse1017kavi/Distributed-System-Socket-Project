#This is just for testing methods and has nothing to do with the project
import threading

def printit():
  threading.Timer(5.0, printit).start()
  print("Hello, World!")
  return 1

def two(a,b):
    sum = a+b
    sub = a-b

    return sum, sub
print('Hii')
printit()

# c = printit()
#
# print(c)


