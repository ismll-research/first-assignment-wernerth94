
import argparse
from unittest import TestCase

parser = argparse.ArgumentParser()
parser.add_argument("--number", type=str, required=True)

class TryTesting(TestCase):
    def test_always_passes(self):
        self.assertTrue(True)

    def test_always_fails(self):
        self.assertTrue(False)

if __name__ == '__main__':
    args = parser.parse_args()
    print("answer is")
    print(args.number)
