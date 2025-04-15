import pytest
from yatzy import Yatzy

def test_ones():
    y = Yatzy()
    y.dice = [1, 1, 3, 4, 5]
    assert y.Ones() == 2

def test_one_pair():
    y = Yatzy()
    y.dice = [3, 3, 5, 5, 6]
    assert y.OnePair() == 10  # Max pair is 5*2=10

def test_full_house():
    y = Yatzy()
    y.dice = [2, 2, 3, 3, 3]
    assert y.FullHouse() == sum([2, 2, 3, 3, 3])

def test_yatzy():
    y = Yatzy()
    y.dice = [5, 5, 5, 5, 5]
    assert y.Yatzy() == 50

# Add tests for all other methods