from tkinter import *
from tkinter import messagebox
#pip install pypng
import png
#pip install pyqrcode
import pyqrcode
#pip install Pillow
from PIL import *
from PIL import Image, ImageTk
from sys import exit
#pip install os-sys
import os


# Definir una función para generar el código qr
def generateQR() :
    
    if os.path.exists("img1.png"):
        os.remove(img1.png)
    
    
    #Obtener el link al que se desea ir. Caja de entrada usando el método get
    inputString = enterTextField.get()
 
    # Valor de la escala del qr
    scale = enterScaleField.get()
    
    #Nombre del archivo png
    nombre = "CodigoQR"

    #si la escala no se ingresa, el valor de escala predeterminado se establece en 5
    if len(scale) :
        
        try :
             
            #conversion de cadena ingresada a entero
            scale = int(scale)
 
        # Si el tipo de conversión no es posible, muestramensaje de error
        except :
            
            messagebox.showerror("Error",
            "La escala debe ser un valor entero. Por ejemplo: 1, 2 , 3 ..")
    
            return
             
    else :
         
        #Establecer valor determinado de la escala
        scale = 5
         
   #si el campo de texto de entrada no está vacío, se creará un código QR. Caso contrario mostraremos un mensaje de error
    if len(inputString) : 
       
        #Generando un objeto de código QR usando la clase create () del módulo pyqrcode
        qrCode = pyqrcode.create(inputString)
        
        #  Guarda este objeto qrCode como un archivo svg con escala 4 usando el método svg() del objeto qrCode.El atributo de escala determina la dimensión de la imagen svg creada
        
        qrCode.svg(f"{nombre}.svg",
                    scale = scale)
 
        #Guarde este objeto qrCode como un archivo png con escala 4 usando el método png() del objeto qrCode
        
        qrCode.png(f"{nombre}.png",
                    scale = scale)
 
        # Mensaje de que se pudo crear el Codigo QR
        messagebox.showinfo('CódigoQR creado!!',
        "El códigoQR se creó con éxito y fue guardado como archivos:CodigoQR.png/.svg")
 
         
    # Se mostrará un mensaje de error si el campo de texto de entrada está vacío
    else :

        messagebox.showerror("Error", "Text field is Empty")
        
    
    
    #Mostrar la imagen en pantalla
    
    img=Image.open(f"{nombre}.png")
    new_img=img.resize((390,360))
    render=ImageTk.PhotoImage(new_img)
    img1=Label(ventana, image= render)
    img1.image= render
    img1.place(x=160, y=308)
 
#Funcion para borrar el contenido de las entradas de texto
def clearAll() :

    enterTextField.delete(0, END)  
    enterTextField.focus_set() 
    enterScaleField.delete(0,END)
    enterScaleField.focus_set()
    

 
# Codigo principal
if __name__ == "__main__" :
    
    # Creando ventana
    ventana = Tk()
    
    #Estableciendo color de la ventana
    ventana.configure(background = 'light blue')
    
    # Estableciendo dimensiones de la ventana
    ventana.geometry("700x700")
 
    # Titulo del programa
    ventana.title("QR CODE GENERATOR")

    # Titulo de la ventana
    titulo = Label(ventana, text="~ GENERADOR CODIGO QR ~", font="italic", fg="black", bg="light goldenrod").place(relx=0.33, rely=0.04)

    # label ingreso de datos

    enterTextLabel = Label(ventana, text = "Ingrese dirección de destino (Url)",fg = 'black', bg = 'grey').place(relx=0.10, rely=0.15)

    enterTextField = Entry(ventana)
    enterTextField.place(relx=0.10, rely=0.20)

  
    enterScaleLabel = Label(ventana, text = "Ingrese Nro escala",fg = 'black', bg = 'grey').place(relx=0.70, rely=0.15)
    enterScaleLabel2 = Label(ventana, text = "Se modificará en los archivos .png y .svg",fg = 'black',bg='light blue').place(relx=0.63, rely=0.23)
    
    enterScaleField = Entry(ventana)
    enterScaleField.place(relx=0.70, rely=0.20)
    
    
    generateButton = Button(ventana, text = "Generar Código",bg = "RosyBrown1", fg = "black",command = generateQR).place(relx=0.25, rely=0.32)
    clearButton = Button(ventana, text = "Limpiar casillas",bg = "PaleGreen3", fg = "black",command = clearAll).place(relx=0.60, rely=0.32)

    clearButton = Button(ventana, text = "Salir",bg = "navajo white", fg = "black",command = exit).place(relx=0.90, rely=0.96)

 
  
  
    ventana.mainloop()

