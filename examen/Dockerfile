# Imagen base de Python
FROM python:3.9

# Directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos necesarios al contenedor
COPY requirements.txt ./

# Instalar las dependencias
RUN pip3 install -r requirements.txt

COPY . .

# Comando para ejecutar la aplicación Flask
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
