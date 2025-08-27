from square import get_square

def test_sq():
    x = 3
    res = get_square(x)
    assert res == 9
    
def test_sq_neg():
    x = -4
    res = get_square(x)
    assert res == 16
    
def test_sq_zero():
    x = 0
    res = get_square(x)
    assert res == 0
    