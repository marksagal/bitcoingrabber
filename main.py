from modules.crack.random_brute import RandomBrute
import sys


def run():
    rb = RandomBrute()
    rb.console()
    # mydict = {'a': 'apple', 'b': 'ball'}
    # keys = ('a', 'b', 'c')
    # print((key in mydict for key in keys))

if __name__ == '__main__':
    sys.exit(run())