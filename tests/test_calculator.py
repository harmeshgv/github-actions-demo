from app.calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 4) == 6

def test_subtract():
    assert subtract(4, 2) == 2

def test_multiply():
    assert multiply(3, 6) == 18
    
def test_divide():
    assert divide(4,2) == 2
