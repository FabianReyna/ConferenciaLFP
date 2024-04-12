from Lexico import Lexico
from Sintactico import Sintactico
def main():
    entrada = "imprimir(5+4);\nimprimir(2*8-1/1);\n#esto se ignora\nimprimir(1+10);"
    instanciaLexico = Lexico()
    tokens = instanciaLexico.analizar(entrada)

    instanciaSintactico =Sintactico(tokens)
    instanciaSintactico.analizar()
    resultados= instanciaSintactico.resultados

    for i in resultados:
        print(i)

if __name__ =="__main__":
    main()