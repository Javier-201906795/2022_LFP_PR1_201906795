import tkinter as tk
#INTERFACES GRAFICAS VENTANAS
import LFP_VNT0_Errores as VNT0
import LFP_VNT2_2_Editar as VNT2_2


ventana = tk.Tk()
ventana.geometry('300x200')
ventana.title('PRACTICA 1')
#█═══════════════[ Textos ] ══════════════════════════════════█
#mensaje = "fhoofkljdfkljdsaklfjdaklfj dfjdfkljsdklfjdl fdfjklsdafjkldafjkld f aaaaa  ffff  bbbb cc ccffffff"

tk.Button(ventana, text='Enviar', command= lambda : VNT2_2.Mostrar()).place(x=10, y=125)

ventana.mainloop()



