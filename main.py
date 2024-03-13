#!/usr/bin/python3
"""Implementation of the various classes"""
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
print("=======================================")

my_model2 = BaseModel()
my_model2.name = "My_First_Model"
my_model2.my_number = 89
print(my_model2.id)
print(my_model2)
print(type(my_model2.created_at))
print("--")
my_model2_json = my_model2.to_dict()
print(my_model2_json)
print("JSON of my_model2:")
for key in my_model2_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model2_json[key]), my_model2_json[key]))
