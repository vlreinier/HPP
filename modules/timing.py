import timeit
from numpy import mean

def get_timing(function, parameters, repeat=5):
    string = function.__name__ + ":\n"
    lib = {}
    for p in parameters:
        timing = timeit.timeit(lambda: function(p), number=repeat)
        lib[len(p)] = timing
        string += "List size: "+str(len(p))+" | "+"Time in sec: "+'{:f}'.format(timing)+"\n"
    return string, lib