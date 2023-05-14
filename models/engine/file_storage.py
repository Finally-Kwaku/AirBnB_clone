#!/usr/bin/python3
"""Module for FileStorage class."""

from typing import Dict, Type
import datetime
import json
import os

from models.base_model import BaseModel


class FileStorage:
    """Class for serialization and deserialization of base classes."""

    __file_path: str = "file.json"
    __objects: Dict[str, BaseModel] = {}

    def all(self) -> Dict[str, BaseModel]:
        """Returns a dictionary of all objects in storage."""
        return self.__objects.copy()

    def new(self, obj: BaseModel) -> None:
        """Adds a new object to the storage."""
        key = f"{type(obj).__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self) -> None:
        """Serializes all objects in storage to JSON file."""
        with open(self.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(d, f)

    def classes(self) -> Dict[str, Type[BaseModel]]:
        """Returns a dictionary of all valid classes and their references."""
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        return {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
        }

    def reload(self) -> None:
        """Deserializes objects from JSON file into storage."""
        if not os.path.isfile(self.__file_path):
            return
        with open(self.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {
                k: self.classes()[v["__class__"]](**v)
                for k, v in obj_dict.items()
            }
            self.__objects = obj_dict

    def attributes(self) -> Dict[str, Dict[str, type]]:
        """Returns a dictionary of all valid attributes and their types for each class."""
        return {
            "BaseModel": {
                "id": str,
                "created_at": datetime.datetime,
                "updated_at": datetime.datetime,
            },
            "User": {
                "email": str,
                "password": str,
                "first_name": str,
                "last_name": str,
            },
            "State": {"name": str},
            "City": {"state_id": str, "name": str},
            "Amenity": {"name": str},
            "Place": {
                "city_id": str,
                "user_id": str,
                "name": str,
                "description": str,
                "number_rooms": int,
                "number_bathrooms": int,
                "max_guest": int,
                "price_by_night": int,
                "latitude": float,
                "longitude": float,
                "amenity_ids": list,
            },
            "Review": {
                "place_id": str,
                "user_id": str,
                "text": str,
            },
        }

