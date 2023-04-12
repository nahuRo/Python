from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox


operador = ''
precios_comida = [1250, 1450, 1650, 1850, 2050, 2250, 2450, 2650]
precios_postres = [1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600]
precios_bebidas = [1050, 950, 850, 750, 650, 1150, 1250, 1350]

def click_btn_cal(num):
    global operador
    operador = operador + num
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)

def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0, END)

def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ''

def revisar_check():
    x = 0
    for c in cuadro_comidas:
        if var_comidas[x].get() == 1:
            cuadro_comidas[x].config(state=NORMAL)
            if cuadro_comidas[x].get() == '0':
                cuadro_comidas[x].delete(0, END)
            cuadro_comidas[x].focus()
        else:
            cuadro_comidas[x].config(state=DISABLED)
            texto_comidas[x].set('0')
        x += 1

    x = 0
    for c in cuadro_bebidas:
        if var_bebidas[x].get() == 1:
            cuadro_bebidas[x].config(state=NORMAL)
            if cuadro_bebidas[x].get() == '0':
                cuadro_bebidas[x].delete(0, END)
            cuadro_bebidas[x].focus()
        else:
            cuadro_bebidas[x].config(state=DISABLED)
            texto_bebidas[x].set('0')
        x += 1

    x = 0
    for c in cuadro_postres:
        if var_postres[x].get() == 1:
            cuadro_postres[x].config(state=NORMAL)
            if cuadro_postres[x].get() == '0':
                cuadro_postres[x].delete(0, END)
            cuadro_postres[x].focus()
        else:
            cuadro_postres[x].config(state=DISABLED)
            texto_postres[x].set('0')
        x += 1

def get_total():
    sub_total_comida = 0 
    p = 0
    for cantidad in texto_comidas:
        sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[p])
        p += 1

    sub_total_bebidas = 0 
    p = 0
    for cantidad in texto_bebidas:
        sub_total_bebidas = sub_total_bebidas + (float(cantidad.get()) * precios_bebidas[p])
        p += 1

    sub_total_postres = 0 
    p = 0
    for cantidad in texto_postres:
        sub_total_postres = sub_total_postres + (float(cantidad.get()) * precios_postres[p])
        p += 1

    sub_total = sub_total_comida + sub_total_bebidas + sub_total_postres
    impuestos = sub_total * 0.07
    total = sub_total + impuestos

    var_costo_comida.set(f'$ {round(sub_total_comida, 2)}')
    var_costo_bebida.set(f'$ {round(sub_total_bebidas, 2)}')
    var_costo_postre.set(f'$ {round(sub_total_postres, 2)}')
    var_subtotal.set(f'$ {round(sub_total)}')
    var_impuesto.set(f'$ {round(impuestos)}')
    var_total.set(f'$ {round(total)}')

def get_recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f'N# - {random.randint(1000,9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'Datos:\t{num_recibo}\t\t{fecha_recibo}\n')
    texto_recibo.insert(END, f'*' * 47 + '\n')
    texto_recibo.insert(END, 'Items\t\tCant.\tCostoItems\n')
    texto_recibo.insert(END, f'-' * 54 + '\n')

    x = 0
    for comida in texto_comidas:
        if comida.get() != '0':
            texto_recibo.insert(END, f'{lista_comidas[x]}\t\t{comida.get()}\t{int(comida.get()) * precios_comida[x]}\n')
        x += 1

    x = 0
    for bebida in texto_bebidas:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{lista_bebidas[x]}\t\t{bebida.get()}\t{int(bebida.get()) * precios_bebidas[x]}\n')
        x += 1

    x = 0
    for postre in texto_postres:
        if postre.get() != '0':
            texto_recibo.insert(END, f'{lista_postres[x]}\t\t{postre.get()}\t{int(postre.get()) * precios_postres[x]}\n')
        x += 1
    
    texto_recibo.insert(END, f'-' * 54 + '\n')
    texto_recibo.insert(END, f'Costo de la Comida: \t\t\t {var_costo_comida.get()}\n')
    texto_recibo.insert(END, f'Costo de la Bebida: \t\t\t {var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f'Costo de los Postres: \t\t\t {var_costo_postre.get()}\n')
    texto_recibo.insert(END, f'-' * 54 + '\n')
    texto_recibo.insert(END, f'Sub-total: \t\t\t {var_subtotal.get()}\n')
    texto_recibo.insert(END, f'Impuestos: \t\t\t {var_impuesto.get()}\n')
    texto_recibo.insert(END, f'Total: \t\t\t {var_total.get()}\n')
    texto_recibo.insert(END, f'-' * 54 + '\n')
    texto_recibo.insert(END, 'Lo esperamos pronto')

def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Informacion','Su recibo ha sido guardado')

def resetear():
    texto_recibo.delete(0.1, END)
    # borro la cantidad en el input de cada producto
    for texto in texto_comidas:
        texto.set('0')
    for texto in texto_bebidas:
        texto.set('0')
    for texto in texto_postres:
        texto.set('0')

    # quito el focus de los checkbox
    for cuadro in cuadro_comidas:
        cuadro.config(state=DISABLED)
    for cuadro in cuadro_bebidas:
        cuadro.config(state=DISABLED)
    for cuadro in cuadro_postres:
        cuadro.config(state=DISABLED)

    # destilo el checkbox
    for var in var_comidas:
        var.set(0)
    for var in var_bebidas:
        var.set(0)
    for var in var_postres:
        var.set(0)

    # borro cuadros de subtota, impuestos, total ...
    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postre.set('')
    var_subtotal.set('')
    var_impuesto.set('')
    var_total.set('')


# inicio tkinter 
app = Tk()

# tamaño de la ventana
app.geometry('1220x630+0+0')

# evitar agrandar ventana con el mouse
app.resizable(0, 0)

# titulo de la ventana
app.title('Mi restaurante - Sistema de facturacion')

# color de fondo
app.config(bg='burlywood')

# *** panel superior ***
panel_sup = Frame(app, bd=1, relief=FLAT)
panel_sup.pack(side=TOP)

# etiqueta de panel superior
etiqueta_sup = Label(panel_sup, text='Sistema de facturacion', fg='azure4', font=('Dsosis', 58),bg='burlywood', width=27)
etiqueta_sup.grid(row=0, column=0)

# *** panel izquierdo ***
panel_izq = Frame(app, bd=1, relief=FLAT)
panel_izq.pack(side=LEFT)

# panel costos (el mas abajo)
panel_costos = Frame(panel_izq, bd=1, relief=FLAT, bg='azure4', padx=70)
panel_costos.pack(side=BOTTOM)

# panel comidas
panel_comidas = LabelFrame(panel_izq, text="Comida", font=('Dosis', 19, 'bold'), bd=1, relief=FLAT, fg='azure4')
panel_comidas.pack(side=LEFT)

# panel bebidas
panel_bebidas = LabelFrame(panel_izq, text="Bebidas", font=('Dosis', 19, 'bold'), bd=1, relief=FLAT, fg='azure4')
panel_bebidas.pack(side=LEFT)

# panel postres
panel_postres = LabelFrame(panel_izq, text="Postres", font=('Dosis', 19, 'bold'), bd=1, relief=FLAT, fg='azure4')
panel_postres.pack(side=LEFT)

# *** panel derecha ***
panel_der = Frame(app, bd=1, relief=FLAT)
panel_der.pack(side=RIGHT)

# panel calculadora
panel_calc = Frame(panel_der, bd=1, relief=FLAT, bg='burlywood')
panel_calc.pack()

# panel recibo
panel_recibo = Frame(panel_der, bd=1, relief=FLAT, bg='burlywood')
panel_recibo.pack()

# panel botones
panel_botones = Frame(panel_der, bd=1, relief=FLAT, bg='burlywood')
panel_botones.pack()

# lista de productos
lista_comidas = ['pollo', 'cordero', 'salmon', 'pizza', 'ñoquis', 'ravioles', 'sushi', 'asado']
lista_bebidas = ['cerveza', 'soda', 'tekila', 'vodka', 'gaseosa', 'agua minera', 'vino blanco', 'vino tinto']
lista_postres = ['helado', 'fruta', 'brownies', 'flan', 'mousse', 'pastel', 'tarta', 'medialunas']

# genero items comida
var_comidas = []
cuadro_comidas = []
texto_comidas = []
contador = 0 
for comida in lista_comidas:
    # creo los ckeckbuttons
    var_comidas.append('')
    var_comidas[contador] = IntVar()
    item = Checkbutton(panel_comidas, text=comida.title(), font=('Dosis', 19, 'bold'), onvalue=1, offvalue=0, variable=var_comidas[contador], command=revisar_check)    
    item.grid(row=contador, column=0, sticky=W)

    # creo los cuadros de entrada (inputs de cantida)
    cuadro_comidas.append('')
    texto_comidas.append('')
    
    texto_comidas[contador] = StringVar()# para setear 0 en el input
    texto_comidas[contador].set('0')# para setear 0 en el input

    cuadro_comidas[contador] = Entry(panel_comidas, font=('Dosis', 18, 'bold'), bd=1, width=6, state=DISABLED,textvariable=texto_comidas[contador])
    cuadro_comidas[contador].grid(row=contador, column=1, sticky=W)

    contador += 1

# genero items bebidas
var_bebidas = []
cuadro_bebidas = []
texto_bebidas = []
contador = 0 
for bebida in lista_bebidas:
    # creo los ckeckbuttons
    var_bebidas.append('')
    var_bebidas[contador] = IntVar()
    item = Checkbutton(panel_bebidas, text=bebida.title(), font=('Dosis', 19, 'bold'), onvalue=1, offvalue=0, variable=var_bebidas[contador], command=revisar_check)
    item.grid(row=contador, column=0, sticky=W)

    # creo los cuadros de entrada (inputs de cantida)
    cuadro_bebidas.append('')
    texto_bebidas.append('')
   
    texto_bebidas[contador] = StringVar()
    texto_bebidas[contador].set('0')

    cuadro_bebidas[contador] = Entry(panel_bebidas, font=('Dosis', 18, 'bold'), bd=1, width=6, state=DISABLED,textvariable=texto_bebidas[contador])
    cuadro_bebidas[contador].grid(row=contador, column=1, sticky=W)

    contador += 1

# genero items postres
var_postres = []
cuadro_postres = []
texto_postres = []
contador = 0 
for postre in lista_postres:
    # creo los ckeckbuttons
    var_postres.append('')
    var_postres[contador] = IntVar()
    item = Checkbutton(panel_postres, text=postre.title(), font=('Dosis', 19, 'bold'), onvalue=1, offvalue=0, variable=var_postres[contador], command=revisar_check)
    item.grid(row=contador, column=0, sticky=W)

    # creo los cuadros de entrada (inputs de cantida)
    cuadro_postres.append('')
    texto_postres.append('')

    texto_postres[contador] = StringVar()
    texto_postres[contador].set('0')

    cuadro_postres[contador] = Entry(panel_postres, font=('Dosis', 18, 'bold'), bd=1, width=6, state=DISABLED,textvariable=texto_postres[contador])
    cuadro_postres[contador].grid(row=contador, column=1, sticky=W)

    contador += 1

# etiquetas de costo y campos de entrada

# variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_impuesto = StringVar()
var_subtotal = StringVar()
var_total = StringVar()

# comida
etiqueta_costo_comida = Label(panel_costos, text='Costo Comida', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida = Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=41)

# bebida
etiqueta_costo_bebida = Label(panel_costos, text='Costo Bebida', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_costo_bebida.grid(row=1, column=0)

texto_costo_bebida = Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx=41)

# postre
etiqueta_costo_postre = Label(panel_costos, text='Costo Postre', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_costo_postre.grid(row=2, column=0)

texto_costo_postre = Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=var_costo_postre)
texto_costo_postre.grid(row=2, column=1, padx=41)

# subtotal
etiqueta_subtotal = Label(panel_costos, text='Costo Subtotal', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_subtotal.grid(row=0, column=2)

texto_subtotal = Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=41)

# impuestos
etiqueta_impuestos = Label(panel_costos, text='Costo Impuestos', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_impuestos.grid(row=1, column=2)

texto_impuestos = Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=var_impuesto)
texto_impuestos.grid(row=1, column=3, padx=41)

# total
etiqueta_total = Label(panel_costos, text='Costo Total', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_total.grid(row=2, column=2)

texto_total = Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=var_total)
texto_total.grid(row=2, column=3, padx=41)

# ----
# botones 
botones =['total', 'recibo', 'guardar', 'resetear']
botones_creados = []
columnas = 0
for boton in botones:
    boton = Button(panel_botones, text=boton.title(), font=('Dosis', 14, 'bold'), fg='white', bg='azure4', bd=1, width=9)
    botones_creados.append(boton)
    boton.grid(row=0, column=columnas)
    columnas += 1

botones_creados[0].config(command=get_total)
botones_creados[1].config(command=get_recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)

# area de recibo
texto_recibo = Text(panel_recibo, font=('Dosis',12, 'bold'), bd=1, width=49, height=10)
texto_recibo.grid(row=0, column=0)

# ----
# calculadora 
visor_calculadora = Entry(panel_calc, font=('Dosis', 16, 'bold'), width=37, bd=1)
visor_calculadora.grid(row=0, column=0, columnspan=4)

# botones de la calculadora
botones_calc = ['7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', 'x', 'R', 'B', '0', '/']
botones_guardados = []

fila_calc = 1
columna_calc = 0

for boton in botones_calc:
    boton = Button(panel_calc,text=boton.title(), font=('Dosis', 16, 'bold'), fg='white', bg='azure4', bd=1, width=8)
    boton.grid(row=fila_calc, column=columna_calc)

    botones_guardados.append(boton)

    if columna_calc == 3:
        fila_calc += 1
    
    columna_calc += 1

    if columna_calc == 4:
        columna_calc =0

botones_guardados[0].config(command=lambda: click_btn_cal('7'))
botones_guardados[1].config(command=lambda: click_btn_cal('8'))
botones_guardados[2].config(command=lambda: click_btn_cal('9'))
botones_guardados[3].config(command=lambda: click_btn_cal('+'))
botones_guardados[4].config(command=lambda: click_btn_cal('4'))
botones_guardados[5].config(command=lambda: click_btn_cal('5'))
botones_guardados[6].config(command=lambda: click_btn_cal('6'))
botones_guardados[7].config(command=lambda: click_btn_cal('-'))
botones_guardados[8].config(command=lambda: click_btn_cal('1'))
botones_guardados[9].config(command=lambda: click_btn_cal('2'))
botones_guardados[10].config(command=lambda: click_btn_cal('3'))
botones_guardados[11].config(command=lambda: click_btn_cal('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda: click_btn_cal('0'))
botones_guardados[15].config(command=lambda: click_btn_cal('/'))

# evito que la pantalla se cierre
app.mainloop() 