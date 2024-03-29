import os
from time import sleep

def show_file():

    # Direccion del archivo a leer
    name_folder = input(' ingrese el nombre de la carpeta donde están ubicados los archivos: ')
    path_file_input = os.path.join(os.path.dirname(os.getcwd()), name_folder) 
 
    # Nombre del archivo a leer
    name_file = input('Ingrese el nombre del archivo, por ejemplo "ascii.art.jardin.txt": ')
    name_input = name_file
    delay = 1.5  # en segundos

    try:
        while True:
        # Abro el archivo a leer y lo cargo  en 'data'
            with open(os.path.join(path_file_input, name_input), encoding='utf_8') as data:
                for line in data: # por cada linea de 'data'
                    centered_line = line.rstrip().center(os.get_terminal_size().columns)
                    print(centered_line)  # imprimo la linea centrada
                    sleep(delay)  # momento de pausa
        
    except FileNotFoundError:
        print('ERROR: No se ha encontrado el archivo.')
        option = input("¿Desea salir (E) o volver a intentarlo (Y)? ").lower()
        if option== 'e':
            exit()
        else:
            show_file()


                  
if __name__ == '__main__':
    show_file()
    
