#Código principal donde se implementa la lógica del juego WorldCraftASCII.
import utilidades as uti

print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _    _ _ _ _ _ _ _ _ _ _ _ _')
print('/ \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ /  \     / \ / \ / \ / \ / \ / \ ')
print('(W )( o )( r )( l )( d )( C )( r )( a )( f )( t )   (A )( S )( C )( I )( I )')
print('\ / \ / \ / \  / \  / \ / \ / \ /  \ / \  / \  /    \  / \  / \  / \  / \  /')  
print('- - - - - - - - - - - - - - - - - - - - - - - - -    - - - - - - - - - - - - \n')

print('Inscripción del Jugador \n')
cdia = input("por favor ingresa un CDIA: ").upper()

#cdia = 'ji466ghj-h@8yot'.upper()
validar = (uti.longitud(cdia,15) and uti.validar_numeros(cdia) and uti.posicion_ocho(cdia) and uti.caracter_diferente(cdia) and uti.letra_o(cdia) and uti.simbolos(cdia))


if validar:
  print("CDIA valido, responde unas preguntas\n")
  fecha = input("ingresa la fecha de nacimiento dia/mes/año, ejemplo: 24/08/1992: ")
  edad= uti.edad(fecha)
  print(edad)
  if edad > 15:
    print("cumples con los requisitos al ser mayor de 15 años\n")
    alias = input("ingresa un alias con una longitud de carateres \nmaxima de 8 y debe contener un numero: ")
    if uti.longitud(alias,8) and uti.validar_numero(alias):
      jugar =  int(input(" ¿Ya has jugado WorldCfraft ASCII (Si = 1, No = 0): "))
      if jugar == 1:
        print("seras asignado al nivel del juego n.10")
        u= uti.asignar_mundo(edad,jugar)
        print(f"seras asignado al {u}")
      elif jugar == 0:
        print("al no a ver jugado nunca empezaras en el nivel n.1")
        u= uti.asignar_mundo(edad,jugar)
        print(f"seras asignado al {u}")
    else:
      print("parametros invalidos")
  elif edad <= 15:
    print("no puedes jugar debido a que tu edad es menor a 15 años")
    
else:
  print("CDIA inválido")
  