#!/usr/bin/python3
"""
This is the base case that
is called by the modules
"""
import json
import csv


class Base:
    """
    This is a base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        this is the function check
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts list of dictionaries to a json
        serial format
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the json format of a list of
        objects to file
        """
        filename = cls.__name__
        my_list = []
        if list_objs is None or list_objs == []:
            my_list = []
        else:
            for cont in list_objs:
                my_list.append(cont.to_dictionary())
        buff = cls.to_json_string(my_list)
        with open(f"{filename}.json", "w") as container:
            container.write(buff)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns an object from a json representation
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates an instance of a class from
        its dictionary representation
        """
        name = cls.__name__
        if name == "Rectangle":
            rectangle = cls(1, 3)
            rectangle.update(**dictionary)
            return rectangle
        else:
            square = cls(3)
            square.updare(**dictionary)
            return square

    @classmethod
    def load_from_file(cls):
        """
        REturn a lisy of classes initiated from a
        file of JSON representation of Instances
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_items = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for count in list_items]
        except Exception:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Stores Rectangle or SQ object to CSV file
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csv_file:
            if list_objs is None or list_objs == []:
                csv_file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    chart = ["id", "width", "height", "x", "y"]
                else:
                    chart = ["id", "size", "x", "y"]
                csv_write = csv.Dictwriter(csv_file, chart=chart)
                for items in list_objs:
                    csv_writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        loads data from a csv file
        """
        result = []
        name = cls.__name__
        with open(f"{name}.csv", "r") as csv_file:
            csv_read = csv.reader(csv_file, delimeter=",")
            for row in csv_read:
                if name == "Square":
                    result.append(cls.create(id=int(row[0]), size=int(row[1]),
                        x=int(row[2]), y=int(row[3])))
                elif name == "Rectangle":
                    result.append(cls.create(id=int(row[0]), width=int(row[1]),
                        height=int(row[2]), x=int(row[3]), y=int(row[4])))
        return result
