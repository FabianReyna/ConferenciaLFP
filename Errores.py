class Errores:
    def __init__(self, tipo, des, linea, col) -> None:
        self.tipo = tipo
        self.descripcion = des
        self.linea = linea
        self.col = col