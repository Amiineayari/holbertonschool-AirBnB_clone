#!/usr/bin/python3
import models
import uuid
from datetime import datetime
"""Write a class BaseModel that defines all common attributes/methods
for other classes:"""


class BaseModel:
    """BseModel with the principal function to inherit"""
    def __init__(self, *args, **kwargs):
        """The constructor of base of the class BaseModel"""
        if kwargs:
            for keys, value in kwargs.items():
                if keys == "created_at" or keys == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if keys != "__class__":
                    self.__dict__[keys] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """saves a new version of class and updates the time of update"""
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """str a function to print the class"""
        txt = "[{}] ({}) {}"
        return txt.format(self.__class__.__name__, self.id, self.__dict__)

    def to_dict(self):
        """To_dict function to have a dictionary version of data"""
        instance_dict = self.__dict__.copy()
        instance_dict.update({"__class__": self.__class__.__name__})
        instance_dict.update({"created_at": self.created_at.isoformat()})
        instance_dict.update({"updated_at": self.updated_at.isoformat()})

        return instance_dict
