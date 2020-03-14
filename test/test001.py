import unittest
from unittest import TestCase


class Test666(unittest.TestCase):
    def test888(self):
       for i in range(10):
           print("我成功啦",i)


if __name__ == '__main__':
    hello=Test666()
    hello.test888()