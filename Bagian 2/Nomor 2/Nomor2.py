def fibonaci (n) : 
    if n < 1:
        return[n]
    return fibonaci(n-1) + [n]
print(fibonaci[5])