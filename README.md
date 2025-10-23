# ZienIdeas
Reto Tecnico: Prototipo de Generador Automático de Relatos Infantiles

# Nombre: Antonio Fernandez Soto (antferna)

El objetivo del projecto es crear un generador de historias a partir de un input.

Las historias seran cuentos infantiles con una estructura determinada.

Pasos a seguir:
-Recibir por consola un texto como argumento, por ejemplo
'python3 zien.py "un caballo negro"'

-Se comprueba que el input es correcto, sino lo es el programa termina la ejecución.

-Si todo sigue bien se procede a enviar el texto a una IA Generadora de textos con una estructura predeterminada añadiendo el texto introducido por el usuario

-El texto generado por la IA pasa al proceso de validación, por el que se envia a otra IA que comprueba si la historia cumple los requisitos predeterminados.

-Si no los cumple vuelve a repetir el proceso, dejando constancia en los logs del error y intentando volver a crear una historia nueva

-Una vez la historia esta validada pasamos al proceso de exportación.

-Volvemos a usar una IA generadora de imagenes introduciendo el input del usuario junto a uno predeterminado donde se genera una imagen que se junta con el PDF generado anteriormente.

-Se procede a la descarga por parte del usuario


