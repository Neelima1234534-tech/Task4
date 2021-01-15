def foo():
   try:
      return 1
   finally:
      return 2
k = foo()
print(k)
# 2,The finally block is executed even there is a return statement in the try block
