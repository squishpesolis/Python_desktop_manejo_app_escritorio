# Instalación Ambiente Producción
1. Descargar e instalar python 3.11
    https://www.python.org/downloads/
2. En cmd.exe ejecutar en la raiz del proyecto:
   - pyinstaller --windowed main.py

# Instalción Ambiente Desarrollo
1. Descargar e instalar python 3.11
    - https://www.python.org/downloads/

2. Instalar virtualenv
    - pip install virtualenv

3. Creacion de un entorno virtual
    ejecutar en la raiz del proyecto
    - virtualenv my-env

4. Si el entorno ya esta creado, se debe activar: en cmd.exe
    - my-env\Scripts\activate.bat

5. Instalar los requerimientos
    - python -m pip install -r requeriments\dev.txt

6. Es conveniente desactivar el ambiente cuando se termine el desarrollo, en cmd.exe:
    - deactivate

7. Ejecutar el programa con:
    - python main.py

8. Generar ejecutable, dentro de (my-env) en cmd.ex ejecutar:
    - pyinstaller main.py -n controlApp  --windowed --collect-data AppOpener --onefile --add-data .env.dev;. --add-data .env.prod;.

# Ejecución de Pruebas


python -m unittest

# TODO
Realizar test de obtener todos los programas 