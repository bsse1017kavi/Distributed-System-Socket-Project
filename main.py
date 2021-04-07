import threading

def printit():
  threading.Timer(5.0, printit).start()
  print("Hello, World!")
  return 1

def two(a,b):
    sum = a+b
    sub = a-b

    return sum, sub
# printit()

c = printit()

print(c)


