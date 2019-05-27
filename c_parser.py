# -*- enconding: utf-8 -*-
#!/usr/bin/python
import ply.yacc as yacc
import os
from c_lexer import tokens
import sys


VERBOSE = 1


def p_inicio(p):
    '''inicio : INICIO cuerpo_fun 
    | empty'''
    pass
def p_cuerpo_fun(p):
    'cuerpo_fun : DELIMITADOR sentencias_lista DELIMITADOR'

def p_sentencias_lista(p):
    '''sentencias_lista : sentencias_lista sentencias 
    | empty'''
    pass


def p_sentencias_lista_2(p):
    'sentencias_lista : sentencias'
    pass


def p_sentencias(p):
    '''sentencias : var_declaration
    | fun_declaraciones 
    | empty'''
    pass


def p_var_declaration_1(p):
    '''var_declaration : type_specifier ID 
    | type_specifier ID IGUAL NUMERO 
    | type_specifier ID IGUAL var '''
    pass

def p_var_declaracion_1(p):
    'var_declaration : empty'
    pass

def p_type_specifier_1(p):
    'type_specifier : ENTERO'
    pass


def p_type_specifier_(p):
    'type_specifier : STRING'
    pass


def p_fun_declaraciones(p):
    '''fun_declaraciones : fun_iteracion fun_declaraciones
    | fun_condicion fun_declaraciones
    | empty'''


def p_fun_iteracion(p):
    'fun_iteracion : iteration_stmt '
    pass



def p_iteration_stmt1(p):
    'iteration_stmt : HASTA LCORCHETE var SEPARADOR var RCORCHETE cuerpo_fun'
    pass

    
def p_iteration_stmt_2(p):
    'iteration_stmt : MIENTRAS LCORCHETE expression RCORCHETE cuerpo_fun'
    pass

def p_fun_condicion_1(p):
    'fun_condicion : SI LCORCHETE expression RCORCHETE cuerpo_fun'

def p_fun_condicion_2(p):
    'fun_condicion :  SI LCORCHETE expression RCORCHETE  cuerpo_fun SINO cuerpo_fun'



def p_expression(p):
    'expression : var operadores var'
    pass


def p_operadores(p):
    '''operadores : MENOR 
    | MENORQUE
    | MAYOR
    | MAYORQUE'''



def sintax(t):
    os.system("g++ -Wall "+t)
    pass


def p_var(p):
    'var : ID'
    pass




def p_empty(p):
    'empty :'
    pass


def p_error(p):
    if VERBOSE:
        if p is not None:
            print ("Error en Sintaxis linea:" , str(p.lexer.lineno),"  Error de Contexto " , str(p.value))
        else:
            print ("Error en Lexico linea: " ,str(c_lexer.lexer.lineno))
    else:
        raise Exception('Syntax', 'error')

parser = yacc.yacc()



