#!/usr/bin/env python
# -*-coding:utf-8 -*-


class Dog(object):
    """一次模拟小狗的简单测试"""
    def __init__(self, name, age):
        """初始化对象的属性"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗草地打滚"""
        print(self.name.title() + " rolled over!")


if __name__ == '__main__':
    d = Dog("XH", 6)
    d.sit()
    d.roll_over()
