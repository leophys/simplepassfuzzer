Simple Pass Fuzzer
==================


It is nothing more than a joke. An incredibly small python tool
based on itertools that can "fuzz" a given word with all the corresponding
variations based on an internal dictionary (work in progress).


Usage
-----

```
Usage: passfuzzer.py [OPTIONS] WORD

  small utility to produce a list of possible passwords from subsituting the
  chars of a given word with capital letters and numbers

Options:
  -p, --stdprint      prints the results to stdout
  -o, --outfile PATH  file name where to save results
  --help              Show this message and exit.
```

LICENCE
-------


This work is licenced under the terms of the [WTFPL](https://en.wikipedia.org/wiki/WTFPL) license.


Credits
-------

Produced at [Quantum Leap](http://www.quantumleap.it/), R&D dept.
