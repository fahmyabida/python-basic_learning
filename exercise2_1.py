# install dill to get name of object
from dill.source import getname

# 1.a
class MyClass:
  str_var = ""
  int_var = 0
  bool_var = True
  # make constructor
  def __init__(self, str_var, int_var, bool_var):
    self.str_var = str_var;
    self.int_var = int_var;
    self.bool_var = bool_var;

  # 3 - preparation
  def check(self, bool, integer):
    if (self.int_var > integer & bool == self.bool_var):
      return True
    else:
      return False

# 1.b
obj_1 = MyClass("One", 1, True)
obj_2 = MyClass("Two", 2, True)
obj_3 = MyClass("Three", 3, True)
obj_4 = MyClass("Four", 4, True)
obj_5 = MyClass("Five", 5, True)
obj_6 = MyClass("Six", 6, True)
obj_7 = MyClass("Seven", 7, True)
obj_8 = MyClass("Eight", 8, True)
obj_9 = MyClass("Nine", 9, True)
obj_10 = MyClass("Ten", 10, True)
array_obj = [obj_1, obj_2, obj_3, obj_4, obj_5, obj_6, obj_7, obj_8, obj_9, obj_10]

# 2.a
comprehension = [ obj for obj in array_obj if obj.int_var % 2 == 1]
comprehension_check_only = [ obj.str_var for obj in array_obj if obj.int_var % 2 == 1]
print comprehension_check_only

# 3 finally
print (obj_5.check(True, 1)) # karena parameter bernilai 1 lebih kecil dari pd 5
print (obj_5.check(True, 6)) # karena parameter bernilai 1 lebih kecil dari pd 5



