from Token import Token
from Errores import Errores

class Lexico:
    def __init__(self) -> None:
       self.linea = 1
       self.columna = 1
       self.i = 0
       self.listaTokens = []
       self.listaErrores = []
       self.buffer = ""
       self.estado = 0

    def newToken(self,lexema, tipo, linea, col):
        self.listaTokens.append(Token(lexema, tipo, linea, col))
    
    def newError(self,tipo,descipcion):
        self.listaErrores.append(Errores(tipo,descipcion,self.linea,self.columna))
    
    # Estado inicial
    def estado0(self,caracter):
        if caracter == '+':
            self.newToken(caracter,"MAS",self.linea,self.columna)
            self.buffer = ""
            self.columna += 1
            return
    
        if caracter == '-':
            self.newToken(caracter,"MENOS",self.linea,self.columna)
            self.buffer = ""
            self.columna += 1
            return
        
        if caracter == '*':
            self.newToken(caracter,"POR",self.linea,self.columna)
            self.buffer = ""
            self.columna += 1
            return
        
        if caracter == '/':
            self.newToken(caracter,"DIV",self.linea,self.columna)
            self.buffer = ""
            self.columna += 1
            return
        
        if caracter == '(':
            self.newToken(caracter,"PAR1",self.linea,self.columna)
            self.buffer = ""
            self.columna += 1
            return
        
        if caracter == ')':
            self.newToken(caracter,"PAR2",self.linea,self.columna)
            self.buffer = ""
            self.columna += 1
            return
        
        if caracter == ';':
            self.newToken(caracter,"PUNTOCOMA",self.linea,self.columna)
            self.buffer = ""
            self.columna += 1
            return
        
        if caracter.isdigit():
            self.buffer = caracter
            self.columna += 1
            self.estado = 1
            return

        if caracter == '#':
            self.buffer = ''
            self.columna += 1
            self.estado = 3
            return
        
        if caracter.lower() == "i":
            self.buffer = caracter
            self.columna += 1
            self.estado = 2
            return
        
        if caracter == '\n':
            self.linea += 1
            self.columna = 1
            return
        
        if caracter == '\t':
            self.columna += 3
            return
        
        if caracter == ' ':
            self.columna += 1
            return
        
        if caracter == '\r':
            return
        
        self.buffer += caracter
        self.newError("LEXICO","Caracter invalido "+self.buffer)
        self.buffer = ""
        self.columna += 1
    
    # Estado de numeros
    def estado1(self,caracter):
        if caracter.isdigit():
            self.buffer += caracter
            self.columna += 1
            return
        
        self.newToken(self.buffer,"NUMERO",self.linea,self.columna)
        self.buffer = ""
        self.estado = 0
        self.i -= 1
    
    # Estado de palabra reservada imprimir
    def estado2(self, caracter):
        if caracter.isalpha():
            self.buffer += caracter
            self.columna += 1
            return
        
        if self.buffer.lower() == "imprimir":
            self.newToken(self.buffer,"TKIMPRIMIR",self.linea,self.columna)
            self.buffer = ""
            self.estado = 0
            self.i -= 1
            return
        
        else:
            self.newError("LEXICO","Palabra reservada invalida "+self.buffer)
            self.buffer = ""
            self.estado = 0
            self.i -= 1
            return
        
        self.buffer += caracter
        self.newError("LEXICO","Caracter invalido "+self.buffer)
        self.buffer = ""
        self.columna += 1
        self.estado = 0

    # estado de comentarios de una linea
    def estado3(self, caracter):
        if caracter == '\n':
            self.buffer = ""
            self.columna = 1
            self.estado = 0
            return
        
        self.buffer += caracter
        self.columna += 1
        return
    
    def analizar(self,entrada):
        self.listaTokens = list()
        self.listaErrores = list()
        self.linea = 1
        self.columna = 1
        self.buffer = ""
        self.estado = 0
        self.i = 0

        while self.i < len(entrada):
            caracter = entrada[self.i]
            if self.estado == 0:
                self.estado0(caracter)
            elif self.estado == 1:
                self.estado1(caracter)
            elif self.estado == 2:
                self.estado2(caracter)
            elif self.estado == 3:
                self.estado3(caracter)
            self.i += 1

        return self.listaTokens