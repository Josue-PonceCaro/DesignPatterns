class Millas:
    def __init__(self):
        self.val4 = 0
      

	# Función para obtener el valor de _distancia

    def get(self):
        print('val3')
        return self.val4

	# Función para definir el valor de _distancia

	# distancia = property(obtener_distancia, definir_distancia, eliminar_distancia)
# Creamos un nuevo objeto 
avion = Millas()

# Indicamos la distancia
# avion.definir_distancia(200)
# avion.set = 4

print(avion.get)


# class Millas:
# 	def __init__(self):
# 		self._distancia = 0

# 	# Función para obtener el valor de _distancia
# 	# Usando el decorador property
# 	@property
# 	def obtener_distancia(self):
# 		print("Llamada al método getter")
# 		return self._distancia

# 	# Función para definir el valor de _distancia
# 	@obtener_distancia.setter
# 	def definir_distancia(self, valor):
# 		if valor < 0:
# 			raise ValueError("No es posible convertir distancias menores a 0.")
# 		print("Llamada al método setter")
# 		self._distancia = valor

# # Creamos un nuevo objeto 
# avion = Millas()

# # Indicamos la distancia
# avion.distancia = 200
