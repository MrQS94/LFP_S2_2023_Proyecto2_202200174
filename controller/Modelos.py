from abc import ABC, abstractmethod

class Expression(ABC):
    def __init__(self, lexema, char, linea, columna):
        self.lexema = lexema
        self.char = char        
        self.linea = linea 
        self.columna = columna 
    
    @abstractmethod
    def get_token_html(self):
        return ''
    
    @abstractmethod
    def get_tipo(self):
        return self.char
    

class Token(Expression):
    def __init__(self, char, lexema, linea, columna):
        self.lexema = lexema
        super().__init__(lexema, char, linea, columna)
    
    def get_token_html(self):
        html = ''
        html += '<tr>\n'
        html += f'<td> {self.lexema} </td>'
        html += f'<td> {self.char} </td>'
        html += f'<td> {self.linea} </td>'
        html += f'<td> {self.columna} </td>'
        html += '</tr>\n'
        return html
    
    def get_tipo(self):
        return self.char

class Error(Expression):
    def __init__(self, char, lexema, linea, columna):
        self.lexema = lexema
        super().__init__(lexema, char, linea, columna)
    
    def get_token_html(self):
        html = ''
        html += '<tr>\n'
        html += f'<td> {self.lexema} </td>'
        html += f'<td> {self.char} </td>'
        html += f'<td> {self.linea} </td>'
        html += f'<td> {self.columna} </td>'
        html += '</tr>\n'
        return html
    
    def get_tipo(self):
        return self.char