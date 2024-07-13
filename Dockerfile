# importando la libreria base para el proyecto, pueden ser varias librerias
FROM python:3

# crea la ruta de donde estara toda la data
WORKDIR /app

# Instala virtualenv para docker
RUN pip install virtualenv

# Crea un entorno virtual, para uso de la api
RUN virtualenv env

# Activa el entorno virtual usando source
RUN /bin/bash -c "source env/bin/activate"

# Copia el archivo requirements.txt al contenedor (el punto es la ruta en la que esta el dockerfile)
COPY requirements.txt .

# Instala las dependencias dentro del entorno virtual
RUN env/bin/pip install --no-cache-dir -r requirements.txt

# copiar todos los archivos de mi proyecto 
COPY . .

# ejecutar todo esto con un comando en cmd
CMD [ "env/bin/python", "app.py"]