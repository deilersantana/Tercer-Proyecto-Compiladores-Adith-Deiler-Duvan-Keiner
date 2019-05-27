# -*- encondig: utf-8 -*-

import ply.lex as lex
import os

# lista de tokens
tokens = (

    # Palabras Reservadas
    'INICIO',
    'HASTA',
    'SI',
    'ENTERO',
    'STRING',
    'SINO',
    'MIENTRAS',
    'OPC',
    # Symbolos
 
    'MAS',
    'MENOS',
    'POR',
    'ENTRE',
    'MENOR',
    'MENORQUE',
    'MAYOR',
    'MAYORQUE',
    'IGUAL',
    'Y',
    'O',
    'IGUALIGUAL',
    'DIFERENTE',
    'LCORCHETE',
    'RCORCHETE',
    'DELIMITADOR',
    'COMILLAS',
    'SEPARADOR',


    #Otros
    'ID',
    'NUMERO',
)


# Reglas de Expresiones Regualres para token de Contexto simple


t_MAS = r'\+'
t_MENOS = r'-'
t_POR = r'\*'
t_ENTRE = r'/'
t_IGUAL = r'='
t_MENOR = r'<'
t_MAYOR = r'>'
t_LCORCHETE = r'\['
t_RCORCHETE = r'\]'
t_DELIMITADOR = r'\|'
t_SEPARADOR = r'\:'
t_COMILLAS = r'\"'


def t_INICIO(t):
    r'inicio'
    return t

def t_SINO(t):
    r'sino'
    return t


def t_SI(t):
    r'si'
    return t


def t_ENTERO(t):
    r'entero'
    return t



def t_MIENTRAS(t):
    r'mientras'
    return t


def t_HASTA(t):
    r'hasta'
    return t


def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

#exprecion regular para reconocer los identificadores


def t_ID(t):
    r'\w+(_\d\w)*'
    return t


def t_STRING(t):
#expresion RE para reconocer los String
    r'\"?(\w+ \ *\w*\d* \ *)\"?'
    return t

def t_Y(t):
    r'oo'
    return t

def t_O(t):
    r'yy'

def t_MENORQUE(t):
    r'<='
    return t


def t_MAYORQUE(t):
    r'>='
    return t


def t_IGUALIGUAL(t):
    r'=='
    return t



def t_DIFERENTE(t):
    r'!='
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'



def t_error(t):
    print (("Error Lexico: " + str(t.value[0])))
    t.lexer.skip(1)



def test(data, lexer):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print (tok)

lexer = lex.lex()

def Analizador_lexico():
    a = raw_input("direccion: ")
    if ( os.path.exists (a)):
        f = open(a)
        data = f.read()
        f.close()
        #Build lexer and try on
        lexer.input(data)
        test(data, lexer)
    else:
        print ("El archivo no existe")


# Test
if __name__ == '__main__':

    # Test  ESTO ES SOLO PARA PROBAR EL FUNCINAMIENTO DE ANIZADOR LEXICO.
    #Cargamos el archivo "c.cpp" que esta en la carpeta ejemplos y lo guardamos
    #la variable data para despues enviarla al analizador lexico para que la
    #descomponga en tokes

    f = open('C:/Users/keiner/Desktop/proyecto 3/ejemplo.ADK')
    data = f.read()
    f.close()
    #Build lexer and try on
    lexer.input(data)
    test(data, lexer)
