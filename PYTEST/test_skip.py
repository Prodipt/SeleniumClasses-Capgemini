import pytest

@pytest.mark.skip
def test_01():
    assert 'marvel' == 'marvel' , "Mismatch"
    print("Run 01")

@pytest.mark.skipif(5==5, reason = 'I am just not Happy with mam')
def test_02():
    assert 'marvel' == 'marvel' , "Mismatch"
    print("Run 02")


@pytest.mark.parametrize("a, b, result", [
    (2, 3, 5),
    (4, 5, 9),
    (1, 1, 2)
])
def test_add(a, b, result):
    assert a + b == result , " Addition Error"