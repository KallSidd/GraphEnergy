from MonteCarlo import bitstring as bs
import pytest

bitstring = bs.BitString("011011")

def test_flip():
    testString = bitstring
    testString.flip(0)
    assert testString == "111011"

def test_set_string():
    testString = bitstring
    newString = bs.BitString("1010101")
    testString.set_string(newString)
    assert testString == "1010101"

def test_on():
    print(bitstring)
    assert bitstring.on() == 4

def test_off():
    assert bitstring.off() == 2

def test_int():
    assert bitstring.int() == 27

def test_set_int():
    testString = bitstring
    testString.set_int(14)
    assert bitstring == "1110"