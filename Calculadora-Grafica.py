######## Graphic calculator   /   Calculadora gráfica  ########

import tkinter 

finestra = tkinter.Tk() #Defining a variable as tkinter. (the engine of the program)
finestra.title( "Calculadora bàsica" ) #The title of the finestra variable.
iterador = 0
#Defining a variable

#Entrada de texto    #Text input

entrada_t = tkinter.Entry(finestra, font = ("Calibri 20")) 
entrada_t.grid(row = 0, column = 0, columnspan = 5, padx = 5, pady = 5) 
#defining the structure through which the text is seen

#Funciones  #Functions

def clicar_boton(x):
    """
    This function defines what each button does when we click on it.
    
    Esta función define lo que hace cada boton a la hora de pulsarlo.
    """
    # Defining the iterador variable as global.
    global iterador  
    entrada_t.insert(iterador, x) 
    iterador = iterador + 1  
    # The variable is added so that each key is displayed on the screen in front of the one previously clicked. 

def eliminar():
    """
    This function defines what the AC (delete) button will do.

    Esta función define lo que hace el botón AC (borrar)
    """
    
    entrada_t.delete(0, tkinter.END)
    iterador = 0
    # The variable is reset so that the new numbers start from position 0.

def operar():
    """
    This function defines what the button (=) has to do to perform the operations.

    Esta función define lo que hace el boton (=) para realizar las operaciones.
    """
    
    operacio = entrada_t.get() #I take the numbers put in the entrada_t.
    resultat = eval(operacio) # The function eval perform the operations.
    entrada_t.delete(0, tkinter.END) # Delete everything before displaying the result.
    entrada_t.insert(0, resultat) # Display the result.
    iterador = 0 
    # The variable is reset so that the new numbers start from position 0.

#Botones   #Buttons
"""
Here we show the characteristics of each button.

Aquí enseñamos las características de cada botón.
"""

boton1 = tkinter.Button(finestra, text = "1", width = 4, height = 4, command = lambda: clicar_boton(1))
boton2 = tkinter.Button(finestra, text = "2", width = 4, height = 4, command = lambda: clicar_boton(2))
boton3 = tkinter.Button(finestra, text = "3", width = 4, height = 4, command = lambda: clicar_boton(3))
boton4 = tkinter.Button(finestra, text = "4", width = 4, height = 4, command = lambda: clicar_boton(4))
boton5 = tkinter.Button(finestra, text = "5", width = 4, height = 4, command = lambda: clicar_boton(5))
boton6 = tkinter.Button(finestra, text = "6", width = 4, height = 4, command = lambda: clicar_boton(6))
boton7 = tkinter.Button(finestra, text = "7", width = 4, height = 4, command = lambda: clicar_boton(7))
boton8 = tkinter.Button(finestra, text = "8", width = 4, height = 4, command = lambda: clicar_boton(8))
boton9 = tkinter.Button(finestra, text = "9", width = 4, height = 4, command = lambda: clicar_boton(9))
boton0 = tkinter.Button(finestra, text = "0", width = 13, height = 7, command = lambda: clicar_boton(0))


boton_eliminar = tkinter.Button(finestra, text = "AC", width = 4, height = 4, command = lambda: eliminar())
boton_parent1 = tkinter.Button(finestra, text = "(", width = 4, height = 4, command = lambda: clicar_boton("("))
boton_parent2 = tkinter.Button(finestra, text = ")", width = 4, height = 4, command = lambda: clicar_boton(")"))
boton_punt = tkinter.Button(finestra, text = ".", width = 4, height = 7, command = lambda: clicar_boton("."))

boton_div = tkinter.Button(finestra, text = "/", width = 4, height = 4, command = lambda: clicar_boton("/"))
boton_multi = tkinter.Button(finestra, text = "x", width = 4, height = 4, command = lambda: clicar_boton("*"))
boton_elevar = tkinter.Button(finestra, text = "^", width = 4, height = 4, command = lambda: clicar_boton("**"))
boton_sumar = tkinter.Button(finestra, text = "+", width = 4, height = 4, command = lambda: clicar_boton("+"))
boton_restar = tkinter.Button(finestra, text = "-", width = 4, height = 4, command = lambda: clicar_boton("-"))
boton_igual = tkinter.Button(finestra, text = "=", width = 4, height = 4, command = lambda: operar())


#Botones en pantalla    #On-screan buttons
"""
Here we show how the buttons will look on the screen.

Aquí enseñamos como se verán los botones en pantalla.
"""

boton1.grid(row = 4, column = 0, padx = 4, pady = 4) # Padx and pady are the outer margins of each button.
boton2.grid(row = 4, column = 1, padx = 4 , pady = 4)
boton3.grid(row = 4, column = 2, padx = 4 , pady = 4)
boton4.grid(row = 3, column = 0, padx = 4 , pady = 4)
boton5.grid(row = 3, column = 1, padx = 4 , pady = 4)
boton6.grid(row = 3, column = 2, padx = 4, pady = 4)
boton7.grid(row = 2, column = 0, padx = 4 , pady = 4)
boton8.grid(row = 2, column = 1, padx = 4 , pady = 4)
boton9.grid(row = 2, column = 2, padx = 4 , pady = 4)
boton0.grid(row = 5, rowspan = 2, column = 0, columnspan = 2, padx = 4 , pady = 5)
 
boton_eliminar.grid(row = 1, column = 0, padx = 4 , pady = 4)
boton_parent1.grid(row = 1, column = 1, padx = 4 , pady = 4)
boton_parent2.grid(row = 1, column = 2, padx = 4 , pady = 4)
boton_punt.grid(row = 5, rowspan= 2, column = 2, padx = 4 , pady = 5)

boton_div.grid(row = 1, column = 3, padx = 4 , pady = 4)
boton_multi.grid(row = 2, column = 3, padx = 4 , pady = 4)
boton_elevar.grid(row = 3, column = 3, padx = 4, pady = 4)
boton_sumar.grid(row = 4, column = 3, padx = 4 , pady = 4)
boton_restar.grid(row = 5, column = 3, padx = 4 , pady = 4)
boton_igual.grid(row = 6, column = 3, padx = 4 , pady = 4)



finestra.mainloop()
