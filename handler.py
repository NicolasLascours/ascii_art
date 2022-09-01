import os
from time import sleep


# Direccion del archivo a leer
name_folder = "ascii_art" # nombre de la carpeta donde están ubicados los archivos
path_file_input = os.path.join(os.path.dirname(os.getcwd()), name_folder) 

def show_file():
    # Nombre del archivo a leer
    name_file = input('Ingrese el nombre del archivo, por ejemplo "ascii.art.jardin.txt": ')
    name_input = name_file
    delay = 1.5  # en segundos

    try:
        while True:
        # Abro el archivo a leer y lo cargo  en 'data'
            with open(os.path.join(path_file_input, name_input), encoding='utf_8') as data:
                for line in data: # por cada linea de 'data'
                    print(line)   # imprimo la linea
                    sleep(delay)  # momento de pausa
        
    except FileNotFoundError:
        print('ERROR: No se ha encontrado el archivo.')

if __name__ == '__main__':
    
    show_file()
    
