from discount import giamgia

def test_giamgia():
    assert giamgia(50000000, 0) == 0.1

def test_giamgia_2():
    assert giamgia(25000000, 25000000) == 0.1

def test_giamgia_3():
    assert giamgia(3000000,0) == 0

def test_giamgia_4():
    assert giamgia(0,3000000) == 0