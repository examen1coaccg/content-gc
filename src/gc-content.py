'''
Name: gc-content.py
Author: Shirley Alquicira
Version: 1.0
Description: Este programa permite llevar a cabo el análisis de secuencias genómicas para determinar el contenido de Guanina y Citosina.
Input: Secuencia de nucleótidos
Output: Impresión en pantalla del porcentaje de GC
Execution:
python gc-content.py atcgatcgatg

'''

import sys

sequence=input("Por favor, introduce la secuencia de nucleótidos a analizar: ").upper()

validSequence = {"A. "T". "G". "C"}
