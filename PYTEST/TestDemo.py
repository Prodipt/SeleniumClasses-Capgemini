import pytest


# class Test_Demo:
#     def test_register(self):
#         print("Registering...")
#     def test_login(self):
#         print("Logging in...")
#     def test_logout(self):
#         print("Logging out...")

@pytest.mark.bhavik
def test_change():
    assert "hello" == "hello", 'Not Equal'
    assert  5==5, 'Not Equal'


# @pytest.mark.bhavik
def test_comparision():
    assert 45 >= 33 , "Not greater than"
    # assert 22 >= 33 , "Not greater than"

# @pytest.mark.bhavik
def test_membership():
    l = [1,2,3]
    assert  3 in l, 'Not in the list'
