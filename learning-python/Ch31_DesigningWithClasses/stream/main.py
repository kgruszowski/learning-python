from upercase_processor import UppercaseProcessor
from odd_processor import OddProcessor
import sys


class HTMLizer():
    def write(self, line):
        print("<html><body>{}</body></html>".format(line))

if __name__ == "__main__":
    converter1 = UppercaseProcessor(open("testfile"), sys.stdout)
    converter1.process()

    print("")

    converter2 = OddProcessor(open("testfile"), sys.stdout)
    converter2.process()

    print("")

    converter3 = UppercaseProcessor(open("testfile"), HTMLizer())
    converter3.process()
