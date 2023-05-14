#!/usr/bin/python3
'''
FileStorage - file storage
'''

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os.path


class FileStorage:
    '''FileStorage - file storage'''

    def __init__(self, path='file.json'):
        '''FileStorage - file storage'''
        self.__file_path = path
        self.__objects = {}

    def all(self):
        '''all - return all objects'''
        return self.__objects

    def new(self, obj):
        '''new - create new object'''
        id1 = getattr(obj, 'id')
        self.__objects[obj.__class__.__name__ + '.' + id1] = obj

    def save(self):
        '''save - save changes in object or new'''
        dict2 = {}
        for key, value in self.__objects.items():
            dict2[key] = value.to_dict()
        with open(self.__file_path, mode='w', encoding="utf-8") as f:
            f.write(json.dumps(dict2))

    def reload(self):
        '''reload - reload objects or new'''
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, encoding="utf-8", mode='r') as f:
                json_string = f.read()
                if json_string:
                    dict1 = json.loads(json_string)
                    for key, value in dict1.items():
                        cls_name = value['__class__']
                        obj = eval(cls_name + "(**value)")
                        self.__objects[key] = obj

