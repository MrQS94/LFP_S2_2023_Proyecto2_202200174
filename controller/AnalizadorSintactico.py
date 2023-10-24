from Modelos import Error
from prettytable import PrettyTable
# disable=C0116
# disable=C0200

class AnalizadorSintactico():
    def __init__(self):
        self.list_tokens = []
        self.list_errors = []
        self.list_claves = []
        self.list_registros = []
        self.count = 0
        self.registros_valores = []
        self.console = ''
        self.count_imprimir = 1
        self.transiciones = ''
        self.nodos = ''
        self.count_instrucciones = 0
        self.count_instruccion = 0
        self.count_clave = 0
        self.count_igual = 0
        self.count_corchete = 0
        self.count_list_claves = 0
        self.count_list_registro = 0
        self.count_cadena = 0
        self.count_coma = 0
        self.count_registro = 0
        self.count_decimal = 0
        self.count_llave = 0
        self.count_value = 0
        self.count_entero = 0
        self.count_proceso = 0
        self.count_parentesis = 0
        self.count_token = 0
    
    def incializar(self):
        self.list_tokens = []
        self.list_errors = []
        self.list_claves = []
        self.list_registros = []
        self.count = 0
        self.registros_valores = []
        self.console = ''
        self.count_imprimir = 1
        self.transiciones = ''
        self.nodos = ''
        self.count_instrucciones = 0
        self.count_instruccion = 0
        self.count_clave = 0
        self.count_igual = 0
        self.count_corchete = 0
        self.count_list_claves = 0
        self.count_list_registro = 0
        self.count_cadena = 0
        self.count_coma = 0
        self.count_registro = 0
        self.count_decimal = 0
        self.count_llave = 0
        self.count_value = 0
        self.count_entero = 0
        self.count_proceso = 0
        self.count_parentesis = 0
        self.count_token = 0
    
    def analizar(self, list_tokens):
        self.incializar()
        self.list_tokens = list_tokens
        self.list_errors = []
        self.nodos += 'node [style="filled"]\n'
        self.inicio()
        return self.console, self.nodos, self.transiciones
    
    def inicio(self):
        self.nodos += f'Instrucciones{self.count_instrucciones} [label="Instrucciones"];\n' 
        self.transiciones += f'inicio -> Instrucciones{self.count_instrucciones}\n'
        self.lista_instrucciones()
    
    def lista_instrucciones(self):
        if self.list_tokens[self.count].lexema.lower().lower() == 'registros':
            self.count_instrucciones += 1
            self.count_instruccion += 1
            self.nodos += f'Instrucciones{self.count_instrucciones} [label="Instrucciones"];\n' 
            self.nodos += f'Instruccion{self.count_instruccion} [label="Instruccion"];\n'
            self.transiciones += f'Instrucciones{self.count_instrucciones - 1} -> Instruccion{self.count_instruccion}\n'
            self.transiciones += f'Instruccion{self.count_instruccion} -> ProcesoRegistros\n'
            self.instrucciones_registros()    
            self.transiciones += f'Instrucciones{self.count_instrucciones - 1} -> Instrucciones{self.count_instrucciones}\n'
            self.lista_instrucciones()
        elif self.list_tokens[self.count].lexema.lower().lower() == 'claves':
            self.count_instrucciones += 1
            self.count_instruccion += 1
            self.nodos += f'Instrucciones{self.count_instrucciones} [label="Instrucciones"];\n'
            self.nodos += f'Instruccion{self.count_instruccion} [label="Instruccion"];\n'
            self.transiciones += f'Instrucciones{self.count_instrucciones - 1} -> Instruccion{self.count_instruccion}\n'
            self.transiciones += f'Instruccion{self.count_instruccion} -> ProcesoClaves\n'
            self.instrucciones_claves()
            self.transiciones += f'Instrucciones{self.count_instrucciones - 1} -> Instrucciones{self.count_instrucciones}\n'
            self.lista_instrucciones()
        elif self.list_tokens[self.count].lexema.lower().lower() == 'comentario simple':
            self.count += 1
            self.lista_instrucciones()
        elif self.list_tokens[self.count].lexema.lower().lower() == 'comillas simples':
            self.count += 1
            self.lista_instrucciones()
        elif self.list_tokens[self.count].lexema.lower().lower() == 'imprimir':
            self.count_instrucciones += 1
            self.count_instruccion += 1
            self.nodos += f'Instrucciones{self.count_instrucciones} [label="Instrucciones"];\n'
            self.nodos += f'Instruccion{self.count_instruccion} [label="Instruccion"];\n'
            self.nodos += f'ProcesoImprimir{self.count_proceso} [label="ProcesoImprimir"];\n'
            self.transiciones += f'Instrucciones{self.count_instrucciones - 1} -> Instruccion{self.count_instruccion}\n'
            self.transiciones += f'Instruccion{self.count_instruccion} -> ProcesoImprimir{self.count_proceso}\n'
            self.instrucciones_imprimir()
            self.transiciones += f'Instrucciones{self.count_instrucciones - 1} -> Instrucciones{self.count_instrucciones}\n'
            self.lista_instrucciones()
        elif self.list_tokens[self.count].lexema.lower().lower() == 'imprimirln':
            self.count_instrucciones += 1
            self.count_instruccion += 1
            self.nodos += f'Instrucciones{self.count_instrucciones} [label="Instrucciones"];\n'
            self.nodos += f'Instruccion{self.count_instruccion} [label="Instruccion"];\n'
            self.nodos += f'ProcesoImprimirln{self.count_proceso} [label="ProcesoImprimirln"];\n'
            self.transiciones += f'Instrucciones{self.count_instrucciones - 1} -> Instruccion{self.count_instruccion}\n'
            self.transiciones += f'Instruccion{self.count_instruccion} -> ProcesoImprimirln{self.count_proceso}\n'
            self.instrucciones_imprimirln()
            self.transiciones += f'Instrucciones{self.count_instrucciones - 1} -> Instrucciones{self.count_instrucciones}\n'
            self.lista_instrucciones()
        elif self.list_tokens[self.count].lexema.lower().lower() == 'datos':
            self.count_instrucciones += 1
            self.count_instruccion += 1
            self.nodos += f'Instrucciones{self.count_instrucciones} [label="Instrucciones"];\n'
            self.nodos += f'Instruccion{self.count_instruccion} [label="Instruccion"];\n'
            self.nodos += f'ProcesoDatos{self.count_proceso} [label="ProcesoDatos"];\n'
            self.transiciones += f'Instrucciones{self.count_instrucciones - 1} -> Instruccion{self.count_instruccion}\n'
            self.transiciones += f'Instruccion{self.count_instruccion} -> ProcesoDatos{self.count_proceso}\n'
            self.instrucciones_datos()
            self.transiciones += f'Instrucciones{self.count_instrucciones - 1} -> Instrucciones{self.count_instrucciones}\n'
            self.lista_instrucciones()
        elif self.list_tokens[self.count].lexema.lower().lower() == 'conteo':
            self.count_instrucciones += 1
            self.count_instruccion += 1
            self.nodos += f'Instrucciones{self.count_instrucciones} [label="Instrucciones"];\n'
            self.nodos += f'Instruccion{self.count_instruccion} [label="Instruccion"];\n'
            self.nodos += f'ProcesoConteo{self.count_proceso} [label="ProcesoConteo"];\n'
            self.transiciones += f'Instrucciones{self.count_instrucciones - 1} -> Instruccion{self.count_instruccion}\n'
            self.transiciones += f'Instruccion{self.count_instruccion} -> ProcesoConteo{self.count_proceso}\n'
            self.instrucciones_conteo()
            self.transiciones += f'Instrucciones{self.count_instrucciones - 1} -> Instrucciones{self.count_instrucciones}\n'
            self.lista_instrucciones()
        elif self.list_tokens[self.count].lexema.lower().lower() == 'promedio':
            self.count_instrucciones += 1
            self.count_instruccion += 1
            self.nodos += f'Instrucciones{self.count_instrucciones} [label="Instrucciones"];\n'
            self.nodos += f'Instruccion{self.count_instruccion} [label="Instruccion"];\n'
            self.nodos += f'ProcesoPromedio{self.count_proceso} [label="ProcesoPromedio"];\n'
            self.transiciones += f'Instrucciones{self.count_instrucciones - 1} -> Instruccion{self.count_instruccion}\n'
            self.transiciones += f'Instruccion{self.count_instruccion} -> ProcesoPromedio{self.count_proceso}\n'
            self.instrucciones_promedio()
            self.transiciones += f'Instrucciones{self.count_instrucciones - 1} -> Instrucciones{self.count_instrucciones}\n'
            self.lista_instrucciones()
        elif self.list_tokens[self.count].lexema.lower().lower() == 'contarsi':
            self.count_instrucciones += 1
            self.count_instruccion += 1
            self.nodos += f'Instrucciones{self.count_instrucciones} [label="Instrucciones"];\n'
            self.nodos += f'Instruccion{self.count_instruccion} [label="Instruccion"];\n'
            self.nodos += f'ProcesoContarSi{self.count_proceso} [label="ProcesoContarSi"];\n'
            self.transiciones += f'Instrucciones{self.count_instrucciones - 1} -> Instruccion{self.count_instruccion}\n'
            self.transiciones += f'Instruccion{self.count_instruccion} -> ProcesoContarSi{self.count_proceso}\n'
            self.instrucciones_contarsi()
            self.transiciones += f'Instrucciones{self.count_instrucciones - 1} -> Instrucciones{self.count_instrucciones}\n'
            self.lista_instrucciones()
        elif self.list_tokens[self.count].lexema.lower().lower() == 'sumar':
            self.count_instrucciones += 1
            self.count_instruccion += 1
            self.nodos += f'Instrucciones{self.count_instrucciones} [label="Instrucciones"];\n'
            self.nodos += f'Instruccion{self.count_instruccion} [label="Instruccion"];\n'
            self.nodos += f'ProcesoSumar{self.count_proceso} [label="ProcesoSumar"];\n'
            self.transiciones += f'Instrucciones{self.count_instrucciones - 1} -> Instruccion{self.count_instruccion}\n'
            self.transiciones += f'Instruccion{self.count_instruccion} -> ProcesoSumar{self.count_proceso}\n'
            self.instrucciones_sumar()
            self.transiciones += f'Instrucciones{self.count_instrucciones - 1} -> Instrucciones{self.count_instrucciones}\n'
            self.lista_instrucciones()
        elif self.list_tokens[self.count].lexema.lower().lower() == 'max':
            self.count_instrucciones += 1
            self.count_instruccion += 1
            self.nodos += f'Instrucciones{self.count_instrucciones} [label="Instrucciones"];\n'
            self.nodos += f'Instruccion{self.count_instruccion} [label="Instruccion"];\n'
            self.nodos += f'ProcesoMax{self.count_proceso} [label="ProcesoMax"];\n'
            self.transiciones += f'Instrucciones{self.count_instrucciones - 1} -> Instruccion{self.count_instruccion}\n'
            self.transiciones += f'Instruccion{self.count_instruccion} -> ProcesoMax{self.count_proceso}\n'
            self.instrucciones_max()
            self.transiciones += f'Instrucciones{self.count_instrucciones - 1} -> Instrucciones{self.count_instrucciones}\n'
            self.lista_instrucciones()
        elif self.list_tokens[self.count].lexema.lower().lower() == 'min':
            self.count_instrucciones += 1
            self.count_instruccion += 1
            self.nodos += f'Instrucciones{self.count_instrucciones} [label="Instrucciones"];\n'
            self.nodos += f'Instruccion{self.count_instruccion} [label="Instruccion"];\n'
            self.nodos += f'ProcesoMin{self.count_proceso} [label="ProcesoMin"];\n'
            self.transiciones += f'Instrucciones{self.count_instrucciones - 1} -> Instruccion{self.count_instruccion}\n'
            self.transiciones += f'Instruccion{self.count_instruccion} -> ProcesoMin{self.count_proceso}\n'
            self.instrucciones_min()
            self.transiciones += f'Instrucciones{self.count_instrucciones - 1} -> Instrucciones{self.count_instrucciones}\n'
            self.lista_instrucciones()
        elif self.list_tokens[self.count].lexema.lower().lower() == 'exportarreporte':
            self.count_instrucciones += 1
            self.count_instruccion += 1
            self.nodos += f'Instrucciones{self.count_instrucciones} [label="Instrucciones"];\n'
            self.nodos += f'Instruccion{self.count_instruccion} [label="Instruccion"];\n'
            self.nodos += f'ProcesoExportar{self.count_proceso} [label="ProcesoExportar"];\n'
            self.transiciones += f'Instrucciones{self.count_instrucciones - 1} -> Instruccion{self.count_instruccion}\n'
            self.transiciones += f'Instruccion{self.count_instruccion} -> ProcesoExportar{self.count_proceso}\n'
            self.instrucciones_exportar()
            self.transiciones += f'Instrucciones{self.count_instrucciones - 1} -> Instrucciones{self.count_instrucciones}\n'
            self.lista_instrucciones()
    
    # ExportarReporte
    def instrucciones_exportar(self):
        if self.list_tokens[self.count].lexema.lower().lower() == 'exportarreporte':
            self.nodos += f'TokenExportar{self.count_token} [label="TokenExportar"];\n'
            self.nodos += f'Exportar{self.count_token} [label="exportarReporte", color="#bcf9eb"];\n'
            self.transiciones += f'ProcesoExportar{self.count_proceso} -> TokenExportar{self.count_token} -> Exportar{self.count_token}\n'
            self.count += 1
            if self.list_tokens[self.count].lexema.lower() == 'parentesis abierto':
                self.nodos += f'SimboloParentesisAbierto{self.count_parentesis} [label="ParentesisAbierto"];\n'
                self.nodos += f'ParentesisAbierto{self.count_parentesis} [label="(", color="#bcf9eb"];\n'
                self.transiciones += f'ProcesoExportar{self.count_proceso} -> SimboloParentesisAbierto{self.count_parentesis} -> ParentesisAbierto{self.count_parentesis}\n'
                self.count_parentesis += 1
                self.count += 1
                if self.list_tokens[self.count].lexema.lower() == 'comillas dobles':
                    self.count += 1
                    if self.list_tokens[self.count].lexema.lower() == 'cadena':
                        texto = self.list_tokens[self.count].char
                        self.nodos += f'Cadena{self.count_cadena} [label="Cadena"];\n'
                        self.nodos += f'Cadena_Text{self.count_cadena} [label="{texto}", color="#bcf9eb"];\n'
                        self.transiciones += f'ProcesoExportar{self.count_proceso} -> Cadena{self.count_cadena} -> Cadena_Text{self.count_cadena}\n'
                        self.count_cadena += 1
                        self.count += 1
                        if self.list_tokens[self.count].lexema.lower() == 'comillas dobles':
                            self.count += 1
                            if self.list_tokens[self.count].lexema.lower() == 'parentesis cerrado':
                                self.nodos += f'SimboloParentesisCerrado{self.count_parentesis} [label="ParentesisCerrado"];\n'
                                self.nodos += f'ParentesisCerrado{self.count_parentesis} [label=")", color="#bcf9eb"];\n'
                                self.transiciones += f'ProcesoExportar{self.count_proceso} -> SimboloParentesisCerrado{self.count_parentesis} -> ParentesisCerrado{self.count_parentesis}\n'
                                self.count_parentesis += 1
                                self.count += 1
                                if self.list_tokens[self.count].lexema.lower() == 'punto y coma':
                                    self.nodos += f'SimboloPuntoyComa{self.count_igual} [label="PuntoyComa"];\n'
                                    self.nodos += f'PuntoyComa{self.count_igual} [label=";", color="#bcf9eb"];\n'
                                    self.transiciones += f'ProcesoExportar{self.count_proceso} -> SimboloPuntoyComa{self.count_igual} -> PuntoyComa{self.count_igual}\n'
                                    self.count_igual += 1
                                    self.count += 1
                                    self.console += '\n--> Exportando...\n'
                                    self.exportar_reporte(texto)
                                    self.count_imprimir = 1
                                else:
                                    error = 'Error sintactico ";"'
                                    self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                            else:
                                error = 'Error sintactico ")"'
                                self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                                self.count += 1
                        else:
                            error = 'Error sintactico "comillas dobles"'
                            self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                    else:
                        error = 'Error sintactico "cadena"'
                        self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                        self.count += 3
                else:
                    error = 'Error sintactico "comillas dobles"'
                    self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
            else:
                error = 'Error sintactico "("'
                self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                self.count += 5
        else:
            error = 'Error sintactico "exportarReporte"'
            self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
        self.count_token += 1       
        self.count_proceso += 1                 
    
    def exportar_reporte(self, title):
        th_head = ''
        t_body = ''
        for clave in self.list_claves:
            th_head += f'<th>{clave}</th>\n'
        
        for registro in self.list_registros:
            t_body += '<tr>\n'
            for valor in registro:
                t_body += f'<td> {valor} </td>\n'
            t_body += '</tr>\n'
        
        html_contenido = f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <title>{title}</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="stylesheet" type="text/css" href="./css/styles.css">
        </head>
        <body>
            <div class="container">
                <h1>{title}</h1>
                <table>
                    <thead>
                        <tr>
                            {th_head}
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
        with open(f'./report/Reporte_{title}.html', 'w', encoding='UTF-8') as file:
            file.write(html_contenido)
            file.close()
    # FIN ExportarReporte
    
    # Min
    def instrucciones_min(self):
        if self.list_tokens[self.count].lexema.lower() == 'min':
            self.nodos += f'TokenMin{self.count_token} [label="TokenMin"];\n'
            self.nodos += f'Min{self.count_token} [label="min", color="#bcf9eb"];\n'
            self.transiciones += f'ProcesoMin{self.count_proceso} -> TokenMin{self.count_token} -> Min{self.count_token}\n'
            self.count += 1
            if self.list_tokens[self.count].lexema.lower() == 'parentesis abierto':
                self.nodos += f'SimboloParentesisAbierto{self.count_parentesis} [label="ParentesisAbierto"];\n'
                self.nodos += f'ParentesisAbierto{self.count_parentesis} [label="(", color="#bcf9eb"];\n'
                self.transiciones += f'ProcesoMin{self.count_proceso} -> SimboloParentesisAbierto{self.count_parentesis} -> ParentesisAbierto{self.count_parentesis}\n'
                self.count_parentesis += 1
                self.count += 1
                if self.list_tokens[self.count].lexema.lower() == 'comillas dobles':
                    self.count += 1
                    if self.list_tokens[self.count].lexema.lower() == 'cadena':
                        texto = self.list_tokens[self.count].char
                        self.nodos += f'Cadena{self.count_cadena} [label="Cadena"];\n'
                        self.nodos += f'Cadena_Text{self.count_cadena} [label="{texto}", color="#bcf9eb"];\n'
                        self.transiciones += f'ProcesoMin{self.count_proceso} -> Cadena{self.count_cadena} -> Cadena_Text{self.count_cadena}\n'
                        self.count_cadena += 1
                        self.count += 1
                        if self.list_tokens[self.count].lexema.lower() == 'comillas dobles':
                            self.count += 1
                            if self.list_tokens[self.count].lexema.lower() == 'parentesis cerrado':
                                self.nodos += f'SimboloParentesisCerrado{self.count_parentesis} [label="ParentesisCerrado"];\n'
                                self.nodos += f'ParentesisCerrado{self.count_parentesis} [label=")", color="#bcf9eb"];\n'
                                self.transiciones += f'ProcesoMin{self.count_proceso} -> SimboloParentesisCerrado{self.count_parentesis} -> ParentesisCerrado{self.count_parentesis}\n'
                                self.count_parentesis += 1
                                self.count += 1
                                if self.list_tokens[self.count].lexema.lower() == 'punto y coma':
                                    self.nodos += f'SimboloPuntoyComa{self.count_igual} [label="PuntoyComa"];\n'
                                    self.nodos += f'PuntoyComa{self.count_igual} [label=";", color="#bcf9eb"];\n'
                                    self.transiciones += f'ProcesoMin{self.count_proceso} -> SimboloPuntoyComa{self.count_igual} -> PuntoyComa{self.count_igual}\n'
                                    self.count_igual += 1
                                    self.count += 1
                                    for i, clave in enumerate(self.list_claves):
                                        if clave == texto:
                                            posicion = i
                                            minimo = self.calcular_min(posicion) 
                                            break
                                        else:
                                            minimo = 'No existe la clave'
                                    self.console += f'\n--> {minimo}'
                                    self.nodos += f'ValorMin{self.count_value} [label="{minimo}", color="#bcf9eb"];\n'
                                    self.transiciones += f'Min{self.count_token} -> ValorMin{self.count_value}\n'
                                    self.count_imprimir = 1
                                    self.count_value += 1
                                else:
                                    error = 'Error sintactico ";"'
                                    self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                            else:
                                error = 'Error sintactico ")"'
                                self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                                self.count += 1
                        else:
                            error = 'Error sintactico "comillas dobles"'
                            self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                    else:
                        error = 'Error sintactico "cadena"'
                        self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                        self.count += 3
                else:
                    error = 'Error sintactico "comillas dobles"'
                    self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
            else:
                error = 'Error sintactico "("'
                self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                self.count += 5
        else:
            error = 'Error sintactico "min"'
            self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
        self.count_token += 1
        self.count_proceso += 1
    
    def calcular_min(self, posicion):
        try:
            minimo = float(self.list_registros[0][posicion])
            for registro in self.list_registros:
                if float(registro[posicion]) < minimo:
                    minimo = float(registro[posicion])
            return minimo
        except ValueError:
            return 'Error al calcular minimo'
    #FIN Min
    
    # Max
    def instrucciones_max(self):
        if self.list_tokens[self.count].lexema.lower() == 'max':
            self.nodos += f'TokenMax{self.count_token} [label="TokenMax"];\n'
            self.nodos += f'Max{self.count_token} [label="max", color="#bcf9eb"];\n'
            self.transiciones += f'ProcesoMax{self.count_proceso} -> TokenMax{self.count_token} -> Max{self.count_token}\n'
            self.count += 1
            if self.list_tokens[self.count].lexema.lower() == 'parentesis abierto':
                self.nodos += f'SimboloParentesisAbierto{self.count_parentesis} [label="ParentesisAbierto"];\n'
                self.nodos += f'ParentesisAbierto{self.count_parentesis} [label="(", color="#bcf9eb"];\n'
                self.transiciones += f'ProcesoMax{self.count_proceso} -> SimboloParentesisAbierto{self.count_parentesis} -> ParentesisAbierto{self.count_parentesis}\n'
                self.count_parentesis += 1
                self.count += 1
                if self.list_tokens[self.count].lexema.lower() == 'comillas dobles':
                    self.count += 1
                    if self.list_tokens[self.count].lexema.lower() == 'cadena':
                        texto = self.list_tokens[self.count].char
                        self.nodos += f'Cadena{self.count_cadena} [label="Cadena"];\n'
                        self.nodos += f'Cadena_Text{self.count_cadena} [label="{texto}", color="#bcf9eb"];\n'
                        self.transiciones += f'ProcesoMax{self.count_proceso} -> Cadena{self.count_cadena} -> Cadena_Text{self.count_cadena}\n'
                        self.count_cadena += 1
                        self.count += 1
                        if self.list_tokens[self.count].lexema.lower() == 'comillas dobles':
                            self.count += 1
                            if self.list_tokens[self.count].lexema.lower() == 'parentesis cerrado':
                                self.nodos += f'SimboloParentesisCerrado{self.count_parentesis} [label="ParentesisCerrado"];\n'
                                self.nodos += f'ParentesisCerrado{self.count_parentesis} [label=")", color="#bcf9eb"];\n'
                                self.transiciones += f'ProcesoMax{self.count_proceso} -> SimboloParentesisCerrado{self.count_parentesis} -> ParentesisCerrado{self.count_parentesis}\n'
                                self.count_parentesis += 1
                                self.count += 1
                                if self.list_tokens[self.count].lexema.lower() == 'punto y coma':
                                    self.nodos += f'SimboloPuntoyComa{self.count_igual} [label="PuntoyComa"];\n'
                                    self.nodos += f'PuntoyComa{self.count_igual} [label=";", color="#bcf9eb"];\n'
                                    self.transiciones += f'ProcesoMax{self.count_proceso} -> SimboloPuntoyComa{self.count_igual} -> PuntoyComa{self.count_igual}\n'
                                    self.count_igual += 1
                                    self.count += 1
                                    for i, clave in enumerate(self.list_claves):
                                        if clave == texto:
                                            posicion = i
                                            maximo = self.calcular_max(posicion) 
                                            break
                                        else:
                                            maximo = 'No existe la clave'
                                    self.console += f'\n--> {maximo}'
                                    self.nodos += f'ValorMax{self.count_value} [label="{maximo}", color="#bcf9eb"];\n'
                                    self.transiciones += f'Max{self.count_token} -> ValorMax{self.count_value}\n'
                                    self.count_imprimir = 1
                                    
                                else:
                                    error = 'Error sintactico ";"'
                                    self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                            else:
                                error = 'Error sintactico ")"'
                                self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                                self.count += 1
                        else:
                            error = 'Error sintactico "comillas dobles"'
                            self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                    else:
                        error = 'Error sintactico "cadena"'
                        self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                        self.count += 3
                else:
                    error = 'Error sintactico "comillas dobles"'
                    self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
            else:
                error = 'Error sintactico "("'
                self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                self.count += 5
        else:
            error = 'Error sintactico "max"'
            self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
        self.count_token += 1
        self.count_proceso += 1
    
    def calcular_max(self, posicion):
        try:
            maximo = 0
            for registro in self.list_registros:
                if float(registro[posicion]) > maximo:
                    maximo = float(registro[posicion])
            return maximo
        except ValueError:
            return 'Error al calcular maximo'
    # FIN Max    
    
    # Sumar
    def instrucciones_sumar(self):
        if self.list_tokens[self.count].lexema.lower() == 'sumar':
            self.nodos += f'TokenSumar{self.count_token} [label="TokenSumar"];\n'
            self.nodos += f'Sumar{self.count_token} [label="sumar", color="#bcf9eb"];\n'
            self.transiciones += f'ProcesoSumar{self.count_proceso} -> TokenSumar{self.count_token} -> Sumar{self.count_token}\n'
            self.count += 1
            if self.list_tokens[self.count].lexema.lower() == 'parentesis abierto':
                self.nodos += f'SimboloParentesisAbierto{self.count_parentesis} [label="ParentesisAbierto"];\n'
                self.nodos += f'ParentesisAbierto{self.count_parentesis} [label="(", color="#bcf9eb"];\n'
                self.transiciones += f'ProcesoSumar{self.count_proceso} -> SimboloParentesisAbierto{self.count_parentesis} -> ParentesisAbierto{self.count_parentesis}\n'
                self.count_parentesis += 1
                self.count += 1
                if self.list_tokens[self.count].lexema.lower() == 'comillas dobles':
                    self.count += 1
                    if self.list_tokens[self.count].lexema.lower() == 'cadena':
                        cadena = self.list_tokens[self.count].char
                        self.nodos += f'Cadena{self.count_cadena} [label="Cadena"];\n'
                        self.nodos += f'Cadena_Text{self.count_cadena} [label="{cadena}", color="#bcf9eb"];\n'
                        self.transiciones += f'ProcesoSumar{self.count_proceso} -> Cadena{self.count_cadena} -> Cadena_Text{self.count_cadena}\n'
                        self.count_cadena += 1
                        self.count += 1
                        if self.list_tokens[self.count].lexema.lower() == 'comillas dobles':
                            self.count += 1
                            if self.list_tokens[self.count].lexema.lower() == 'parentesis cerrado':
                                self.nodos += f'SimboloParentesisCerrado{self.count_parentesis} [label="ParentesisCerrado"];\n'
                                self.nodos += f'ParentesisCerrado{self.count_parentesis} [label=")", color="#bcf9eb"];\n'
                                self.transiciones += f'ProcesoSumar{self.count_proceso} -> SimboloParentesisCerrado{self.count_parentesis} -> ParentesisCerrado{self.count_parentesis}\n'
                                self.count_parentesis += 1
                                self.count += 1
                                if self.list_tokens[self.count].lexema.lower() == 'punto y coma':
                                    self.nodos += f'SimboloPuntoyComa{self.count_igual} [label="PuntoyComa"];\n'
                                    self.nodos += f'PuntoyComa{self.count_igual} [label=";", color="#bcf9eb"];\n'
                                    self.transiciones += f'ProcesoSumar{self.count_proceso} -> SimboloPuntoyComa{self.count_igual} -> PuntoyComa{self.count_igual}\n'
                                    self.count_igual += 1
                                    self.count += 1
                                    for i, clave in enumerate(self.list_claves):
                                        if clave == cadena:
                                            posicion = i
                                            suma = self.calcular_sumar(posicion) 
                                            break
                                        else:
                                            suma = 'No existe la clave'
                                    self.console += f'\n--> {suma}'
                                    self.nodos += f'ValorSumar{self.count_value} [label="{suma}", color="#bcf9eb"];\n'
                                    self.transiciones += f'Sumar{self.count_token} -> ValorSumar{self.count_value}\n'
                                    self.count_value += 1
                                else:
                                    error = 'Error sintactico ";"'
                                    self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                            else:
                                error = 'Error sintactico ")"'
                                self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                                self.count += 1
                        else:
                            error = 'Error sintactico "comillas dobles"'
                            self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                    else:
                        error = 'Error sintactico "cadena"'
                        self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                        self.count += 3
                else:
                    error = 'Error sintactico "comillas dobles"'
                    self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
            else:
                error = 'Error sintactico "("'
                self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                self.count += 5
        else:
            error = 'Error sintactico "sumar"'
            self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
        self.count_token += 1
        self.count_proceso += 1
        
    def calcular_sumar(self, posicion):
        try:
            suma = 0
            for registro in self.list_registros:
                suma += float(registro[posicion])
            return suma
        except ValueError:
            return 'La clave no es un valor númerico'
    #FIN Sumar
    
    # Contarsi
    def instrucciones_contarsi(self):
        if self.list_tokens[self.count].lexema.lower() == 'contarsi':
            self.count += 1
            self.nodos += f'TokenContarsi{self.count_token} [label="TokenContarsi"];\n'
            self.nodos += f'ContarSi{self.count_token} [label="contarsi", color="#bcf9eb"];\n'
            self.transiciones += f'ProcesoContarSi{self.count_proceso} -> TokenContarsi{self.count_token} -> ContarSi{self.count_token}\n'
            if self.list_tokens[self.count].lexema.lower() == 'parentesis abierto':
                self.nodos += f'SimboloParentesisAbierto{self.count_parentesis} [label="ParentesisAbierto"];\n'
                self.nodos += f'ParentesisAbierto{self.count_parentesis} [label="(", color="#bcf9eb"];\n'
                self.transiciones += f'ProcesoContarSi{self.count_proceso} -> SimboloParentesisAbierto{self.count_parentesis} -> ParentesisAbierto{self.count_parentesis}\n'
                self.count_parentesis += 1
                self.count += 1
                if self.list_tokens[self.count].lexema.lower() == 'comillas dobles':
                    self.count += 1
                    if self.list_tokens[self.count].lexema.lower() == 'cadena':
                        cadena = self.list_tokens[self.count].char
                        self.nodos += f'Cadena{self.count_cadena} [label="Cadena"];\n'
                        self.nodos += f'Cadena_Text{self.count_cadena} [label="{cadena}", color="#bcf9eb"];\n'
                        self.transiciones += f'ProcesoContarSi{self.count_proceso} -> Cadena{self.count_cadena} -> Cadena_Text{self.count_cadena}\n'
                        self.count_cadena += 1
                        self.count += 1
                        if self.list_tokens[self.count].lexema.lower() == 'comillas dobles':
                            self.count += 1
                            if self.list_tokens[self.count].lexema.lower() == 'coma':
                                self.nodos += f'SimboloComa{self.count_coma} [label="Coma"];\n'
                                self.nodos += f'Coma{self.count_coma} [label=",", color="#bcf9eb"];\n'
                                self.transiciones += f'ProcesoContarSi{self.count_proceso} -> SimboloComa{self.count_coma} -> Coma{self.count_coma}\n'
                                self.count_coma += 1
                                self.count += 1
                                if self.list_tokens[self.count].lexema.lower() == 'entero' or self.list_tokens[self.count].lexema.lower() == 'decimal':
                                    entero = self.list_tokens[self.count].char
                                    self.nodos += f'Entero{self.count_entero} [label="Numero"];\n'
                                    self.nodos += f'Entero_Text{self.count_entero} [label="{entero}", color="#bcf9eb"];\n'
                                    self.transiciones += f'ProcesoContarSi{self.count_proceso} -> Entero{self.count_entero} -> Entero_Text{self.count_entero}\n'
                                    self.count += 1
                                    self.count_entero += 1
                                    if self.list_tokens[self.count].lexema.lower() == 'parentesis cerrado':
                                        self.nodos += f'SimboloParentesisCerrado{self.count_parentesis} [label="ParentesisCerrado"];\n'
                                        self.nodos += f'ParentesisCerrado{self.count_parentesis} [label=")", color="#bcf9eb"];\n'
                                        self.transiciones += f'ProcesoContarSi{self.count_proceso} -> SimboloParentesisCerrado{self.count_parentesis} -> ParentesisCerrado{self.count_parentesis}\n'
                                        self.count_parentesis += 1
                                        self.count += 1
                                        if self.list_tokens[self.count].lexema.lower() == 'punto y coma':
                                            self.nodos += f'SimboloPuntoyComa{self.count_igual} [label="PuntoyComa"];\n'
                                            self.nodos += f'PuntoyComa{self.count_igual} [label=";", color="#bcf9eb"];\n'
                                            self.transiciones += f'ProcesoContarSi{self.count_proceso} -> SimboloPuntoyComa{self.count_igual} -> PuntoyComa{self.count_igual}\n'
                                            self.count_igual += 1
                                            self.count += 1
                                            for i, clave in enumerate(self.list_claves):
                                                if clave == cadena:
                                                    posicion = i
                                                    valor_count = self.calcular_contar_si(posicion, entero)
                                                    self.console += f'\n--> {valor_count}'
                                                    self.count_imprimir = 1
                                                else:
                                                    valor_count = 'No existe la clave' 
                                            self.nodos += f'ValorContarSi{self.count_value} [label="{valor_count}", color="#bcf9eb"];\n'
                                            self.transiciones += f'ContarSi{self.count_token} -> ValorContarSi{self.count_value}\n'
                                            self.count_value += 1
                                        else:
                                            error = 'Error sintactico ";"'
                                            self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                                    else:
                                        error = 'Error sintactico ")"'
                                        self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                                        self.count += 1
                                elif self.list_tokens[self.count].lexema.lower() == 'comillas dobles':
                                    self.count += 1
                                    if self.list_tokens[self.count].lexema.lower() == 'cadena':
                                        valor = self.list_tokens[self.count].char
                                        self.nodos += f'Cadena{self.count_cadena} [label="Cadena"];\n'
                                        self.nodos += f'Cadena_Text{self.count_cadena} [label="{valor}", color="#bcf9eb"];\n'
                                        self.transiciones += f'ProcesoContarSi{self.count_proceso} -> Cadena{self.count_cadena} -> Cadena_Text{self.count_cadena}\n'
                                        self.count_cadena += 1
                                        self.count += 1
                                        if self.list_tokens[self.count].lexema.lower() == 'comillas dobles':
                                            self.count += 1
                                            if self.list_tokens[self.count].lexema.lower() == 'parentesis cerrado':
                                                self.nodos += f'SimboloParentesisCerrado{self.count_parentesis} [label="ParentesisCerrado"];\n'
                                                self.nodos += f'ParentesisCerrado{self.count_parentesis} [label=")", color="#bcf9eb"];\n'
                                                self.transiciones += f'ProcesoContarSi{self.count_proceso} -> SimboloParentesisCerrado{self.count_parentesis} -> ParentesisCerrado{self.count_parentesis}\n'
                                                self.count_parentesis += 1
                                                self.count += 1
                                                if self.list_tokens[self.count].lexema.lower() == 'punto y coma':
                                                    self.nodos += f'SimboloPuntoyComa{self.count_igual} [label="PuntoyComa"];\n'
                                                    self.nodos += f'PuntoyComa{self.count_igual} [label=";", color="#bcf9eb"];\n'
                                                    self.transiciones += f'ProcesoContarSi{self.count_proceso} -> SimboloPuntoyComa{self.count_igual} -> PuntoyComa{self.count_igual}\n'
                                                    self.count_igual += 1
                                                    self.count += 1
                                                    for i, clave in enumerate(self.list_claves):
                                                        if clave == cadena:
                                                            posicion = i
                                                            valor_count = self.calcular_contar_si(posicion, valor)
                                                            self.console += f'\n--> {valor_count}'
                                                            self.count_imprimir = 1
                                                        else:
                                                            valor_count = 'No existe la clave' 
                                                    self.nodos += f'ValorContarSi{self.count_value} [label="{valor_count}", color="#bcf9eb"];\n'
                                                    self.transiciones += f'ContarSi{self.count_token} -> ValorContarSi{self.count_value}\n'
                                                    self.count_value += 1
                                                else:
                                                    error = 'Error sintactico ";"'
                                                    self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                                            else:
                                                error = 'Error sintactico ")"'
                                                self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                                                self.count += 1
                                        else:
                                            error = 'Error sintactico "comillas dobles"'
                                            self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                                    else:
                                        error = 'Error sintactico "cadena"'
                                        self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                                        self.count += 3
                                else:
                                    error = 'Error sintactico "entero o comillas dobles"'
                                    self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                                    self.count += 2
                            else:
                                error = 'Error sintactico ","'
                                self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                                self.count += 3
                        else:
                            error = 'Error sintactico "comillas dobles"'
                            self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                    else:
                        error = 'Error sintactico "cadena"'
                        self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                        self.count += 5
                else:
                    error = 'Error sintactico "comillas dobles"'
                    self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
            else:
                error = 'Error sintactico "("'
                self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                self.count += 7
        else:
            error = 'Error sintactico "contarsi"'
            self.list_errors.append(Error(error, 'Error semantico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))                            
        self.count_token += 1
        self.count_proceso += 1                
    
    def calcular_contar_si(self, posicion, valor):
        count = 0
        for registro in self.list_registros:
            if registro[posicion] == valor:
                count += 1
        return count
    # FIN Contarsi
    
    # Promedio
    def instrucciones_promedio(self):
        if self.list_tokens[self.count].lexema.lower() == 'promedio':
            self.nodos += f'TokenPromedio{self.count_token} [label="TokenPromedio"];\n'
            self.nodos += f'Promedio{self.count_token} [label="promedio", color="#bcf9eb"];\n'
            self.transiciones += f'ProcesoPromedio{self.count_proceso} -> TokenPromedio{self.count_token} -> Promedio{self.count_token}\n'
            self.count += 1
            if self.list_tokens[self.count].lexema.lower() == 'parentesis abierto':
                self.nodos += f'SimboloParentesisAbierto{self.count_parentesis} [label="ParentesisAbierto"];\n'
                self.nodos += f'ParentesisAbierto{self.count_parentesis} [label="(", color="#bcf9eb"];\n'
                self.transiciones += f'ProcesoPromedio{self.count_proceso} -> SimboloParentesisAbierto{self.count_parentesis} -> ParentesisAbierto{self.count_parentesis}\n'
                self.count_parentesis += 1
                self.count += 1
                if self.list_tokens[self.count].lexema.lower() == 'comillas dobles':
                    self.count += 1
                    if self.list_tokens[self.count].lexema.lower() == 'cadena':
                        head = self.list_tokens[self.count].char    
                        self.nodos += f'Cadena{self.count_cadena} [label="Cadena"];\n'         
                        self.nodos += f'Cadena_Text{self.count_cadena} [label="{head}", color="#bcf9eb"];\n'
                        self.transiciones += f'ProcesoPromedio{self.count_proceso} -> Cadena{self.count_cadena} -> Cadena_Text{self.count_cadena}\n'
                        self.count_cadena += 1
                        self.count += 1
                        if self.list_tokens[self.count].lexema.lower() == 'comillas dobles':
                            self.count += 1
                            if self.list_tokens[self.count].lexema.lower() == 'parentesis cerrado':
                                self.nodos += f'SimboloParentesisCerrado{self.count_parentesis} [label="ParentesisCerrado"];\n'
                                self.nodos += f'ParentesisCerrado{self.count_parentesis} [label=")", color="#bcf9eb"];\n'
                                self.transiciones += f'ProcesoPromedio{self.count_proceso} -> SimboloParentesisCerrado{self.count_parentesis} -> ParentesisCerrado{self.count_parentesis}\n'
                                self.count_parentesis += 1
                                self.count += 1
                                if self.list_tokens[self.count].lexema.lower() == 'punto y coma':
                                    self.nodos += f'SimboloPuntoyComa{self.count_igual} [label="PuntoyComa"];\n'
                                    self.nodos += f'PuntoyComa{self.count_igual} [label=";", color="#bcf9eb"];\n'
                                    self.transiciones += f'ProcesoPromedio{self.count_proceso} -> SimboloPuntoyComa{self.count_igual} -> PuntoyComa{self.count_igual}\n'
                                    self.count_igual += 1
                                    self.count += 1
                                    for i in range(len(self.list_registros)):
                                        if self.list_claves[i] == head:
                                            posicion = i
                                            promedio = self.calcular_promedio(posicion)
                                            break
                                        else:
                                            promedio = 'No existe la clave'
                                    self.nodos += f'Promedio_Texto{self.count_decimal} [label="{promedio}", color="#bcf9eb"];\n'
                                    self.transiciones += f'Promedio{self.count_token} -> Promedio_Texto{self.count_decimal}\n'
                                    self.count_decimal += 1
                                    self.count_token += 1
                                    self.console += f'\n--> {promedio}'
                                    self.count_imprimir = 1
                                else:
                                    error = 'Error sintactico ";"'
                                    self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                            else:
                                error = 'Error sintactico ")"'
                                self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                                self.count += 1
                        else:
                            error = 'Error sintactico "comillas dobles"'
                            self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                    else:
                        error = 'Error sintactico "cadena"'
                        self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                        self.count += 3
                else:
                    error = 'Error sintactico "comillas dobles"'
                    self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
            else:
                error = 'Error sintactico "("'
                self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                self.count += 5
        else:
            error = 'Error sintactico "promedio"'
            self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
        self.count_token += 1
        self.count_proceso += 1
        
    def calcular_promedio(self, posicion):
        try:
            suma = 0
            total_registros = len(self.list_registros)
            for registro in self.list_registros:
                suma += float(registro[posicion])
            promedio = suma / total_registros
            return promedio
        except ValueError:
            return 'El valor no es númerico'
    # FIN Promedio
    
    # Datos
    def instrucciones_datos(self):
        if self.list_tokens[self.count].lexema.lower() == 'datos':
            self.nodos += f'TokenDatos{self.count_token} [label="TokenDatos"];\n'
            self.nodos += f'Datos{self.count_token} [label="datos", color="#bcf9eb"];\n'
            self.transiciones += f'ProcesoDatos{self.count_proceso} -> TokenDatos{self.count_token} -> Datos{self.count_token}\n'
            self.count += 1
            if self.list_tokens[self.count].lexema.lower() == 'parentesis abierto':
                self.nodos += f'SimboloParentesisAbierto{self.count_parentesis} [label="ParentesisAbierto"];\n'
                self.nodos += f'ParentesisAbierto{self.count_parentesis} [label="(", color="#bcf9eb"];\n'
                self.transiciones += f'ProcesoDatos{self.count_proceso} -> SimboloParentesisAbierto{self.count_parentesis} -> ParentesisAbierto{self.count_parentesis}\n'
                self.count_parentesis += 1
                self.count += 1
                if self.list_tokens[self.count].lexema.lower() == 'parentesis cerrado':
                    self.nodos += f'SimboloParentesisCerrado{self.count_parentesis} [label="ParentesisCerrado"];\n'
                    self.nodos += f'ParentesisCerrado{self.count_parentesis} [label=")", color="#bcf9eb"];\n'
                    self.transiciones += f'ProcesoDatos{self.count_proceso} -> SimboloParentesisCerrado{self.count_parentesis} -> ParentesisCerrado{self.count_parentesis}\n'
                    self.count_parentesis += 1
                    self.count += 1
                    if self.list_tokens[self.count].lexema.lower() == 'punto y coma':
                        self.nodos += f'SimboloPuntoyComa{self.count_igual} [label="PuntoyComa"];\n'
                        self.nodos += f'PuntoyComa{self.count_igual} [label=";", color="#bcf9eb"];\n'
                        self.transiciones += f'ProcesoDatos{self.count_proceso} -> SimboloPuntoyComa{self.count_igual} -> PuntoyComa{self.count_igual}\n'
                        self.count_igual += 1
                        self.count += 1
                        datos = self.pretty_table()
                        self.console += f'\n--> \n{datos} \n'
                        self.count_imprimir = 1
                    else:
                        error = 'Error sintactico ";"'
                        self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                else:
                    error = 'Error sintactico ")"'
                    self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                    self.count += 1
            else:
                error = 'Error sintactico "("'
                self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                self.count += 2
        else:
            error = 'Error sintactico "datos"'
            self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
        self.count_token += 1
        self.count_proceso += 1
        
    def pretty_table(self):
        a = PrettyTable()
        a.field_names = self.list_claves
        for i in self.list_registros:
            a.add_row(i)
        return a
    # FIN Datos
    
    #Conteo
    def instrucciones_conteo(self):
        if self.list_tokens[self.count].lexema.lower().lower() == 'conteo':
            self.nodos += f'TokenConteo{self.count_token} [label="TokenConteo"];\n'
            self.nodos += f'Conteo{self.count_token} [label="conteo", color="#bcf9eb"];\n'
            self.transiciones += f'ProcesoConteo{self.count_proceso} -> TokenConteo{self.count_token} -> Conteo{self.count_token}\n'
            self.count += 1
            if self.list_tokens[self.count].lexema.lower() == 'parentesis abierto':
                self.nodos += f'SimboloParentesisAbierto{self.count_parentesis} [label="ParentesisAbierto"];\n'
                self.nodos += f'ParentesisAbierto{self.count_parentesis} [label="(", color="#bcf9eb"];\n'
                self.transiciones += f'ProcesoConteo{self.count_proceso} -> SimboloParentesisAbierto{self.count_parentesis} -> ParentesisAbierto{self.count_parentesis}\n'
                self.count_parentesis += 1
                self.count += 1
                if self.list_tokens[self.count].lexema.lower() == 'parentesis cerrado':
                    self.nodos += f'SimboloParentesisCerrado{self.count_parentesis} [label="ParentesisCerrado"];\n'
                    self.nodos += f'ParentesisCerrado{self.count_parentesis} [label=")", color="#bcf9eb"];\n'
                    self.transiciones += f'ProcesoConteo{self.count_proceso} -> SimboloParentesisCerrado{self.count_parentesis} -> ParentesisCerrado{self.count_parentesis}\n'
                    self.count_parentesis += 1
                    self.count += 1
                    if self.list_tokens[self.count].lexema.lower() == 'punto y coma':
                        self.nodos += f'SimboloPuntoyComa{self.count_igual} [label="PuntoyComa"];\n'
                        self.nodos += f'PuntoyComa{self.count_igual} [label=";", color="#bcf9eb"];\n'
                        self.transiciones += f'ProcesoConteo{self.count_proceso} -> SimboloPuntoyComa{self.count_igual} -> PuntoyComa{self.count_igual}\n'
                        self.count_igual += 1
                        self.count += 1
                        self.count_imprimir = 1
                        self.console += f'\n--> {len(self.list_registros)}'
                    else:
                        error = 'Error sintactico ";"'
                        self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                else:
                    error = 'Error sintactico ")"'
                    self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                    self.count += 1	
            else:
                error = 'Error sintactico "("'
                self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                self.count += 2
        else:
            error = 'Error sintactico "conteo"'
            self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
        self.count_token += 1
        self.count_proceso += 1
    #FIN Conteo
    
    # Imprimirln
    def instrucciones_imprimirln(self):
        if self.list_tokens[self.count].lexema.lower() == 'imprimirln':
            self.nodos += f'TokenImprimirln{self.count_token} [label="TokenImprimirlm"];\n'
            self.nodos += f'Imprimirln{self.count_token} [label="imprimirln", color="#bcf9eb"];\n'
            self.transiciones += f'ProcesoImprimirln{self.count_proceso} -> TokenImprimirln{self.count_token} -> Imprimirln{self.count_token}\n'
            self.count += 1
            if self.list_tokens[self.count].lexema.lower() == 'parentesis abierto':
                self.nodos += f'SimboloParentesisAbierto{self.count_parentesis} [label="ParentesisAbierto"];\n'
                self.nodos += f'ParentesisAbierto{self.count_parentesis} [label="(", color="#bcf9eb"];\n'
                self.transiciones += f'ProcesoImprimirln{self.count_proceso} -> SimboloParentesisAbierto{self.count_parentesis} -> ParentesisAbierto{self.count_parentesis}\n'
                self.count_parentesis += 1
                self.count += 1
                if self.list_tokens[self.count].lexema.lower() == 'comillas dobles':
                    self.count += 1
                    if self.list_tokens[self.count].lexema.lower() == 'cadena':
                        text = self.list_tokens[self.count].char
                        self.nodos += f'Cadena{self.count_cadena} [label="Cadena"];\n'
                        self.nodos += f'Cadena_Text{self.count_cadena} [label="\'{text}\'", color="#bcf9eb"];\n'
                        self.transiciones += f'ProcesoImprimirln{self.count_proceso} -> Cadena{self.count_cadena} -> Cadena_Text{self.count_cadena}\n'
                        self.count_cadena += 1
                        self.count += 1
                        if self.list_tokens[self.count].lexema.lower() == 'comillas dobles':
                            self.count += 1
                            if self.list_tokens[self.count].lexema.lower() == 'parentesis cerrado':
                                self.nodos += f'SimboloParentesisCerrado{self.count_parentesis} [label="ParentesisCerrado"];\n'
                                self.nodos += f'ParentesisCerrado{self.count_parentesis} [label=")", color="#bcf9eb"];\n'
                                self.transiciones += f'ProcesoImprimirln{self.count_proceso} -> SimboloParentesisCerrado{self.count_parentesis} -> ParentesisCerrado{self.count_parentesis}\n'
                                self.count_parentesis += 1
                                self.count += 1
                                if self.list_tokens[self.count].lexema.lower() == 'punto y coma':
                                    self.nodos += f'SimboloPuntoyComa{self.count_igual} [label="PuntoyComa"];\n'
                                    self.nodos += f'PuntoyComa{self.count_igual} [label=";", color="#bcf9eb"];\n'
                                    self.transiciones += f'ProcesoImprimirln{self.count_proceso} -> SimboloPuntoyComa{self.count_igual} -> PuntoyComa{self.count_igual}\n'
                                    self.count_igual += 1
                                    self.count += 1
                                    self.console += f'\n--> {text}'
                                    self.count_imprimir = 1
                                else:
                                    error = 'Error sintactico ";"'
                                    self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                            else:
                                error = 'Error sintactico ")"'
                                self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                                self.count += 1
                        else:
                            error = 'Error sintactico "Comillas Dobles"'
                            self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                    else:
                        error = 'Error sintactico "Cadena de Texto"'
                        self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                else:
                    error = 'Error sintactico "Comillas Dobles"'
                    self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
            else:
                error = 'Error sintactico "("'
                self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                self.count += 5
        else:
            error = 'Error sintactico "imprimirln"'
            self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
        self.count_token += 1
        self.count_proceso += 1
    #FIN Imprimirln
    
    # Imprimir
    def instrucciones_imprimir(self):
        if self.list_tokens[self.count].lexema.lower() == 'imprimir':
            self.nodos += f'TokenImprimir{self.count_token} [label="TokenImprimir"];\n'
            self.nodos += f'Imprimir{self.count_token} [label="imprimir", color="#bcf9eb"];\n'
            self.transiciones += f'ProcesoImprimir{self.count_proceso} -> TokenImprimir{self.count_token} -> Imprimir{self.count_token}\n'
            self.count += 1
            if self.list_tokens[self.count].lexema.lower() == 'parentesis abierto':
                self.nodos += f'SimboloParentesisAbierto{self.count_parentesis} [label="ParentesisAbierto"];\n'
                self.nodos += f'ParentesisAbierto{self.count_parentesis} [label="(", color="#bcf9eb"];\n'
                self.transiciones += f'ProcesoImprimir{self.count_proceso} -> SimboloParentesisAbierto{self.count_parentesis} -> ParentesisAbierto{self.count_parentesis}\n'
                self.count_parentesis += 1
                self.count += 1
                if self.list_tokens[self.count].lexema.lower() == 'comillas dobles':
                    self.count += 1
                    if self.list_tokens[self.count].lexema.lower() == 'cadena':
                        text = self.list_tokens[self.count].char
                        self.nodos += f'Cadena{self.count_cadena} [label="Cadena"];\n'
                        self.nodos += f'Cadena_Text{self.count_cadena} [label="\'{text}\'", color="#bcf9eb"];\n'
                        self.transiciones += f'ProcesoImprimir{self.count_proceso} -> Cadena{self.count_cadena} -> Cadena_Text{self.count_cadena}\n'
                        self.count_cadena += 1
                        self.count += 1
                        if self.list_tokens[self.count].lexema.lower() == 'comillas dobles':
                            self.count += 1
                            if self.list_tokens[self.count].lexema.lower() == 'parentesis cerrado':
                                self.nodos += f'SimboloParentesisCerrado{self.count_parentesis} [label="ParentesisCerrado"];\n'
                                self.nodos += f'ParentesisCerrado{self.count_parentesis} [label=")", color="#bcf9eb"];\n'
                                self.transiciones += f'ProcesoImprimir{self.count_proceso} -> SimboloParentesisCerrado{self.count_parentesis} -> ParentesisCerrado{self.count_parentesis}\n'
                                self.count_parentesis += 1
                                self.count += 1
                                if self.list_tokens[self.count].lexema.lower() == 'punto y coma':
                                    self.nodos += f'SimboloPuntoyComa{self.count_igual} [label="PuntoyComa"];\n'
                                    self.nodos += f'PuntoyComa{self.count_igual} [label=";", color="#bcf9eb"];\n'
                                    self.transiciones += f'ProcesoImprimir{self.count_proceso} -> SimboloPuntoyComa{self.count_igual} -> PuntoyComa{self.count_igual}\n'
                                    self.count_igual += 1
                                    self.count += 1
                                    if self.count_imprimir == 0:
                                        self.console += text
                                    else:
                                        self.console += f'--> {text}'
                                        self.count_imprimir = 0
                                else:
                                    error = 'Error sintactico ";"'
                                    self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                            else:
                                error = 'Error sintactico ")"'
                                self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                                self.count += 1
                        else:
                            error = 'Error sintactico "Comillas Dobles"'
                            self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                    else:
                        error = 'Error sintactico "Cadena de Texto"'
                        self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                else:
                    error = 'Error sintactico "Comillas Dobles"'
                    self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
            else:
                error = 'Error sintactico "("'
                self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                self.count += 5
        else:
            error = 'Error sintactico "imprimir"'
            self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
        self.count_token += 1
        self.count_proceso += 1
    #FIN Imprimir
    
    # Claves
    def instrucciones_claves(self):
        if self.list_tokens[self.count].lexema.lower().lower() == 'claves':
            self.transiciones += 'ProcesoClaves -> TokenClaves\n'
            self.transiciones += 'TokenClaves -> claves\n'
            self.count += 1
            if self.list_tokens[self.count].lexema.lower() == 'igual':
                self.nodos += f'SimboloIgual{self.count_igual} [label="Igual"];\n'
                self.transiciones += f'ProcesoClaves -> SimboloIgual{self.count_igual}\n'
                self.nodos += f'igual{self.count_igual} [label="=", color="#bcf9eb"];\n'
                self.transiciones += f'SimboloIgual{self.count_igual} -> igual{self.count_igual}\n'
                self.count_igual += 1
                self.count += 1
                if self.list_tokens[self.count].lexema.lower() == 'corchete abierto':
                    self.nodos += f'SimboloCorchete{self.count_corchete} [label="CorcheteAbierto"];\n'
                    self.nodos += f'CorcheteAbierto{self.count_corchete} [label="[", color="#bcf9eb"];\n'
                    self.transiciones += f'ProcesoClaves -> SimboloCorchete{self.count_corchete} -> CorcheteAbierto{self.count_corchete}\n'
                    self.count_corchete += 1
                    self.count += 1
                    self.nodos += f'ListClaves{self.count_list_claves} [label="ListaClaves"];\n'
                    self.transiciones += f'ProcesoClaves -> ListClaves{self.count_list_claves}\n'
                    self.lista_claves()
                    if self.list_tokens[self.count].lexema.lower() == 'corchete cerrado':
                        self.nodos += f'SimboloCorchete{self.count_corchete} [label="CorcheteCerrado"];\n'
                        self.nodos += f'CorcheteCerrado{self.count_corchete} [label="]", color="#bcf9eb"];\n'
                        self.transiciones += f'ProcesoClaves -> SimboloCorchete{self.count_corchete} -> CorcheteCerrado{self.count_corchete}\n'
                        self.count += 1
                        self.count_corchete += 1
                    else:
                        error = 'Error sintactico "]"'
                        self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                else:
                    error = 'Error sintactico "["'
                    self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
            else:
                error = 'Error sintactico "="'
                self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
        else:
            error = 'Error sintactico "claves"'
            self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                
    def lista_claves(self):
        self.nodos += f'Clave{self.count_clave} [label="Clave"];\n'
        self.transiciones += f'ListClaves{self.count_list_claves} -> Clave{self.count_clave}\n'
        self.count_list_claves += 1
        self.count_clave += 1
        self.claves()
    
    def claves(self):
        if self.list_tokens[self.count].lexema.lower() == 'comillas dobles':
            self.count += 1
            self.desagrupar_claves()
        elif self.list_tokens[self.count].lexema.lower() == 'cadena':
            cadena = self.list_tokens[self.count].char
            self.list_claves.append(cadena)
            self.nodos += f'Cadena{self.count_cadena} [label="Cadena"];\n'
            self.nodos += f'Cadena_Texto{self.count_cadena} [label="{cadena}", color="#bcf9eb"];\n'
            self.transiciones += f'Clave{self.count_clave - 1} -> Cadena{self.count_cadena} -> Cadena_Texto{self.count_cadena}\n'
            self.count_cadena += 1
            self.count += 1
            self.desagrupar_claves()
        else:
            if self.list_tokens[self.count].lexema.lower() != 'corchete cerrado': # Cambiarlo si es necesario
                error = 'Error sintactico en claves'
                self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
            
    def desagrupar_claves(self):
        if self.list_tokens[self.count].lexema.lower() == 'coma':
            self.nodos += f'SimboloComa{self.count_coma} [label="Coma"];\n'
            self.nodos += f'Coma{self.count_coma} [label=",", color="#bcf9eb"];\n'
            self.nodos += f'Clave{self.count_clave} [label="Clave"];\n'
            self.transiciones += f'Clave{self.count_clave - 1} -> SimboloComa{self.count_coma} -> Coma{self.count_coma}\n'
            self.count_coma += 1
            self.transiciones += f'Clave{self.count_clave - 1} -> Clave{self.count_clave}\n'
            self.count_clave += 1
            self.count += 1
            self.claves()
        else:
            self.claves()
    # FIN Claves
    
    
    # Registros
    def instrucciones_registros(self):
        if self.list_tokens[self.count].lexema.lower().lower() == 'registros':
            self.transiciones += 'ProcesoRegistros -> TokenRegistros\n'
            self.transiciones += 'TokenRegistros -> registros\n'
            self.count += 1
            if self.list_tokens[self.count].lexema.lower() == 'igual':
                self.nodos += f'SimboloIgual{self.count_igual} [label="Igual"];\n'
                self.transiciones += f'ProcesoRegistros -> SimboloIgual{self.count_igual}\n'
                self.nodos += f'igual{self.count_igual} [label="="];\n'
                self.transiciones += f'SimboloIgual{self.count_igual} -> igual{self.count_igual}\n'
                self.count_igual += 1
                self.count += 1
                if self.list_tokens[self.count].lexema.lower() == 'corchete abierto':
                    self.nodos += f'SimboloCorchete{self.count_corchete} [label="CorcheteAbierto"];\n'    
                    self.nodos += f'CorcheteAbierto{self.count_corchete} [label="[", color="#bcf9eb"];\n'
                    self.transiciones += f'ProcesoRegistros -> SimboloCorchete{self.count_corchete} -> CorcheteAbierto{self.count_corchete}\n'
                    self.count_corchete += 1
                    self.count += 1
                    self.nodos += f'ListRegistros{self.count_list_registro} [label="ListaRegistros"];\n'
                    self.transiciones += f'ProcesoRegistros -> ListRegistros{self.count_list_registro}\n'
                    self.lista_registros()
                    if self.list_tokens[self.count].lexema.lower() == 'corchete cerrado':
                        self.nodos += f'SimboloCorchete{self.count_corchete} [label="CorcheteCerrado"];\n'
                        self.nodos += f'CorcheteCerrado{self.count_corchete} [label="]", color="#bcf9eb"];\n'
                        self.transiciones += f'ProcesoRegistros -> SimboloCorchete{self.count_corchete} -> CorcheteCerrado{self.count_corchete}\n'
                        self.count += 1
                        self.count_corchete += 1
                    else:
                        error = 'Error sintactico "]"'
                        self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                else:
                    error = 'Error sintactico "["'
                    self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
            else:
                error = 'Error sintactico "="'
                self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
        else:
            error = 'Error sintactico "registros"'
            self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
                
    def lista_registros(self):
        self.nodos += f'Registro{self.count_registro} [label="Registro"];\n'
        self.transiciones += f'ListRegistros{self.count_list_registro} -> Registro{self.count_registro}\n'
        self.count_list_registro += 1
        self.registros()
    
    def registros(self):
        if self.list_tokens[self.count].lexema.lower() == 'comillas dobles':
            self.count += 1
            self.desagrupar_registros()
        elif self.list_tokens[self.count].lexema.lower() == 'cadena':
            cadena = self.list_tokens[self.count].char
            self.nodos += f'Cadena{self.count_cadena} [label="Cadena"];\n'
            self.nodos += f'Cadena_Texto{self.count_cadena} [label="{cadena}", color="#bcf9eb"];\n'
            self.transiciones += f'Value{self.count_value - 1} -> Cadena{self.count_cadena} -> Cadena_Texto{self.count_cadena}\n'
            self.count_cadena += 1
            self.registros_valores.append(cadena)
            self.count += 1
            self.desagrupar_registros()
        elif self.list_tokens[self.count].lexema.lower() == 'entero':
            numero_int = self.list_tokens[self.count].char
            self.nodos += f'Entero{self.count_entero} [label="Entero"];\n'
            self.nodos += f'Entero_Texto{self.count_entero} [label="{numero_int}", color="#bcf9eb"];\n'
            self.transiciones += f'Value{self.count_value - 1} -> Entero{self.count_entero} -> Entero_Texto{self.count_entero}\n'
            self.count_entero += 1
            self.registros_valores.append(numero_int)
            self.count += 1
            self.desagrupar_registros()
            self.registros()
        elif self.list_tokens[self.count].lexema.lower() == 'decimal':
            numero_decimal = self.list_tokens[self.count].char
            self.nodos += f'Decimal{self.count_decimal} [label="Decimal"];\n'
            self.nodos += f'Decimal_Texto{self.count_decimal} [label="{numero_decimal}", color="#bcf9eb"];\n'
            self.transiciones += f'Value{self.count_value - 1} -> Decimal{self.count_decimal} -> Decimal_Texto{self.count_decimal}\n'
            self.count_decimal += 1
            self.registros_valores.append(numero_decimal)
            self.count += 1
            self.desagrupar_registros()
        elif self.list_tokens[self.count].lexema.lower() == 'llave abierta':
            self.count += 1
            self.count_registro += 1
            self.nodos += f'SimboloLlaveAbierta{self.count_llave} [label="LlaveAbierta"];\n'
            self.nodos += 'llaveAbierta' + str(self.count_llave) + ' [label="{", color="#bcf9eb"];\n'
            self.nodos += f'Registro{self.count_registro} [label="Registro"];\n'
            self.nodos += f'ListValues{self.count_registro - 1} [label="ListaValores"];\n'
            self.nodos += f'Value{self.count_value} [label="Valor"];\n'
            self.transiciones += f'Registro{self.count_registro - 1} -> SimboloLlaveAbierta{self.count_llave} -> llaveAbierta{self.count_llave}\n'
            self.transiciones += f'Registro{self.count_registro - 1} -> ListValues{self.count_registro - 1} -> Value{self.count_value}\n'
            self.count_llave += 1
            self.count_value += 1
            self.registros()
        elif self.list_tokens[self.count].lexema.lower() == 'llave cerrada':            
            self.count += 1
            self.nodos += f'SimboloLlaveCerrada{self.count_llave} [label="LlaveCerrada"];\n'
            self.nodos += 'llaveCerrada' + str(self.count_llave) + ' [label="}", color="#bcf9eb"];\n'
            self.transiciones += f'Registro{self.count_registro - 1} -> SimboloLlaveCerrada{self.count_llave} -> llaveCerrada{self.count_llave}\n'
            self.transiciones += f'Registro{self.count_registro - 1} -> Registro{self.count_registro}\n'
            self.count_llave += 1
            self.list_registros.append(self.registros_valores)
            self.registros_valores = []
            self.registros()
        else:
            if self.list_tokens[self.count].lexema.lower() != 'corchete cerrado': # Cambiarlo si es necesario
                error = 'Error sintactico en registros'
                self.list_errors.append(Error(error, 'Error sintactico', self.list_tokens[self.count].linea, self.list_tokens[self.count].columna))
    
    def desagrupar_registros(self):
        if self.list_tokens[self.count].lexema.lower() == 'coma':
            self.nodos += f'Value{self.count_value} [label="Valor"];\n'
            self.transiciones += f'Value{self.count_value - 1} -> Value{self.count_value}\n'
            self.count_value += 1
            self.count += 1
            self.registros()
        elif self.list_tokens[self.count].lexema.lower() == 'llave cerrada':
            pass
        else:
            self.registros()
    # FIN Registros
    
    # ListaErroresSintacticos
    def get_lista_errores(self):
        return self.list_errors
    # FIN ListaErroresSintacticos