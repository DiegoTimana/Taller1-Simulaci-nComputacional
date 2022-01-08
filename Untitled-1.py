import PyPDF2 
import textract
import nltk
#nltk.download() se debe descargar para utilizar la funcion word tokenize
from nltk.tokenize import word_tokenize


filename = 'Cien-anos-de-soledad.pdf'
pdfFileObj = open(filename,'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#para analizar todas las paginas
num_pages = pdfReader.numPages
count = 0
text = ""

#para leer todas las paginas del pfd 
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()

#Ahora tenemos una variable de texto que contiene todo el texto derivado de nuestro archivo PDF. Escriba print (texto) 
# para ver qué contiene. Es probable que contenga muchos espacios, posiblemente basura como '\ n', etc.

#la funcion word tokenize separará todo el texto en una lista de palabras individuales (incluye los caracteres de puntuacion)
tokens = word_tokenize(text)

#lista de la longitud de las palabras que estan despues de un signo gramatical
nums = []

#signos
signos = [',','.',';',':','?','¿','(',')','!','¡']

#funcion que revisa en bucle los tokens, y agrega a la lista de numeros la palabra que hay despues de cada signo gramatical
# hasta que la lista tenga 1000 datos (se llene).
#cuando atrapamos una excepcion significa que llegamos al final del texto, y seteamos la bandera de finalizacion con un -1
#para detener el bucle.
def pseudoaleatorios(signo,lista):
    start = 0
    finish_flag = 0
    while finish_flag == 0 and len(lista) < 1000:
        try:
            index = tokens.index(signo,start) 
        except:
            finish_flag = -1
        palabra = tokens[index+1]
        lista.append(len(palabra)) #ya se agregó el numero a la lista de nuestros pseudo aleatorios
        start = index+2


for n in signos: 
    if len(nums) < 1000:
        pseudoaleatorios(n,nums)
    else: 
        break

###################################SALIDA PRIMER EJERCICIO############################################################
print("SALIDA PUNTO A","tamaño de la lista", len(nums), "\n Lista de los numeros", "\n", nums)


#######EJERCICIO 2##########
resultado = []
start = 0 #empieza a buscar desde el token 0, se tiene que ir actualizando cada vez para ir mas adelante.
#for para obtener el indice inicial y el indice final de los signos de gramática.
def generarnum(lista):
    indice_ini = 0 # indices de donde se encuentran los signos gramaticales.
    indice_fin = 0
    global start
    for n in tokens:
        if n in signos and indice_ini==0:
            indice_ini = tokens.index(n,start)
        elif n in signos and indice_ini != 0:
            indice_fin = tokens.index(n,indice_ini+1)
        elif indice_fin != 0 and indice_ini != 0:
            break 
    num = 0
#con este for contamos los caracteres de cada palabara entre los dos indices (signos de gramatica), que nos resulta en el
#numero que buscamos
    for i in range(indice_ini+1, indice_fin):
        num += len(tokens[i])
    lista.append(num)
    start = indice_fin

#funcion que llama a generar num en bucle hasta que se consigan los 1000 numeros que necesitamos
def aleatorios():
    while len(resultado) < 1000:
        generarnum(resultado)

aleatorios()

###################################SALIDA SEGUNDO EJERCICIO############################################################
#print("SALIDA PUNTO B","tamaño de la lista", len(resultado), "\n Lista de los numeros", "\n", resultado)


    