#!/usr/bin/python3
import sys

load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

with open(sys.stdin, "r") as f:
    save_to_json_file(f, "my_json.json")


with open("my_json.json", "a") as f:
    input_file = load_from_json_file(f)
    print(input_file)
    
