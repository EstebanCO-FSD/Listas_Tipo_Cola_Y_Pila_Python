class Persona:

    def __init__(self, codigo, nombre, telefono, edad):
        self.codigo = codigo
        self.nombre = nombre
        self.telefono = telefono
        self.edad = edad
    
    def obtenerDatos(self):
        datos = [self.codigo, self.nombre, self.telefono, self.edad]

        """
        datos = {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "telefono": self.telefono,
            "edad": self.edad
        }
        """

        return datos