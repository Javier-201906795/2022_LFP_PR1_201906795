import tkinter as tk
#INTERFACES GRAFICAS VENTANAS
import LFP_VNT0_Errores as VNT0


ventana = tk.Tk()
ventana.geometry('300x200')
ventana.title('PRACTICA 1')
#█═══════════════[ Textos ] ══════════════════════════════════█
#mensaje = "fhoofkljdfkljdsaklfjdaklfj dfjdfkljsdklfjdl fdfjklsdafjkldafjkld f aaaaa  ffff  bbbb cc ccffffff"
mensaje = "fhoofkljdfkljdsaklfjdaklfj dfjdfkljsdklfjdl fdfjklsdafjkldafjkld f aaaaa  ffff  bbbb cc ccffffff dfjfldjdklfjdklafl dfljdklfj dklf dfjdklfjklda d f lkjdkl fjda fsda fldsl fkd fsdkl fsdfjsdklfjkldfjkld lda fjkldafjskldaf a fhoofkljdfkljdsaklfjdaklfj dfjdfkljsdklfjdl fdfjklsdafjkldafjkld f aaaaa  ffff  bbbb cc ccffffff dfjfldjdklfjdklafl dfljdklfj dklf dfjdklfjklda d f lkjdkl fjda fsda fldsl fkd fsdkl fsdfjsdklfjkldfjkld lda fjkldafjskldaf a fhoofkljdfkljdsaklfjdaklfj dfjdfkljsdklfjdl fdfjklsdafjkldafjkld f aaaaa  ffff  bbbb cc ccffffff dfjfldjdklfjdklafl dfljdklfj dklf dfjdklfjklda d f lkjdkl fjda fsda fldsl fkd fsdkl fsdfjsdklfjkldfjkld lda fjkldafjskldaf a"
tk.Button(ventana, text='Enviar', command= lambda : VNT0.Mostrar(mensaje)).place(x=10, y=125)

ventana.mainloop()



