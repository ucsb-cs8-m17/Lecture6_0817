import pytest
def areaTriangle(base,height):
    '''
    area of a triangle
    '''

    return (0.5) * base * height  # stub

def test_areaTriangle_1():
    assert areaTriangle(2,3) == 3

def kmToMiles(km):
    return km * 0.621371

def test_kmToMiles_1():
    assert kmToMiles(1.0)==pytest.approx(0.621371)

def test_kmToMiles_2():
    assert kmToMiles(100.7)==pytest.approx(62.572079)

