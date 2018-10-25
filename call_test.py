# File: callback_demo.py
# To demonstrate implementation and use of callbacks in Python, 
# using just plain functions.
# Author: Vasudev Ram
# Copyright 2017 Vasudev Ram
# Web site: https://vasudevram.github.io
# Blog: https://jugad2.blogspot.com
# Product store: https://gumroad.com/vasudevram

class Test(object):
    def __init__(self):
        self.callback_map = {}
    
    def call(self,path):
        if path in self.callback_map:
            func = self.callback_map[path]
            func()



    def watch(self,path,callback):
        self.callback_map[path] = callback
        callback()

    def callback_a(self):
        print("NO")


if __name__ == "__main__":
    path = "/a"
    obj = Test()
    obj.watch('/a',obj.callback_a)
    obj.call(path)
