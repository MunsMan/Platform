from Objects import BaseObject
from Functions import JSONHandler, SpecialPrint

fjson = JSONHandler().list_of_tree()
print(fjson)
P = SpecialPrint()
P.print_tree(fjson)
