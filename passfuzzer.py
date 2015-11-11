#!/usr/bin/env python2

from itertools import product as prod
import click

class Password():
    __d1337 = {
        "a": ["a", "A", "4"],
        "b": ["b", "B", "8"],
        "c": ["c", "C"],
        "d": ["d", "D"],
        "e": ["e", "E", "3"],
        "f": ["f", "F"],
        "g": ["g", "G", "9"],
        "h": ["h", "H"],
        "i": ["i", "I", "1"],
        "j": ["j", "J"],
        "k": ["k", "K"],
        "l": ["l", "L", "1"],
        "m": ["m", "M"],
        "n": ["n", "N"],
        "o": ["o", "O", "0"],
        "p": ["p", "P"],
        "q": ["q", "Q"],
        "r": ["r", "R"],
        "s": ["s", "S", "5"],
        "t": ["t", "T", "7"],
        "u": ["u", "U"],
        "v": ["v", "V"],
        "w": ["w", "W"],
        "x": ["x", "X"],
        "y": ["y", "Y"],
        "z": ["z", "Z"]
    }

    def diz(self, char):
        if char in self.__d1337.keys():
            return self.__d1337[char]
        else:
            return char

    def substitute(self, word, length):
        self.password = word
        self.length = length
        chars = map(self.diz, list(word))
        return map(\
                   ''.join,\
                   map(\
                       list,\
                       list(\
                            prod(*chars)\
                            )\
                       )\
                   )

    def echo(self):
        return self.substitute(self.password,self.length)

    def __init__(self, password):
        self.password = password
        self.length = len(password)

@click.command()
@click.argument('word')#\, metavar='<word>', help='word to be fuzzed')
@click.option('-p', '--stdprint', is_flag=True, help='prints the results to stdout')
@click.option('-o', '--outfile', type=click.Path(), default=None, help='file name where to save results')
def passfuzz(word, stdprint, outfile):
    '''
    small utility to produce a list of possible
    passwords from subsituting the chars of a given word with capital
    letters and numbers
    '''
    p = Password(word)
    if stdprint:
        for i in p.echo():
            print "{}".format(i)
    else:
        f = open(outfile,"a")
        for i in p.echo():
            f.write("{}\n".format(i))
        f.close()

if __name__=='__main__':
    passfuzz()
