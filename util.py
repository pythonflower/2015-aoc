import re
import functools
import collections
import time

#### FILE INPUT AND PARSING

def Input(day, line_parser=str.strip, file_template='data/{:02d}.txt'):
    "For this day's input file, return a tuple of each line parsed by `line_parser`."
    return mapt(line_parser, open(file_template.format(day)))

def tInput(day, line_parser=str.strip, file_template='test/{}.txt'):
    return Input(day, line_parser, file_template)

def words(text): 
    "A tuple of all letters in a string (ignore other characters)."
    return mapt(str, re.findall(r'\w+', text))

def integers(text): 
    "A tuple of all integers in a string (ignore other characters)."
    return mapt(int, re.findall(r'-?\d+', text))

#### UTILITY FUNCTIONS

def mapt(fn, *args): 
    "Do a map, and make the results into a tuple."
    return tuple(map(fn, *args))

def compose(*functions):
    return functools.reduce(lambda f, g: lambda x: f(g(x)), functions)

def multimapset(items):
    "Given (key, val) pairs, return {key: [val, ....], ...}."
    result = collections.defaultdict(set)
    for (key, val) in items:
        result[key].add(val)
    return result

def multimap(items):
    "Given (key, val) pairs, return {key: [val, ....], ...}."
    result = collections.defaultdict(list)
    for (key, val) in items:
        result[key].append(val)
    return result


Point = complex
def X(p): return p.real
def Y(p): return p.imag

def neighbors8(p): 
    "The eight neighboring squares."
    P = Point
    return (p + n for n in (P(-1, -1), P(0, -1), P(+1, -1),
                            P(-1,  0),           P(+1,  0),
                            P(-1, +1), P(0, +1), P(+1, +1)))

def timedfunc(f, args):
	x = time.time()
	answer = f(*args)
	y = time.time()
	return y-x, answer
	
cat = "".join
