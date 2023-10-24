import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from AnalizadorLexico import AnalizadorLexico
from AnalizadorSintactico import AnalizadorSintactico
from graphviz import Source
import os

analizador_lexico= AnalizadorLexico()
analizador_sintactico = AnalizadorSintactico()

class Controlador():
    def __init__(self):
        self.root = tk.Tk()
        self.text_input = tk.Text()
        self.combo = ttk.Combobox()
        self.text_output = tk.Text()
        self.tokens_lexico = []
        self.errores_lexico = []
        self.errores_sintacticos = []
        self.node = ''
        self.transicion = ''

    # 'src\\prueba 2.bizdata'
    def abrir(self):
        archivo = filedialog.askopenfilename(title='Seleccione un archivo', filetypes=(('.bizdata files', '*.bizdata'), ('all files', '*.*')))
        if archivo:
            with open(archivo, 'r', encoding='UTF-8') as file:
                contenido = file.read()
                self.text_input.delete('1.0', tk.END)
                self.text_input.insert(tk.END, contenido)
                self.text_input.insert(tk.END, '\n♥')
                file.close()
        
    def analizar(self):
        txt = self.text_input.get('1.0', tk.END)
        if txt.strip() != '':
            self.tokens_lexico = analizador_lexico.analizar(txt)
            self.errores_lexico = analizador_lexico.get_lista_errores()  
            texto_salida, self.node, self.transicion = analizador_sintactico.analizar(self.tokens_lexico)
            self.errores_sintacticos = analizador_sintactico.get_lista_errores()
            
            messagebox.showinfo(message='Análisis finalizado.', title='Análisis')
            self.text_output.config(state='normal')
            self.text_output.delete('1.0', tk.END)
            self.text_output.insert(tk.END, texto_salida)
            self.text_output.config(state='disabled')
            self.combo.config(state='readonly')
        else:
            messagebox.showerror(message='No hay texto para analizar.', title='Análisis')
    
    def reporte_errores(self):
        t_body_lexico = ''
        t_body_sintacticos = ''
        no = 0
        for lexico in self.errores_lexico:
            t_body_lexico += '<tr>\n'
            t_body_lexico += f'<td>{no}</td>\n'
            t_body_lexico += f'<td>{lexico.char}</td>\n'
            t_body_lexico += f'<td>{lexico.lexema}</td>\n'
            t_body_lexico += f'<td>{lexico.linea}</td>\n'
            t_body_lexico += f'<td>{lexico.columna}</td>\n'
            t_body_lexico += '</tr>\n'
            no += 1
        
        no = 0
        for sintacticos in self.errores_sintacticos:
            t_body_sintacticos += '<tr>\n'
            t_body_sintacticos += f'<td>{no}</td>\n'
            t_body_sintacticos += f'<td>{sintacticos.char}</td>\n'
            t_body_sintacticos += f'<td>{sintacticos.lexema}</td>\n'
            t_body_sintacticos += f'<td>{sintacticos.linea}</td>\n'
            t_body_sintacticos += f'<td>{sintacticos.columna}</td>\n'
            t_body_sintacticos += '</tr>\n'
            no += 1
        
        html_contenido_lexico = f'''
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <title>Reporte Errores Lexicos</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="stylesheet" type="text/css" href="../css/styles.css">
        </head>
        <body>
            <div class="container">
                <h1>Reporte Errores Lexicos</h1>
                <table>
                    <thead>
                        <tr>
                            <th> No. </th>
                            <th> Error </th>
                            <th> Tipo </th>
                            <th> Fila </th>
                            <th> Columna </th>
                        </tr>
                    </thead>
                    <tbody>
                        {t_body_lexico}
                    </tbody>
                </table>
            </div>
        </body>
        </html>
        '''
        
        html_contenido_sintactico = f'''
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <title>Reporte Errores Sintacticos</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="stylesheet" type="text/css" href="../css/styles.css">
        </head>
        <body>
            <div class="container">
                <h1>Reporte Errores Sintacticos</h1>
                <table>
                    <thead>
                        <tr>
                            <th> No. </th>
                            <th> Error </th>
                            <th> Tipo </th>
                            <th> Fila </th>
                            <th> Columna </th>
                        </tr>
                    </thead>
                    <tbody>
                        {t_body_sintacticos}
                    </tbody>
                </table>
            </div>
        </body>
        </html>
        '''
        messagebox.showinfo(message='Reporte de Errores generado.', title='Reporte de Errores')
        with open('./report/Error/Reporte Errores Lexicos.html', 'w', encoding='UTF-8') as file:
            file.write(html_contenido_lexico)
            file.close()
        
        with open('./report/Error/Reporte Errores Sintacticos.html', 'w', encoding='UTF-8') as file:
            file.write(html_contenido_sintactico)
            file.close()
    
    def reporte_arbol_derivacion(self):
        arbol = 'digraph G {\n' + self.node + self.transicion + '\n}'
        messagebox.showinfo(message='Reporte del Arbol de Derivación generado.', title='Arbol de Derivación')
        with open('./report/tree/Arbol de Derivación.dot', 'w', encoding='UTF-8') as file:
            file.write(arbol)
            file.close()
        graph = Source(arbol, filename='./report/tree/Arbol de Derivación', format='pdf')
        graph.render(filename='./report/tree/Arbol de Derivación', cleanup=True)
    
    def reporte_tokens(self):
        t_body = ''
        no = 0 
        for token in self.tokens_lexico:
            t_body += '<tr>\n'
            t_body += f'<td>{no}</td>\n'
            t_body += f'<td>{token.char}</td>\n'
            t_body += f'<td>{token.lexema}</td>\n'
            t_body += f'<td>{token.linea}</td>\n'
            t_body += f'<td>{token.columna}</td>\n'
            t_body += '</tr>\n'
            no += 1
        
        html_contenido = f'''
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <title>Reporte Tokens</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="stylesheet" type="text/css" href="../css/styles.css">
        </head>
        <body>
            <div class="container">
                <h1>Reporte Tokens</h1>
                <table>
                    <thead>
                        <tr>
                            <th> No. </th>
                            <th> Token </th>
                            <th> Lexema </th>
                            <th> Fila </th>
                            <th> Columna </th>
                        </tr>
                    </thead>
                    <tbody>
                        {t_body}
                    </tbody>
                </table>
            </div>
        </body>
        </html>
        '''
        messagebox.showinfo(message='Reporte de Tokens generado.', title='Reporte de Tokens')
        with open('./report/Token/Reporte Tokens.html', 'w', encoding='UTF-8') as file:
            file.write(html_contenido)
            file.close()
    
    def limpiar(self):
        self.text_input.delete('1.0', tk.END)
        self.text_output.config(state='normal')
        self.text_output.delete('1.0', tk.END)
        self.text_output.config(state='disabled')
        self.combo.config(state='disabled')
        self.tokens_lexico = []
        self.errores_lexico = []
        self.errores_sintacticos = []
        self.node = ''
        self.transicion = ''
        self.combo.set('Reportes')
        messagebox.showinfo(message='Se limpió el contenido.', title='Limpiar')
    
    def cargar_frame(self):
        ruta_error = 'report\\Error'
        ruta_token = 'report\\Token'
        ruta_tree = 'report\\Tree'
        if not os.path.exists(ruta_error):
            os.makedirs(ruta_error)
        if not os.path.exists(ruta_token):
            os.makedirs(ruta_token)
        if not os.path.exists(ruta_tree):
            os.makedirs(ruta_tree)
        
        #setting title
        self.root.title("Proyecto 2 - 202200174")
        #setting window size
        width=1250
        height=625
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)

        label = tk.Label(self.root)
        label["fg"] = "#333333"
        label["justify"] = "center"
        label["text"] = "Proyecto 2 - 202200174"
        label.place(x=30,y=20,width=158,height=30)

        button_abrir = tk.Button(self.root)
        button_abrir["bg"] = "#f0f0f0"
        button_abrir["fg"] = "#000000"
        button_abrir["justify"] = "center"
        button_abrir["text"] = "ABRIR"
        button_abrir.place(x=560,y=20,width=70,height=25)
        button_abrir["command"] = self.abrir

        button_analizar = tk.Button(self.root)
        button_analizar["bg"] = "#f0f0f0"
        button_analizar["fg"] = "#000000"
        button_analizar["justify"] = "center"
        button_analizar["text"] = "ANALIZAR"
        button_analizar.place(x=670,y=20,width=70,height=25)
        button_analizar["command"] = self.analizar

        self.combo = ttk.Combobox(self.root, values=['Reporte de Errores', 'Reporte de Tokens', 'Arbol de Derivación'], state='disabled')
        self.combo.set('Reportes')
        self.combo.place(x=800,y=20,width=125,height=25)

        self.text_input = tk.Text(self.root, wrap='word', font=("Arial", 11))
        self.text_input.place(x=30,y=70,width=490,height=500)

        self.text_output = tk.Text(self.root, wrap='word', font=("Arial", 11), state='disabled')
        self.text_output.place(x=550,y=70,width=675,height=500)
        
        button_limpiar = tk.Button(self.root)
        button_limpiar["bg"] = "#f0f0f0"
        button_limpiar["fg"] = "#000000"
        button_limpiar["justify"] = "center"
        button_limpiar["text"] = "LIMPIAR"
        button_limpiar.place(x=30,y=580,width=70,height=25)
        button_limpiar["command"] = self.limpiar
        
        
        self.combo.bind("<<ComboboxSelected>>", lambda event: self.combo_selected())
        self.root.mainloop()
    
    def combo_selected(self):
        seleccion = self.combo.get()
        if seleccion == 'Reporte de Errores':
            self.reporte_errores()
        elif seleccion == 'Reporte de Tokens':
            self.reporte_tokens()
        elif seleccion == 'Arbol de Derivación':
            self.reporte_arbol_derivacion()


