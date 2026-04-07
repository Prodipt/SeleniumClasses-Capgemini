import pytest
#
# @pytest.fixture()
# def idk():
#     print("I actually don't know")
#     yield
#     print("Still Don't Know")
#
# def test_01(idk):
#     print("I have to type something")
#
# def test_02():
#     print("Here we didn't use that function")
#
@pytest.fixture(autouse=True)
def idk2():
    print("I actually don't know")
    yield
    print("Still Don't Know")

def test_03():
    print("I have to type something")

def test_04():
    print("Here we're using autouse")

