import random
def veletlen():
    lista = []
    for i in range(15):
        szamok = random.randrange(-90, 500)
        lista.append(szamok)
    return lista
def csillag(lista):
    print("II/A, B, C: ", end="\n\t")
    for i in range(len(lista)-1):
        print(lista[i], end="*")
    print(lista[-1])

def oszthatoak_szama (lista):
    tiz_o = 0
    for i in range(len(lista)):
        if lista[i] % 10 == 0:
            tiz_o += 1
    return tiz_o

def konzolra_ir(tiz_o):
    print(f"II/F:\n\tTízzel osztható számok száma: {tiz_o}")

def fajl_ir (tiz_o):
    f = open("kimutatas.txt ", "w", encoding="utf8")
    f.write(f"II/F:\n\tTízzel osztható számok száma: {tiz_o}")
    f.close()





