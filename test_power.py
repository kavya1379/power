from power import power

def test_positive():
    assert power(2,2) == 4

def test_zero():
    assert power(2,0) == 1

def test_negative_exp():
    assert round(power(2,-2),3) == 0.25