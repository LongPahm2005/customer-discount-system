from discount import giamgia

def test_giamgia():
    assert giamgia(60000000, 2000000) == 0.1

def test_giamgia_2():
    assert giamgia(30000000, 2000000) == 0

def test_giamgia_3():
    assert giamgia(49000000,2000000) == 0.1