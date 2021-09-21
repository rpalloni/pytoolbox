############## class attributes access control #############

''' single underscore: private variable but no interpreter block '''
class P:
   def __init__(self):
      self._x = 100
      self.y = 200

   def print(self):
      print(self._x, self.y)

class C(P):
   def __init__(self):
      super().__init__()
      self._x = 300
      self.y = 400
d = C()
d.print() # 300 400

''' double underscore: private variable and interpreter (fake) block '''
class P:
   def __init__(self):
      self.__x = 100
      self.y = 200

   def print(self):
      print(self.__x, self.y)

class C(P):
   def __init__(self):
      super().__init__()
      self.__x = 300
      self.y = 400
d = C()
d.print() # 100 400

''' double underscore workaround: name mangling '''
class P:
   def __init__(self):
      self.__x = 100
      self.y = 200

   def print(self):
      print(self.__x, self.y)

class C(P):
   def __init__(self):
      super().__init__()
      self._P__x = 300 # hacking access with name mangling: self._<classname>__attribute
      self.y = 400
d = C()
d.print() # 300 400
