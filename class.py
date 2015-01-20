class A:
 def __init__(self, name):
  print('hello A'+name)

class B(A):
 def __init__(self):
  super(B,self).__init__("called from B")
  print('hello B ')

class C(B):
 def print(self):
  super(C,self).__init__()
  print("it's me, C")

c = C()
print('-'*20)
 
