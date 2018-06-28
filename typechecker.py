''
Created on Jun 11, 2018

@author: Rich Katz
'''

from dataclasses import dataclass
import dataclasses

from builtins import str

# class Chair(object):
#     pass
# c = Chair()

class  Chair(object):

       def __init__(self, legsin):
               self.legs = legsin


c1 = Chair(3)
c2 = Chair(4)
print(c1.legs)



@dataclass
class type_checking(object):
    """ Provide validation for the type of each feild """

    def __post_init__(self):
        self.typecheck()

    def typecheck(self):
        dict = dataclasses.asdict(self)
        # print(dict)
        for f in dataclasses.fields(self):
            actual = dict[f.name]
            if not isinstance(actual, f.type):
                print ("Not valid ", f.type, " is not ", type(actual))
                return False
        return True


@dataclass
class PersonScore(type_checking):
    """ Person location and a number associated with them."""
    name: str
    value: int
    addr: str
    city: str


def recode(myinst: type_checking, format:str):
    flist = dataclasses.fields(myinst)
    if format == "D":
        # Django
        pass
    elif format == "Q":
        # SQL Alchemy
        pass
    elif format == "P":
        for f1 in flist:
            print (f1.name, f1.type)
    elif format == "A":
        # attrs
        pass


a = PersonScore("George", 1, "High Street", "St Paul")
b = PersonScore("Tom", 2, "Columbus Ave", "San Francisco")

recode(b, "P")

flist = dataclasses.fields(a)
# print(flist)

print(a)
print(b)

print(a.typecheck())

