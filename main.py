class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self, color):
        if color == "rojo" or color == "verde" or color == "negro" or color == "amarillo" or color == "blanco":
            self.color = color

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    
    def cambiarRegistro(self, registro):
        self.registro = registro
    
    def asignarTipo(self, tipo):
        if tipo == "electrico" or tipo == "gasolina":
            self.tipo = tipo

class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        Auto.cantidadCreados += 1

       
    
    def cantidadAsientos(self):
        x = 0
        for asientos in self.asientos:
            if asientos != None:
                x += 1
        return x


    
    def verificarIntegridad(self):
        if self.registro == self.motor.registro:
            for asiento in self.asientos:
                if asiento != None:
                    if asiento.registro != self.registro:
                        return "Las piezas no son originales"
            return "Auto original"
        
