from MonteCarlo import bitstring as bs

def test_flip():
    bitstring = bs.BitString("011011")
    bitstring.flip(0)
    assert bitstring == "111011"

def test_set_string():
    bitstring = bs.BitString("011011")
    newString = "1010101"
    bitstring.set_string(newString)
    assert bitstring == "1010101"

def test_on():
    bitstring = bs.BitString("011011")
    assert bitstring.on() == 4

def test_off():
    bitstring = bs.BitString("011011")
    assert bitstring.off() == 2

def test_int():
    bitstring = bs.BitString("011011")
    assert bitstring.int() == 27

def test_set_int():
    bitstring = bs.BitString("011011")
    bitstring.set_int(14)
    assert bitstring == "1110"