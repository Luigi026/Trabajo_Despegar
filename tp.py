from math import prod
import time
from collections import Counter

class Sucursal:
    def __init__(self):
        self.productos = []

    def registrar_producto(self, nuevo_producto):
        self.productos.add(nuevo_producto)
        
    def recargar_stock(self,codigo_producto,cantidad_a_agregar):
        codigo_valido = False
        for producto in self.productos:
            if producto.codigo_valido(codigo_producto):
               codigo_valido = True
               producto.stock += cantidad_a_agregar
        if not codigo_valido:
            raise ValueError ("El codigo no corresponde a un producto registrado")
            
    def hay_stock(self, codigo_producto):
        for producto in self.productos:
            if codigo_producto == producto.codigo:
                return producto.stock > 0
        return False
    
    def calcular_precio_final(self, producto, es_extranjero):
        precio_final = 0
        if es_extranjero and producto.precio > 70:
            precio_final = producto.precio
            return precio_final
        else:
            precio_final = producto.precio+(21*producto.precio)/100
        return precio_final  

   
    def contar_categorias(self):
        lista_total_categorias = set()
        for producto in self.productos:
            for categoria in producto.categoria:
                lista_total_categorias.add(categoria)
        return len(lista_total_categorias)

    def realizar_compra(self,codigo_producto,cantidad_a_comprar,es_extranjero):
        codigo_valido = False
        for producto in self.productos:
            if producto.codigo_valido(codigo_producto):
               codigo_valido = True
               if producto.hay_stock_para_venta(cantidad_a_comprar):
                  producto.stock -= cantidad_a_comprar
                  monto_total = self.calcular_precio_final(producto, es_extranjero)*cantidad_a_comprar
                  self.ventas.append({"producto":producto.nombre,"cantidad_vendida":cantidad_a_comprar,"monto":monto_total,"fecha":time.strftime("%d/%m"),"anio":time.strftime("%Y")})
               else:
                  raise ValueError ("No hay suficiente stock para realizar la venta")      
        if not codigo_valido:
           raise ValueError ("El codigo no corresponde a un producto registrado")
              

    def descontinuar_productos(self):
        self.productos = {producto for producto in self.productos if producto.stock > 0}

    def valor_ventas_del_dia(self):
        venta_dia = 0
        if self.hay_ventas():
           for venta in self.ventas:
            if time.strftime("%d/%m") == venta["fecha"]:
               venta_dia += venta["monto"]
        else:
            raise ValueError ("No hay ventas registradas") 
        return venta_dia
    
    def ventas_del_anio(self):
        venta_anio = 0
        if self.hay_ventas(): 
           for venta in self.ventas:
               if time.strftime("%Y") == venta["anio"]:
                  venta_anio += venta["monto"]
        else:
            raise ValueError ("No hay ventas registradas")
        return venta_anio              

    def productos_mas_vendidos(self,cantidad_de_productos):
        productos_vendidos = []
        mas_vendidos = []
        for venta in self.ventas:
            productos_vendidos.append(venta["producto"])
        
        mas_vendidos = Counter(productos_vendidos)
        return mas_vendidos.most_common(cantidad_de_productos)
        

    def actualizar_precios_segun(self, criterio, porcentaje):
        for producto in self.productos:
            if criterio.corresponde_a(producto):
               producto.actualizar_precio_segun_porcentaje(porcentaje)
        

    def ganancia_diaria(self):
        if self.hay_ventas():
           return self.valor_ventas_del_dia() - self.gastos_del_dia()
        else:
            return self.gastos_del_dia()

    def hay_ventas(self):
        return len(self.ventas) > 0


    def listar_productos_segun(self,criterio):
        return {producto for producto in self.productos if criterio.corresponde_a(producto)}

         # Sucursales --- 

class SucursalFisica(Sucursal):
    def __init__(self):
        self.productos = set()
        self.ventas = []
        self.gasto_por_dia = 15000
    
    def gastos_del_dia(self):
        return self.gasto_por_dia
    
    
class SucursalVirtual(Sucursal):
    def __init__(self):
        self.productos = set()
        self.ventas = []
        self.gasto_por_dia = 1000
        self.gasto_variable = 1

    def gastos_del_dia(self):
        if len(self.ventas) > 100:
            return len(self.ventas)*self.gasto_variable
        else:
            return self.gasto_por_dia

    def modificar_gasto_variable(self,nuevo_valor):
        self.gasto_variable = nuevo_valor



class SucursalMarte(Sucursal):
    pass  

                   # Clase Prenda ---
   
class Prenda:
    def __init__(self,un_codigo,un_nombre,un_precio,categoria):
        self.codigo = un_codigo
        self.nombre = un_nombre
        self.precio = un_precio
        self.estado = Nueva()
        self.stock = 0
        self.categoria = set()
        self.categoria.add(categoria)
        
        
    def hay_stock(self):
       return self.stock > 0

    def hay_stock_para_venta(self,cantidad_a_vender):
        if self.stock >= cantidad_a_vender:
           self.stock -= cantidad_a_vender
           return True
        else:
           return False
       

    def codigo_valido(self,codigo):
       return codigo == self.codigo

    def ver_categorias(self):
        categorias = ",".join(self.categoria)
        return categorias
           
    def agregar_categoria(self,nueva_categoria):
       self.categoria.add(nueva_categoria)
    
    def cambiar_estado(self,nuevo_estado):
        self.estado = nuevo_estado

    def precio_final(self,precio):
        preci0_final = self.estado.precio_final(precio)
        return preci0_final

    def es_de_categoria(self, categoria):
        return categoria in self.categoria 
        

    def es_de_nombre(self, un_nombre): 
        return un_nombre == self.nombre 

    def actualizar_precio_segun_porcentaje(self, porcentaje):
        self.precio = self.precio + (self.precio * porcentaje)/100
    
 

                 # Estados de prendas ---

class Nueva:
    def precio_final(self,precio):
        return precio
    
class Promocion:
    def __init__(self, valor_descuento):
        self.valor = valor_descuento
        
    def precio_final(self, precio):
      return precio - self.valor
    
class Liquidacion:
    def precio_final(self, precio):
        return precio / 2               

                 # Segun criterios ---

class PorNombre:
    def __init__(self,u_nombre):
        self.nombre = u_nombre         
    
    def corresponde_a(self,producto):
        return producto.nombre == self.nombre

class PorPrecio:
    def __init__(self,u_precio):
        self.precio = u_precio

    def corresponde_a(self,producto):
        return producto.precio < self.precio   

class PorCategoria:
    def __init__(self, categoria):
        self.categoria = categoria

    def corresponde_a(self,producto):
        return producto.es_de_categoria(self.categoria)

class PorStock:
    def corresponde_a(self, producto):
        return producto.stock > 0

class PorOposicion:
    def __init__(self,criterio):
        self.criterio = criterio

    def corresponde_a(self, producto):
        return not self.criterio.corresponde_a(producto)
 

class PorCodigo:
    def __init__(self, u_codigo):
        self.codigo = u_codigo
        
    def corresponde_a(self,producto):
        return producto.codigo == self.codigo
        
    
        
    