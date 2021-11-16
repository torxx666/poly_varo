
from dataclasses import dataclass, field
from typing import Optional, List


@dataclass
class Person:
    age:Optional[int] =1
    def __init__(self,value=None) -> None:
        self.age = value

    def __str__(self) -> str:
        return f"{self.age}"



@dataclass
class MagicList():
    
    cls_type: Optional[Person] = None
    internal_list: List = field(default_factory=[])

    def __init__(self, cls_type: type= None):
        # if cls_type is  None:
        self.internal_list = []
        self.cls_type = cls_type

    
    def __str__(self):
        return f"{self.internal_list}"

    def __getitem__(self, key):
        if isinstance(self.cls_type,type):
            if key not in self.internal_list:
                self.internal_list.append(self.cls_type())
            return self.internal_list[key]
        else:
            return getattr(self, key)

        

    def __setitem__(self, key, newvalue):

        if self.cls_type:
            self.internal_list.append(self.cls_type(newvalue))
        else:
            self.internal_list.append(newvalue)

    def __repr__(self) -> str:
        return 

    
a = MagicList()
a[0] = 5
print(a)



b = MagicList(cls_type=Person)

b[0].age = 52
print(b)

assert a.__str__()=='[5]'
assert b[0].__str__()=='52'
