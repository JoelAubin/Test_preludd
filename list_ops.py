import operator


def append(xs, ys):
    return xs+ys


def concat(lists):
    L = []
    for liste in lists:
        L = L + liste
        
    return L


def filter_clone(function, xs):
    
    L = []
    for element in xs:
        if function(element):
            L = L + [element]
    return L

def length(xs):
    c = 0
    for element in xs:
        c = c+1
    return c 
    
    

def map_clone(function, xs):
    
    L = []
    for element in xs:
        
        L = L + [function(element)]
    
    return L
    


def foldl(function, xs, acc):
    res = 0 
    if length(xs) == 0:
        return acc
    for element in xs:
        res = function(res,element)
    res = function(res,acc)
        
    return res
        
    

def foldr(function, xs, acc):
    xxs = reverse(xs)
    res = acc 
    if length(xxs) == 0:
        return acc
    for element in xxs:
        res = function(element,res)
    
    return res
    

def reverse(xs):
    L = []
    k = length(xs)
    for i in range(k):
        L = L + [xs[k - i -1]]
        
    return L
        
