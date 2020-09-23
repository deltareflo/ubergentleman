import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Cuestionario COVID-19")
        
        self.seleccion0=tk.IntVar()
        self.seleccion0.set(0)
        self.seleccion1=tk.IntVar()
        self.seleccion1.set(0)
        self.seleccion2=tk.IntVar()
        self.seleccion2.set(0)
        self.seleccion3=tk.IntVar()
        self.seleccion3.set(0)
        self.seleccion4=tk.IntVar()
        self.seleccion4.set(0)
        self.seleccion5=tk.IntVar()
        self.seleccion5.set(0)
        self.seleccion6=tk.IntVar()
        self.seleccion6.set(0)
        self.seleccion7=tk.IntVar()
        self.seleccion7.set(0)
        self.seleccion8=tk.IntVar()
        self.seleccion8.set(0)
        self.seleccion9=tk.IntVar()
        self.seleccion9.set(0)
        self.seleccion10=tk.IntVar()
        self.seleccion10.set(0)
        self.seleccion11=tk.IntVar()
        self.seleccion11.set(0)
        self.seleccion12=tk.IntVar()
        self.seleccion12.set(0)
        self.titulo=tk.Label(self.ventana1,text="Autocuestionario SARS-Cov2 (Covid-19)")
        self.titulo.grid(columnspan=3,row=0)
        self.titulo.config(font=("arial", 16, "bold"))
        self.item1=tk.Label(self.ventana1,text="¿Estás teniendo tos?")
        self.item1.grid(column=0,row=1)
        self.radio1=tk.Radiobutton(self.ventana1,text="Sí", variable=self.seleccion0, value=1)
        self.radio1.grid(column=1, row=1)
        self.radio2=tk.Radiobutton(self.ventana1,text="No", variable=self.seleccion0, value=0)
        self.radio2.grid(column=2, row=1)
        self.item2=tk.Label(self.ventana1,text="¿Estás teniendo escalofríos?")
        self.item2.grid(column=0,row=2)
        self.item2_1=tk.Radiobutton(self.ventana1,text="Sí", variable=self.seleccion1, value=1)
        self.item2_1.grid(column=1, row=2)
        self.radio2_2=tk.Radiobutton(self.ventana1,text="No", variable=self.seleccion1, value=0)
        self.radio2_2.grid(column=2, row=2)
        self.item3=tk.Label(self.ventana1,text="En este momento o en los días previos ¿has tenido diarrea?")
        self.item3.grid(column=0,row=3)
        self.item3_1=tk.Radiobutton(self.ventana1,text="Sí", variable=self.seleccion2, value=1)
        self.item3_1.grid(column=1, row=3)
        self.item3_2=tk.Radiobutton(self.ventana1,text="No", variable=self.seleccion2, value=0)
        self.item3_2.grid(column=2, row=3)
        self.item4=tk.Label(self.ventana1,text="¿Tienes dolor de garganta?")
        self.item4.grid(column=0,row=4)
        self.item4_1=tk.Radiobutton(self.ventana1,text="Sí", variable=self.seleccion3, value=1)
        self.item4_1.grid(column=1, row=4)
        self.item4_2=tk.Radiobutton(self.ventana1,text="No", variable=self.seleccion3, value=0)
        self.item4_2.grid(column=2, row=4)
        self.item5=tk.Label(self.ventana1,text="¿Estás teniendo dolor de cuerpo y malestar general?")
        self.item5.grid(column=0,row=5)
        self.item5_1=tk.Radiobutton(self.ventana1,text="Sí", variable=self.seleccion4, value=1)
        self.item5_1.grid(column=1, row=5)
        self.item5_2=tk.Radiobutton(self.ventana1,text="No", variable=self.seleccion4, value=0)
        self.item5_2.grid(column=2, row=5)
        self.item6=tk.Label(self.ventana1,text="¿Estás presentando dolor de cabeza?")
        self.item6.grid(column=0,row=6)
        self.item6_1=tk.Radiobutton(self.ventana1,text="Sí", variable=self.seleccion5, value=1)
        self.item6_1.grid(column=1, row=6)
        self.item6_2=tk.Radiobutton(self.ventana1,text="No", variable=self.seleccion5, value=0)
        self.item6_2.grid(column=2, row=6)
        self.item7=tk.Label(self.ventana1,text="¿Has tenido fiebre? [para fines correctos más de 37,8°C]")
        self.item7.grid(column=0,row=7)
        self.item7_1=tk.Radiobutton(self.ventana1,text="Sí", variable=self.seleccion6, value=1)
        self.item7_1.grid(column=1, row=7)
        self.item7_2=tk.Radiobutton(self.ventana1,text="No", variable=self.seleccion6, value=0)
        self.item7_2.grid(column=2, row=7)
        self.item8=tk.Label(self.ventana1,text="¿Has perdido el olfato?")
        self.item8.grid(column=0,row=8)
        self.item8_1=tk.Radiobutton(self.ventana1,text="Sí", variable=self.seleccion7, value=1)
        self.item8_1.grid(column=1, row=8)
        self.item8_2=tk.Radiobutton(self.ventana1,text="No", variable=self.seleccion7, value=0)
        self.item8_2.grid(column=2, row=8)
        self.item9=tk.Label(self.ventana1,text="¿Estás teniendo dificultad para respirar? [como si no entrara el aire al pecho]")
        self.item9.grid(column=0,row=9)
        self.item9_1=tk.Radiobutton(self.ventana1,text="Sí", variable=self.seleccion8, value=2)
        self.item9_1.grid(column=1, row=9)
        self.item9_2=tk.Radiobutton(self.ventana1,text="No", variable=self.seleccion8, value=0)
        self.item9_2.grid(column=2, row=9)
        self.item10=tk.Label(self.ventana1,text="¿Estás experimentando fatiga? [real deterioro de mis movimientos y mis ganas de hacer algo]")
        self.item10.grid(column=0,row=10)
        self.item10_1=tk.Radiobutton(self.ventana1,text="Sí", variable=self.seleccion9, value=2)
        self.item10_1.grid(column=1, row=10)
        self.item10_2=tk.Radiobutton(self.ventana1,text="No", variable=self.seleccion9, value=0)
        self.item10_2.grid(column=2, row=10)
        self.item11=tk.Label(self.ventana1,text="¿Has viajado en los últimos 14 días?")
        self.item11.grid(column=0,row=11)
        self.item11_1=tk.Radiobutton(self.ventana1,text="Sí", variable=self.seleccion10, value=3)
        self.item11_1.grid(column=1, row=11)
        self.item11_2=tk.Radiobutton(self.ventana1,text="No", variable=self.seleccion10, value=0)
        self.item11_2.grid(column=2, row=11)
        self.item12=tk.Label(self.ventana1,text="¿Has viajado (o en contacto con alguien que haya viajado) o estado en área afectada por SARS-COV2 (COVID-19)?")
        self.item12.grid(column=0,row=12)
        self.item12_1=tk.Radiobutton(self.ventana1,text="Sí", variable=self.seleccion11, value=3)
        self.item12_1.grid(column=1, row=12)
        self.item12_2=tk.Radiobutton(self.ventana1,text="No", variable=self.seleccion11, value=0)
        self.item12_2.grid(column=2, row=12)
        self.item13=tk.Label(self.ventana1,text="¿Has estado en contacto directo o cuidado a algún paciente positivo de SARS-COV2 (COVID-19)?")
        self.item13.grid(column=0,row=13)
        self.item13_1=tk.Radiobutton(self.ventana1,text="Sí", variable=self.seleccion12, value=3)
        self.item13_1.grid(column=1, row=13)
        self.item13_2=tk.Radiobutton(self.ventana1,text="No", variable=self.seleccion12, value=0)
        self.item13_2.grid(column=2, row=13)
        

        self.boton1=tk.Button(self.ventana1, text="Mostrar resultado", command=self.sumatoria, bg="green")
        self.boton1.grid(column=0, row=15)
        self.boton2=tk.Button(self.ventana1, text="Restablecer", command=self.borrar, bg="red")
        self.boton2.grid(column=1, row=15, columnspan=2)
        self.resultado=tk.Label(text="Resultado")
        self.resultado.grid(column=0, row=16)
        self.label1=tk.Label(text="")
        self.label1.grid(column=0, row=17)
        self.descripcion=tk.Label(text="Descripción")
        self.descripcion.grid(column=0, row=18)
        self.label2=tk.Label(text="")
        self.label2.grid(column=0, row=19)
        self.ventana1.mainloop()

    def borrar(self):
        self.T.delete("1.0", tk.END)
        self.label2.configure(text="", background="white")
        self.label1.configure(text="")
        self.seleccion0.set(0)
        self.seleccion1.set(0)
        self.seleccion2.set(0)
        self.seleccion3.set(0)
        self.seleccion4.set(0)
        self.seleccion5.set(0)
        self.seleccion6.set(0)
        self.seleccion7.set(0)
        self.seleccion8.set(0)
        self.seleccion9.set(0)
        self.seleccion10.set(0)
        self.seleccion11.set(0)
        self.seleccion12.set(0)
        

    def sumatoria(self):
        self.suma=0
        messagebox.showinfo("Advertencia", "Esto no es un diagnóstico y no sustituye una consulta con su médico")
        self.nombre_text=tk.StringVar()
        self.suma=self.seleccion0.get()+self.seleccion1.get()+self.seleccion2.get()+self.seleccion3.get()+self.seleccion4.get()+self.seleccion5.get()+self.seleccion6.get()+self.seleccion7.get()+self.seleccion8.get()+self.seleccion9.get()+self.seleccion10.get()+self.seleccion11.get()+self.seleccion12.get()
        self.label1.configure(text=str(self.suma))
        if self.suma<3:
            self.label2.configure(text="Podría ser estrés, tome sus precauciones y observe", font = ("arial", 12, "bold"), foreground = "green")
        elif self.suma<6:
            self.label2.configure(text="Hidratese, conserve medidas de higiene, observe y reevalúe en 2 días", font = ("arial", 12, "bold"), foreground = "green")
        elif self.suma<12:
            self.label2.configure(text="Acuda a consulta con el médico", font = ("arial", 12, "bold"), background = "black", foreground = "yellow")
        else:
            self.label2.configure(text="Llame a los servicios para realizar detección para SARS-COV2 (COVID-19)", font = ("arial", 12, "bold"), foreground = "red")
        self.T = tk.Text(self.ventana1, height=8, width=100,  state="normal", font=('Times New Roman', 12))
        self.SS = tk.Scrollbar(self.ventana1)
        self.SS.config(command=self.T.yview)
        self.T.config(yscrollcommand=self.SS.set)
        self.T.grid(column=0, row=20, padx=5, pady=5, columnspan=3)
        self.SS.grid(column=3, row=20)
        self.T.insert(tk.END,"""Informaciones útiles\nTelefonos a los que puede consultar\n
911\n
137 SOS Mujer\n
Contención psicológica para población en general. Consulta a distancia por Voluntarios del departamento de salud mental de la 6ta región sanitaria:\n
	Lic. Ester López. Lunes a viernes/Turno tarde/14:00 a 19:00 h/ 0983 477019\n
	Lic. Gladys Gauto/ Viernes/ Turnos Mañana y Tarde/ 0981 670367\n
	Lic. Margarita López/ Lunes a viernes 07:00 a 13:00 h/ 0982 893992\n
	Lic. Cinthia Chávez/ Lunes, miercoles y viernes/ Turno Tarde/ 14:00 a 19:00 h/ 0983 789878\n
	Lic. Vittorip Ramirez/ Jueves/ 08:00 a 17:00 h/ 0984 363087\n
	Lic. Rosana Prieto/ Lunes a viernes/Turno mañana/ 07:00 a 11:00 h/ 0981 314 684\n
Cátedra De Psiquiatría Hospital De Clínicas- 24h/ +595 962 440001\n
E-Medicus 0983 522583\n
Ambiente Gestaltico- Apoyo psicológico gratuito\n
	Lic. Osvaldo Escobar/ 0981 843900\n
	Lic. Luis Cortesi/ 0994 700225\n
OMS- Información y orientación sobre el COVID-19/ Enviar la palabra "Hola" por whatsapp al +41 225017690\n

Páginas Web a las que puede acceder para información o consulta\n

Atención de profesionales de salud mental. Copiar el siguiente enlace: https://bit.ly/2ydInYe\n
OMS https://www.who.int/es/emergencies/diseases/novel-coronavirus-2019\n
Consejos para afrontar el COVID-19 por ECIS http://www.ecisweb.com/documentos\n    
    """)
aplicacion1=Aplicacion()