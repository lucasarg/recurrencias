a = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13, 'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20, 'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26}

b = {'a': 5, 'c': 6, 'b': 2, 'e': 6, 'd': 4, 'g': 1, 'f': 6, 'i': 9, 'h': 3, 'k': 11, 'j': 10, 'm': 50, 'l': 12, 'o': 1, 'n': 900}

c = {}
#def repeticiones(a,b):
for i in a:
    if i in b:
        x = a[i]- b[i]
        c[i] = x
    
#print (c) habilitado
#{k: v for k, v in sorted(c.items(), key=lambda item: item[1])}
d = sorted(c.items(), key=lambda x: x[1], reverse=True)


print (d)








