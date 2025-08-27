# SYSACAD

Aplicación de gestión de universidades desarrollada en Python con el framework Flask.
Permite crear, leer, actualizar y eliminar información de universidades.

# CARACTERISTICAS

CRUD de universidades

Separación de entornos (desarrollo, testing y producción)

Migraciones con Flask-Migrate

Configuración mediante variables de entorno (.env)

# INSTALACION

1. Clonar el repositorio

2. Crear y activar entorno virtual
   python3 -m venv venv
   source venv/bin/activate # Linux / Mac
   venv\Scripts\activate # Windows

3. Instalar dependencias
   pip install -r requirements.txt o ./install.sh

4. Configurar base de datos

Crear 3 bases de datos:

sysacad_dev

sysacad_test

sysacad_prod

5. Configurar variables de entorno

Copiar el archivo de ejemplo y editarlo:

cp env_example .env

6. Crear migraciones y tablas
   flask db init
   flask db migrate
   flask db upgrade

7. Seleccionar entorno de ejecución

Usar el script boot.sh para elegir development o production y correr la aplicacion:

./boot.sh development o ./boot.sh production

## Uso

Una vez iniciada la aplicación, la API estará disponible en:

http://localhost:5000/api/v1

### Ejemplo de endpoint

- Obtener todas las universidades:

GET http://localhost:5000/api/v1/universidad

- Crear una nueva universidad:

POST http://localhost:5000/api/v1/universidad
Body (JSON):
{
"nombre": "Universidad de Ejemplo",
"sigla": "UEX",
"tipo": "Privada"
}

- Obtener universidad por Hashid:

GET http://localhost:5000/api/v1/universidad/Y10NDOQA72bnPwqK

Grupo:
Aguilera Sebastián
Aguilera Rocio
Gualpa Agostina
González Luciana
Perez Jazmín
Choquevillca Celeste
Guzman Dana
