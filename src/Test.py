#!/usr/bin/env python
# -*-coding:utf-8 -*-


def delRight():
    favorite_language = "Python "
    favorite_language = favorite_language.rstrip()
    print(favorite_language)


def greet_user(username):
    """显示HI"""
    print("你好," + username)


def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("-" + topping)


def build_profile(first, last, **user_info):
    """创建一个字典,其中包含我们知道的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


if __name__ == '__main__':
    # delRight()
    # greet_user("大佬")
    # make_pizza("i", "n", "k")
    user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
    print(user_profile)
