import timeit
from numpy import mean

def get_timing(function, to_iterate, repeat=1):
    string = function.__name__ + ":\n"
    lib = {}
    for i in to_iterate:
        timing = timeit.timeit(lambda: function(i), number=repeat)
        lib[len(i)] = timing
        string += "List size: "+str(len(i))+" | "+"Time in sec: "+'{:f}'.format(timing)+"\n"
    return string, lib

def function_timing(function, repeat=1, **kwargs):
    return timeit.timeit(lambda: function(**kwargs), number=repeat)