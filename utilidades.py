#En este modulo agregar la función de validación del código CDIA
import re
from datetime import datetime

# Inscripción del Jugador

def validar_numeros(codigo:str) -> bool:
  """
	Función encarga de validar si existe un total de 4 numeros 
  Parameters
	-----------------
	codigo : str
		cadena a validar
	Returns
	------------------
	existe : bool
		Retorna True si existe, de lo contrario False
  """
  
  pr = len(re.findall(r'\d', codigo.upper()))
  if pr == 4:
    return True
  else:
    return False
 
def longitud(codigo : str,longitud : int) -> bool:
  """
	Función encarga de validar el largo de una cadena de texto
  Parameters
	-----------------
	codigo : str
		cadena a validar
	Returns
	------------------
	existe : bool
		Retorna True si existe, de lo contrario False
  """
  if codigo.__len__() == longitud: 
    return True
  else:
    return False

def posicion_ocho(codigo : str) -> bool:
  """
	Función encarga de validar segun la posicion el caracter simbolo 
  Parameters
	-----------------
	codigo : str
		cadena a validar
	Returns
	------------------
	existe : bool
		Retorna True si existe, de lo contrario False
  """
  
  if codigo.upper()[8] == '-':
    return True
  else:
    return False

def caracter_diferente(codigo : str) -> bool:
  """
	Función encarga de validar que los caracteres en las posiciones
  sean diferentes.
  Parameters
	-----------------
	codigo : str
		cadena a validar
	Returns
	------------------
	existe : bool
		Retorna True si existe, de lo contrario False
  """
  if codigo.upper()[1] == codigo.upper()[-2]:
    return False
  else:
    return True

def letra_o(codigo : str) -> bool:
  """
	Función encarga de validar si existe  al menos una letra en 
  la cadena de texto.
  Parameters
	-----------------
	codigo : str
		cadena a validar
	Returns
	------------------
	existe : bool
		Retorna True si existe, de lo contrario False
  """
  if codigo.upper().count('O') == 1:
    return True
  else:
    return False

def simbolos(codigo : str) -> bool:
  """
	Función encarga de validar si existe una serie de simbolos
  en la cadena de texto ingresada.
  Parameters
	-----------------
	codigo : str
		cadena a validar
	Returns
	------------------
	existe : bool
		Retorna True si existe, de lo contrario False
  """
  if codigo.count('>') or codigo.count('=') or codigo.count('@'):
    return True
  else:
    return False
    
# Inscripción del Jugador
def edad(fecha : str) -> str:
  """
	Función encarga de validar la fecha 
  Parameters
	-----------------
	codigo : str
		cadena a validar
	Returns
	------------------
	existe : bool
		Retorna edad si existe, de lo contrario err
  """
  try:
    fecha_nacimiento = datetime.strptime(fecha, '%d/%m/%Y')
    fecha_actual = datetime.now()
    edad = fecha_actual.year - fecha_nacimiento.year
    return edad
  except ValueError as err:
    err = 'Formato Incorrecto de la fecha de nacimiento'
    return err
def validar_numero(codigo : str):
  """
	Función encarga de validar que una cadena de texto contenga digitos numericos
  Parameters
	-----------------
	codigo : str
		cadena a validar
	Returns
	------------------
	existe : bool
		Retorna true si existe, de lo contrario False
  """
  if re.search(r'\d', codigo) != False:
    return True
  else:
    return False

def asignar_mundo(edad : int , jugar: int) -> str:
  """
	Función encarga de validar el mundo de acuerdo a la edad y si jugo o no
  Parameters
	-----------------
	codigo : str
		cadena a validar
	Returns
	------------------
	existe : bool
		Retorna True si existe, de lo contrario False
  """
  mundo_1 = "Mundo 1"
  mundo_2 = "Mundo 2"
  mundo_3 = "Mundo 3"
  mundo_4 = "Mundo 4"
  no_mundo= "no posees mundo"
  if edad >= 16 and edad <= 30 and jugar == 0:
    return mundo_1
  elif edad >= 16 and edad <= 30 and jugar == 1:
    return mundo_2
  elif edad >= 31 and edad <= 40 and jugar == 1:
    return mundo_3
  elif edad > 40  and jugar == 0:
    return mundo_4
  else:
    return no_mundo