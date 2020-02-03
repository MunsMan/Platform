from Objects import BaseObject
from Functions import JSONHandler

fjson = JSONHandler().create_object_model(BaseObject)
print(fjson)