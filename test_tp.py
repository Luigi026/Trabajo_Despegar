from tp import *
import pytest


              ###################################### TESTS ###################################################
              
def test_registrar_un_producto():
    reiniciar_listas(sucursal_retiro)
    sucursal_retiro.registrar_producto(remera_talle_s)
    assert len(sucursal_retiro.productos) == 1
    
def test_registrando_multiples_productos_4():
    sucursal_retiro.registrar_producto(zapatos_negros)
    sucursal_retiro.registrar_producto(gorra_blanca)
    sucursal_retiro.registrar_producto(remera_talle_s)
    sucursal_retiro.registrar_producto(jean_talle_40)
    assert len(sucursal_retiro.productos) == 4 
    
def test_recargar_stock():
    reiniciar_listas(sucursal_retiro)
    sucursal_retiro.registrar_producto(remera_talle_s)
    sucursal_retiro.recargar_stock(100, 500)
    assert sucursal_retiro.hay_stock(100)

def test_recargar_varios_productos_a_nuestro_stock():
    reiniciar_listas(sucursal_retiro)
    reiniciar_stock(remera_talle_s)
    sucursal_retiro.registrar_producto(remera_talle_s)
    sucursal_retiro.registrar_producto(jean_talle_40)
    sucursal_retiro.registrar_producto(gorra_blanca)
    sucursal_retiro.recargar_stock(100, 10)
    sucursal_retiro.recargar_stock(200, 200)
    sucursal_retiro.recargar_stock(300, 50)
    assert remera_talle_s.stock == 10
    assert jean_talle_40.stock == 200
    assert gorra_blanca.stock == 50

def test_hay_stock():
    reiniciar_listas(sucursal_retiro)
    sucursal_retiro.registrar_producto(remera_talle_s)
    sucursal_retiro.recargar_stock(100, 500)
    assert sucursal_retiro.hay_stock(100) == True
    
def test_demostraremos_que_si_no_recargamos_productos_nuestro_stock_estara_vacio():
    reiniciar_listas(sucursal_retiro)
    reiniciar_stock(jean_talle_40)
    reiniciar_stock(gorra_blanca)
    sucursal_retiro.registrar_producto(jean_talle_40)
    sucursal_retiro.registrar_producto(gorra_blanca)
    assert sucursal_retiro.hay_stock(200) == False
    assert sucursal_retiro.hay_stock(300) == False
    
def test_calcular_precio_final_con_cliente_extranjero():
    reiniciar_listas(sucursal_retiro)
    sucursal_retiro.registrar_producto(remera_talle_s)
    sucursal_retiro.recargar_stock(100, 500)
    assert sucursal_retiro.calcular_precio_final(remera_talle_s, True) == 1500
    
def test_calcular_precio_final_con_vendedor_local():
    reiniciar_listas(sucursal_retiro)
    sucursal_retiro.registrar_producto(remera_talle_s)
    sucursal_retiro.recargar_stock(100, 500)
    assert sucursal_retiro.calcular_precio_final(jean_talle_40, False) == 3630


def test_realizar_compra():
    reiniciar_listas(sucursal_retiro)
    sucursal_retiro.registrar_producto(remera_talle_s)
    sucursal_retiro.recargar_stock(100, 500)
    sucursal_retiro.realizar_compra(100,1, True)
    assert len(sucursal_retiro.ventas) == 1

def test_validara_cantidad_de_compras():
    productos_previamente_recargados_retiro()
    sucursal_retiro.realizar_compra(100, 27, True)
    sucursal_retiro.realizar_compra(200, 42, True)
    sucursal_retiro.realizar_compra(400, 21, True)
    sucursal_retiro.realizar_compra(300, 22, True)
    assert len(sucursal_retiro.ventas) == 4
    
def test_contar_por_categorias_con_tres_productos_de_distinta_categoria():
    reiniciar_listas(sucursal_retiro)
    sucursal_retiro.registrar_producto(remera_talle_s)
    sucursal_retiro.registrar_producto(jean_talle_40)
    sucursal_retiro.registrar_producto(gorra_blanca)
    assert sucursal_retiro.contar_categorias() == 3

def test_se_puede_dar_al_producto_una_categoria_inicial():
    reiniciar_listas(sucursal_retiro)
    reiniciar_listas(sucursal_air)
    assert remera_talle_s.categoria == {"remera"}
        
def test_vamos_a_buscar_productos_por_precio():
    reiniciar_listas(sucursal_retiro)
    sucursal_retiro.registrar_producto(remera_talle_s)
    sucursal_retiro.registrar_producto(jean_talle_40)
    assert remera_talle_s.precio == 1500
    assert jean_talle_40.precio == 3000

def test_descontinuar_jean_talle_40_sin_stock():
    reiniciar_listas(sucursal_retiro)
    sucursal_retiro.descontinuar_productos()
    assert len(sucursal_retiro.productos) == 0

def test_ventas_del_dia_con_productos_y_35_und_del_mismo():
    reiniciar_listas(sucursal_retiro)
    sucursal_retiro.registrar_producto(remera_talle_s)
    sucursal_retiro.registrar_producto(jean_talle_40)
    sucursal_retiro.recargar_stock(100, 500)
    sucursal_retiro.recargar_stock(200, 500)
    sucursal_retiro.realizar_compra(100, 35, True)
    assert sucursal_retiro.valor_ventas_del_dia() == 52500

def test_productos_que_mas_se_vendieron():
    reiniciar_listas(sucursal_retiro)
    sucursal_retiro.registrar_producto(remera_talle_s)
    sucursal_retiro.registrar_producto(jean_talle_40)
    sucursal_retiro.registrar_producto(gorra_blanca)
    sucursal_retiro.recargar_stock(100, 200)
    sucursal_retiro.recargar_stock(200, 400)
    sucursal_retiro.recargar_stock(300, 600)
    sucursal_retiro.realizar_compra(100, 30, True)
    sucursal_retiro.realizar_compra(200, 20, True)
    sucursal_retiro.realizar_compra(200, 20, True)
    assert len(sucursal_retiro.productos_mas_vendidos(2)) == 2

def test_ventas_del_dia_con_dos_productos_de_diferentes_cetegorias():
    reiniciar_listas(sucursal_retiro)
    reiniciar_stock(Prenda)
    sucursal_retiro.registrar_producto(remera_talle_s)
    sucursal_retiro.registrar_producto(jean_talle_40)
    sucursal_retiro.recargar_stock(100, 500)
    sucursal_retiro.recargar_stock(200, 500)
    sucursal_retiro.realizar_compra(100, 30, True)
    sucursal_retiro.realizar_compra(200, 20, False)
    assert sucursal_retiro.valor_ventas_del_dia() == 117600

def test_ventas_del_anio(): 
    reiniciar_listas(sucursal_retiro)
    sucursal_retiro.registrar_producto(remera_talle_s)
    sucursal_retiro.registrar_producto(jean_talle_40)
    sucursal_retiro.registrar_producto(gorra_blanca)
    sucursal_retiro.recargar_stock(100, 200)
    sucursal_retiro.recargar_stock(200, 400)
    sucursal_retiro.recargar_stock(300, 600)
    sucursal_retiro.realizar_compra(100, 30, True)
    sucursal_retiro.realizar_compra(200, 20, True)
    sucursal_retiro.realizar_compra(300, 10, False)
    assert sucursal_retiro.ventas_del_anio() == 159450
    
def test_solo_me_sumara_las_ventas_que_sean_del_anio():
    reiniciar_listas(sucursal_retiro)
    sucursal_retiro.registrar_producto(remera_talle_s)
    sucursal_retiro.registrar_producto(jean_talle_40)
    sucursal_retiro.registrar_producto(gorra_blanca)
    sucursal_retiro.recargar_stock(100, 200)
    sucursal_retiro.recargar_stock(200, 400)
    sucursal_retiro.recargar_stock(300, 600)
    sucursal_retiro.realizar_compra(100, 30, True)
    sucursal_retiro.realizar_compra(200, 20, True)
    sucursal_retiro.ventas.append({"producto":"celular", "monto":25000, "anio":2020})
    assert sucursal_retiro.ventas_del_anio() == 105000

def test_de_ganancia_sucursal_con_parametros_de_la_fisica():
    reiniciar_listas(sucursal_retiro)
    reiniciar_stock(Prenda)
    sucursal_retiro.registrar_producto(remera_talle_s)
    sucursal_retiro.registrar_producto(jean_talle_40)
    sucursal_retiro.registrar_producto(gorra_blanca)
    sucursal_retiro.recargar_stock(100, 200)
    sucursal_retiro.recargar_stock(200, 400)
    sucursal_retiro.recargar_stock(300, 600)
    sucursal_retiro.realizar_compra(100, 30, True)
    sucursal_retiro.realizar_compra(200, 20, True)
    assert sucursal_retiro.ganancia_diaria() == 90000

def test_de_ganancia_sucursal_con_parametros_de_la_virtual():
    reiniciar_listas(sucursal_air)
    reiniciar_stock(Prenda)
    sucursal_air.registrar_producto(remera_talle_s)
    sucursal_air.registrar_producto(jean_talle_40)
    sucursal_air.registrar_producto(gorra_blanca)
    sucursal_air.recargar_stock(100, 200)
    sucursal_air.recargar_stock(200, 400)
    sucursal_air.recargar_stock(300, 600)
    sucursal_air.modificar_gasto_variable(1000)
    sucursal_air.realizar_compra(100, 10, True)
    sucursal_air.realizar_compra(200, 20, True)
    assert sucursal_air.ganancia_diaria() == 74000

def test_actualizaremos_precios_por_categorias():
    reiniciar_listas(sucursal_retiro)
    reiniciar_stock(Prenda)
    sucursal_retiro.registrar_producto(jean_talle_40)
    sucursal_retiro.actualizar_precios_segun(PorCategoria("jean"), 50)
    assert jean_talle_40.precio == 4500

def test_actualizaremos_precios_por_categorias_solo_a_la_que_corresponda():
    productos_previamente_recargados_retiro()
    sucursal_retiro.actualizar_precios_segun(PorCategoria("zapatos"), 100)
    assert zapatos_negros.precio == 10000
    assert remera_talle_s.precio == 1500
    assert jean_talle_40.precio == 3000

def test_actualizaremos_precio_segun_stock():
    reiniciar_listas(sucursal_retiro)
    reiniciar_stock(Prenda)
    sucursal_retiro.registrar_producto(gorra_blanca)
    sucursal_retiro.registrar_producto(remera_talle_s)
    sucursal_retiro.recargar_stock(100, 200)
    sucursal_retiro.recargar_stock(300, 600)
    sucursal_retiro.actualizar_precios_segun(PorStock(),100)
    assert gorra_blanca.precio == 9000
    assert remera_talle_s.precio == 3000

def test_actualizaremos_precios_segun_su_nombre():
    reiniciar_listas(sucursal_retiro)
    reiniciar_stock(Prenda)
    reinicio_el_precio_de_las_prendas()
    sucursal_retiro.registrar_producto(gorra_blanca)
    sucursal_retiro.recargar_stock(300, 600)
    sucursal_retiro.actualizar_precios_segun(PorNombre("gorra_blanca"),50)
    assert gorra_blanca.precio == 6750

def test_actualizaremos_precios_segun_su_precio():
    reiniciar_listas(sucursal_retiro)
    reiniciar_stock(Prenda)
    reinicio_el_precio_de_las_prendas()
    sucursal_retiro.registrar_producto(gorra_blanca)
    sucursal_retiro.registrar_producto(remera_talle_s)
    sucursal_retiro.recargar_stock(100, 200)
    sucursal_retiro.recargar_stock(300, 600)
    sucursal_retiro.actualizar_precios_segun(PorPrecio(4800), 200)
    assert remera_talle_s.precio == 4500
    assert gorra_blanca.precio == 13500


def test_actualizaremos_precio_solo_a_los_que_cumplan_con_nuestro_criterio_por_precio():
    productos_previamente_recargados_retiro()
    sucursal_retiro.actualizar_precios_segun(PorPrecio(2000), 100)
    assert remera_talle_s.precio == 3000
    assert jean_talle_40.precio == 3000
    assert zapatos_negros.precio == 5000
    assert gorra_blanca.precio == 4500

def test_actualizaremos_precio_utilizando_nuestro_criterio_por_oposicion_nombre():
    reiniciar_listas(sucursal_retiro)
    reiniciar_stock(Prenda)
    reinicio_el_precio_de_las_prendas()
    sucursal_retiro.registrar_producto(remera_talle_s)
    sucursal_retiro.recargar_stock(100, 200)
    sucursal_retiro.actualizar_precios_segun(PorOposicion(PorNombre("gorra_blanca")), 200)
    assert remera_talle_s.precio == 4500
    
def test_utilizaremos_el_criterio_por_oposicion_categoria_para_actualizar_precio():
    productos_previamente_recargados_retiro()
    sucursal_retiro.actualizar_precios_segun(PorOposicion(PorCategoria("jean")), 100)
    assert zapatos_negros.precio == 10000

def test_actualizaremos_precio_utilizando_nuestro_criterio_por_oposicion_categoria():
    productos_previamente_recargados_retiro()
    sucursal_retiro.actualizar_precios_segun(PorOposicion(PorCategoria("zapatos")), 100)
    assert zapatos_negros.precio == 5000

def test_actualizaremos_precio_porque_aplicamos_nuestro_criterio_por_oposicion_por_stock():
    reiniciar_listas(sucursal_retiro)
    reiniciar_stock(gorra_blanca)
    reiniciar_stock(remera_talle_s)
    reinicio_el_precio_de_las_prendas()
    sucursal_retiro.registrar_producto(gorra_blanca)
    sucursal_retiro.registrar_producto(remera_talle_s)
    sucursal_retiro.actualizar_precios_segun(PorOposicion(PorStock()), 100)
    assert gorra_blanca.precio == 9000
    assert remera_talle_s.precio == 3000

def test_no_actualizaremos_precio_porque_no_aplicamos_nuestro_criterio_por_oposicion_por_stock():
    reiniciar_listas(sucursal_retiro)
    reiniciar_stock(Prenda)
    reinicio_el_precio_de_las_prendas()
    sucursal_retiro.registrar_producto(gorra_blanca)
    sucursal_retiro.registrar_producto(remera_talle_s)
    sucursal_retiro.recargar_stock(100, 50)
    sucursal_retiro.recargar_stock(300, 100)
    sucursal_retiro.actualizar_precios_segun(PorOposicion(PorStock()), 100)
    assert gorra_blanca.precio == 4500
    assert remera_talle_s.precio == 1500
   
def test_demostraremos_que_no_se_actualza_nada_que_no_cumpla_con_nuestro_criterio_por_oposicion_por_precio():
    productos_previamente_recargados_retiro()
    sucursal_retiro.actualizar_precios_segun(PorOposicion(PorPrecio(10000)), 50)
    assert zapatos_negros.precio == 5000
    assert gorra_blanca.precio == 4500
    assert remera_talle_s.precio == 1500
    assert jean_talle_40.precio == 3000

def test_actualizaremos_todos_los_precios_basado_en_nuestro_criterio_por_oposicion_por_precio():
    productos_previamente_recargados_retiro()
    sucursal_retiro.actualizar_precios_segun(PorOposicion(PorPrecio(100)), 50)
    assert zapatos_negros.precio == 7500
    assert gorra_blanca.precio == 6750
    assert remera_talle_s.precio == 2250
    assert jean_talle_40.precio == 4500



# TODO hacer la tarea programada de discontinuar productos.  


######################################## Mini base de datos ###########################################

sucursal_retiro = SucursalFisica()
remera_talle_s = Prenda(100,"remera talle s",1500,"remera")
jean_talle_40 = Prenda(200, "jean_talle_40", 3000, "jean")
zapatos_negros = Prenda(400, "zapatos_negros", 5000, "zapatos")
gorra_blanca = Prenda(300, "gorra_blanca", 4500, "gorra")

sucursal_air = SucursalVirtual()
remera_talle_s = Prenda(100,"remera talle s",1500,"remera")
jean_talle_40 = Prenda(200, "jean_talle_40", 3000, "jean")
gorra_blanca = Prenda(300, "gorra_blanca", 4500, "gorra")
zapatos_negros = Prenda(400, "zapatos_negros", 5000, "zapatos")

def reiniciar_listas(sucursal):
    sucursal.productos.clear()
    sucursal.ventas.clear()

def reiniciar_stock(prenda):
    prenda.stock = 0

def reinicio_el_precio_de_las_prendas():
    remera_talle_s.precio = 1500
    jean_talle_40.precio = 3000
    gorra_blanca.precio = 4500
    zapatos_negros.precio = 5000

def productos_previamente_recargados_retiro():
    reiniciar_listas(sucursal_retiro)
    reiniciar_stock(Prenda)
    reinicio_el_precio_de_las_prendas()
    sucursal_retiro.registrar_producto(zapatos_negros)
    sucursal_retiro.registrar_producto(gorra_blanca)
    sucursal_retiro.registrar_producto(remera_talle_s)
    sucursal_retiro.registrar_producto(jean_talle_40)
    sucursal_retiro.recargar_stock(400, 100)
    sucursal_retiro.recargar_stock(100, 200)
    sucursal_retiro.recargar_stock(300, 600)
    sucursal_retiro.recargar_stock(200, 300)

def productos_previamente_recargados_air():
    reiniciar_listas(sucursal_air)
    reiniciar_stock(Prenda)
    reinicio_el_precio_de_las_prendas()
    sucursal_air.registrar_producto(zapatos_negros)
    sucursal_air.registrar_producto(gorra_blanca)
    sucursal_air.registrar_producto(remera_talle_s)
    sucursal_air.registrar_producto(jean_talle_40)
    sucursal_air.recargar_stock(400, 100)
    sucursal_air.recargar_stock(100, 200)
    sucursal_air.recargar_stock(300, 600)
    sucursal_air.recargar_stock(200, 300)