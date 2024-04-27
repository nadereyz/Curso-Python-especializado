class Producto:
    def __init__(self, nombre, precio, stock): #    Inicio el producto con nombre, precio y stock.
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_informacion(self):
        print(f"Producto: {self.nombre}, Precio: {self.precio}, Stock: {self.stock}")    # Imprime la información del producto.

    def agregar_stock(self, cantidad):
        self.stock += cantidad #Añade stock al producto.

    def vender(self, cantidad):
        # aun no esta.