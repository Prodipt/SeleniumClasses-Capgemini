
# class Test_Demo:
#     def test_register(self):
#         print("Registering...")
#     def test_login(self):
#         print("Logging in...")
#     def test_logout(self):
#         print("Logging out...")


def test_paglu():
    assert "hello" == "helli", 'Not Equal'
    assert  5==5, 'Not Equal'

def test_comparision():
    assert 45 >= 33 , "Not greater than"
    assert 22 >= 33 , "Not greater than"

def test_membership():
    l = [1,2,3]
    assert  4 not in l , 'Not in the list'
    assert  4 in l, 'Not in the list'
