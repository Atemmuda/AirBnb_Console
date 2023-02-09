#!/usr/bin/python3
"""Fles storage engine for the objects"""

import json
from os import path


class FileStorage():
    """Class for storing object in a json file format"""
    __file_path = ""
    __objects = {}

    def all(self):
        """returns all the dictionary object"""
        return self.__objects
    
    def new(self, obj):
        """sets in the object with key the obj with the key <obj class name>.id"""
        self.__objects["__class__.__name__.id"] = obj

    def save(self):
        """serializes object to the JSON file"""
    
    def reload(self):
        """deserialze the JSON file to __objects if file exists"""
        