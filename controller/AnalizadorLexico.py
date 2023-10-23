from Modelos import Token, Error

class AnalizadorLexico():
    def __init__(self):
        self.tokens = []
        self.errores = []
    
    def analizar(self, file):
        i = 0
        self.tokens = []
        self.errores = []
        columna = 1
        linea = 1
        estado = 0
        lexema = ''
        while len(file) > i:
            char = file[i]
            if estado == 0:
                if char == '=':
                    self.tokens.append(Token(char, 'igual', linea, columna))
                    columna += 1
                elif char == '[':
                    self.tokens.append(Token(char, 'corchete abierto', linea, columna))
                    columna += 1
                elif char == ']':
                    self.tokens.append(Token(char, 'corchete cerrado', linea, columna))
                    columna += 1
                elif char == '{':
                    self.tokens.append(Token(char, 'llave abierta', linea, columna))
                    columna += 1
                elif char == '}':
                    self.tokens.append(Token(char, 'llave cerrada', linea, columna))
                    columna += 1
                elif char == '(':
                    self.tokens.append(Token(char, 'parentesis abierto', linea, columna))
                    columna += 1
                elif char == ')':
                    self.tokens.append(Token(char, 'parentesis cerrado', linea, columna))
                    columna += 1
                elif char == ',':
                    self.tokens.append(Token(char, 'coma', linea, columna))
                    columna += 1
                elif char == ';':
                    self.tokens.append(Token(char, 'punto y coma', linea, columna))
                    columna += 1	
                elif char == ' ' or char == '\t':
                    columna += 1
                elif char == '"':
                    self.tokens.append(Token(char, 'comillas dobles', linea, columna))
                    columna += 1
                    estado = 7
                elif char == '#':
                    self.tokens.append(Token(char, 'comentario simple', linea, columna))
                    columna += 1
                    estado = 1
                elif char == '\'':
                    self.tokens.append(Token(char, 'comillas simples', linea, columna))
                    columna += 1
                    estado = 2
                elif char == '\n':
                    linea += 1
                    columna = 1
                elif self.is_num(char):
                    lexema += char
                    columna += 1
                    estado = 9
                elif self.is_letter(char):
                    lexema += char
                    columna += 1
                    estado = 11 
                elif char == '♥':
                    self.tokens.append(Token(char, 'fin del archivo', linea, columna))
                else:
                    error = f'Error lexico "{ord(char)}": ' + char
                    self.errores.append(Error(error, 'Error lexico', linea, columna))
            elif estado == 1:
                if char == '\n':
                    linea += 1
                    columna = 1
                    estado = 0
            elif estado == 2:
                if char == '\'':
                    columna += 1
                    estado = 3
                elif char == '\n':
                    linea += 1
                    columna += 1
            elif estado == 3:
                if char == '\'':
                    self.tokens.append(Token("'''", 'comillas simples', linea, columna))
                    columna += 1
                    estado = 4
                elif char == '\n':
                    linea += 1
                    columna = 1
                elif ord(char) == 32 or ord(char) == 10 or ord(char) == 9:
                    pass
                else:
                    error = f'Error lexico "{ord(char)}": ' + char
                    self.errores.append(Error(error, 'Error lexico', linea, columna))   
            elif estado == 4:
                if char == '\'':
                    columna += 1
                    estado = 5
                elif char == '\n':
                    linea += 1
                    columna = 1
            elif estado == 5:
                if char  ==  "'":
                    columna += 1
                    estado = 6
                elif char == '\n':
                    linea += 1
                    columna=1
            elif estado == 6:
                if char  ==  "'":
                    self.tokens.append(Token("'''", 'comillas simples', linea, columna))
                    columna += 1
                    estado = 0
                elif char == '\n':
                    linea += 1
                    columna = 1
            elif estado == 7:
                if self.is_char(char):
                    lexema += char
                    columna += 1
                    estado = 8
                elif char == '"':
                    lexema = ''
                    columna += 1
                    i -= 1
                    estado = 8
                else:
                    error = f'Error lexico "{ord(char)}": ' + char
                    self.errores.append(Error(error, 'Error lexico', linea, columna))
            elif estado == 8:
                if self.is_char(char):
                    lexema += char
                    columna += 1
                elif char == '"':
                    self.tokens.append(Token(lexema, 'cadena', linea, columna))
                    self.tokens.append(Token(char, 'comillas dobles', linea, columna))
                    lexema = ''
                    columna += 1
                    estado = 0
                else:
                    error = f'Error lexico "{ord(char)}": ' + char
                    self.errores.append(Error(error, 'Error lexico', linea, columna))
            elif estado == 9:
                if self.is_num(char):
                    lexema += char
                    columna += 1
                elif char == '.':
                    lexema += char
                    columna += 1
                    estado = 10
                else:
                    self.tokens.append(Token(lexema, 'entero', linea, columna))
                    lexema = ''
                    i -= 1
                    estado = 0
            elif estado == 10:
                if self.is_num(char):
                    lexema += char
                    columna += 1
                else:
                    self.tokens.append(Token(lexema, 'decimal', linea, columna))
                    lexema = ''
                    estado = 0
                    i -= 1
            elif estado == 11:
                if self.is_letter(char):
                    lexema += char
                else:
                    if lexema.lower() == 'claves':
                        self.tokens.append(Token('claves', lexema, linea, columna))
                    elif lexema.lower()  == 'registros':
                        self.tokens.append(Token('registros', lexema, linea, columna))
                    elif lexema == 'imprimir':
                        self.tokens.append(Token('imprimir', lexema, linea, columna))
                    elif lexema == 'imprimirln':
                        self.tokens.append(Token('imprimirln', lexema, linea, columna))
                    elif lexema == 'conteo':
                        self.tokens.append(Token('conteo', lexema, linea, columna))
                    elif lexema == 'promedio':
                        self.tokens.append(Token('promedio', lexema, linea, columna))
                    elif lexema == 'contarsi':
                        self.tokens.append(Token('contarsi', lexema, linea, columna))
                    elif lexema == 'datos':
                        self.tokens.append(Token('datos', lexema, linea, columna))
                    elif lexema == 'sumar':
                        self.tokens.append(Token('sumar', lexema, linea, columna))
                    elif lexema == 'max':
                        self.tokens.append(Token('max', lexema, linea, columna))
                    elif lexema == 'min':
                        self.tokens.append(Token('min', lexema, linea, columna))
                    elif lexema == 'exportarReporte':
                        self.tokens.append(Token('exportarReporte', lexema, linea, columna))
                    else:
                        error = f'Error lexico "{ord(char)}": ' + char
                        self.errores.append(Error(error, 'Error lexico', linea, columna))
                    lexema = ''
                    i -= 1
                    estado = 0
            i += 1
        return self.tokens
    
    def get_lista_errores(self):
        return self.errores
    
    def is_char(self, char):
        if ((ord(char) >= 32 and ord(char) != 34)):
            return True
        elif (160 <= ord(char) <= 165 or ord(char) == 129 or ord(char) == 130):
            return True
        elif ord(char) == 34:
            return False
        
    def is_letter(self, char):
        if((ord(char) >= 65 and ord(char) <= 90) 
        or (ord(char) >= 97 and ord(char) <= 122) 
        or ord(char)  ==  164 or ord(char)  ==  165):
            return True
        else:
            return False
    
    def is_num(self, char):
        if ((ord(char) >= 48 and ord(char) <= 57)):
            return True
        else:
            return False