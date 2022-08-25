import sys


print(r'\begin{tabular}{|c|c|c|}')
print(r'\hline')
print(r'Caracter&ASCII&Binario\\')
print(r'\hline')
for i in range(1,len(sys.argv)):
    n = sys.argv[i]
    for c in n:
        a = ord(c)
        b = bin(a).replace("0b", "")
        line = c +  ' & ' + f'{a}'+ '&' f'{b}' + r'\\'
        print(line)
        print(r'\hline')
print(r'\end{tabular}')

