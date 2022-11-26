from unittest import TestCase

import pytest as pytest

from app import fooBarQix


@pytest.mark.parametrize("value,expected",
                         [(1, "1"),
                          (2, "2"),
                          (3, "FooFoo"),
                          (4, "4"),
                          (5, "BarBar"),
                          (6, "Foo"),
                          (7, "QixQix"),
                          (8, "8"),
                          (9, "Foo"),
                          (10, "Bar*"),
                          (13, "Foo"),
                          (15, "FooBarBar"),
                          (21, "FooQix"),
                          (33, "FooFooFoo"),
                          (51, "FooBar"),
                          (52, "Bar"),
                          (53, "BarFoo"),
                          (101, "1*1"),
                          (303, "FooFoo*Foo"),
                          (105, "FooBarQix*Bar"),
                          (10101, "FooQix**"),
                          (1004, "1**4"),
                          (1005, "FooBar**Bar"),
                          ])
def test_foo_bar_qix(value, expected):
    result = fooBarQix(value)
    assert result == expected

