#!/usr/bin/python3
"""Module for FileStorage class."""
import datetime
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """Class for serialization and deserialization of base classes."""
    def __init__(self):
        """Initialize file path and objects dictionary."""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """Returns __objects dictionary."""
        return self.__objects

    def new(self, obj):
        """Sets new obj in __objects dictionary."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON file."""
        with open(self.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(d, f)

    def reload(self):
        """Deserializes JSON file into __objects."""
        if not os.path.isfile(self.__file_path):
            return
        with open(self.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: BaseModel(**v) for k, v in obj_dict.items()}
            self.__objects = obj_dict

    def attributes(self):
        """Returns the valid attributes and their types for classname."""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return attributes

