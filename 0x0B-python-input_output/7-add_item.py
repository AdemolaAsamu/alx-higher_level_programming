#!/usr/bin/python3
"""
This modules executes and Adds
all argument to python list
"""
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def add_and_save_to_list():
   """"
   This is the function that adds and saces
   """
   try:
        load_data = load_from_json_file("add_item.json")
        size = len(sys.argv)
        for arg in range(1, size):
            load_data.append(sys.argv[arg])
        save_to_json_file(load_data, "add_item.json")
    except FileNotFoundError:
        with open("add_item.json", "w") as content:
            content.write("[]")
        load_data = load_from_json_file("add_item.json")
        buff = len(sys.argv)
        for arg in range(1, buff):
            load_data.append(sys.argv[arg])
        save_to_json_file(load_data, "add_item.json")


if __name__ == "__main__":
    add_and_save_to_list()
