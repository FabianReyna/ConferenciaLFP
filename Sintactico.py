class Sintactico:
    def __init__(self, tokens) -> None:
        self.listaTokens = tokens[::-1]
        self.resultados = []

    def analizar(self):
        self.INICIO()

    def INICIO(self):
        self.INSTRUCCIONES()

    def INSTRUCCIONES(self):
        self.INSTRUCCION()
        self.INSTRUCCIONES2()

    def INSTRUCCION(self):
        try:
            tmp = self.listaTokens[-1].tipo
            if tmp == "TKIMPRIMIR":
                self.listaTokens.pop()
                self.IMPRIMIR()
            # MAS INSTRUCCIONES
        except:
            pass

    def INSTRUCCIONES2(self):
        try:
            tmp = self.listaTokens[-1].tipo
            if tmp=="TKIMPRIMIR":
                self.INSTRUCCION()
                self.INSTRUCCIONES2()
                # MAS CASOS INSTRUCCION
        except:
            pass
    
    def IMPRIMIR(self):
        tmp = self.listaTokens[-1].tipo
        if tmp=="PAR1":
            self.listaTokens.pop()
            resultadoExpresion = self.EXPRESION()
            tmp = self.listaTokens[-1].tipo
            if tmp == "PAR2":
                self.listaTokens.pop()
                tmp = self.listaTokens[-1].tipo
                if tmp=="PUNTOCOMA":
                    self.listaTokens.pop()
                    self.resultados.append(resultadoExpresion)

    def EXPRESION(self):
        valor = self.TERMINO()
        return self.EXPRESION2(valor)

    def EXPRESION2(self, valor):
        tmp = self.listaTokens[-1].tipo
        if tmp in ["MAS", "MENOS"]:
            operador = self.listaTokens.pop().tipo
            termino = self.TERMINO()
            if operador == "MAS":
                valor += termino
            else:
                valor -= termino
            return self.EXPRESION2(valor)
        return valor
    
    def TERMINO(self):
        valor=self.FACTOR()
        return self.TERMINO2(valor)
    
    def TERMINO2(self,valor):
        tmp = self.listaTokens[-1].tipo
        if tmp in ["POR", "DIV"]:
            operador= self.listaTokens.pop().tipo
            factor = self.FACTOR()
            if operador=="POR":
                valor *= factor
            else:
                valor /= factor
            return self.TERMINO2(valor)
        return valor
    
    def FACTOR(self):
        tmp = self.listaTokens[-1].tipo
        if tmp == "PAR1":
            self.listaTokens.pop()
            valor = self.EXPRESION()
            tmp = self.listaTokens[-1].tipo
            if tmp == "PAR2":
                self.listaTokens.pop()
                return valor
        elif tmp == "NUMERO":
            aux = self.listaTokens.pop()
            return float(aux.lexema)
