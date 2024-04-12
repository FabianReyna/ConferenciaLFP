class Token:
    def __init__(self, lexema, tipo, linea, col):
        self.lexema = lexema
        self.tipo = tipo
        self.linea = linea
        self.col = col
    
    def __str__(self) -> str:
        return f"Lexema: {self.lexema} Tipo: {self.tipo} Linea: {self.linea} Columna: {self.col}"