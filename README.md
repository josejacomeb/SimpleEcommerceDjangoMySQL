# SimpleEcommerceDjangoMySQL
## Dependencias Software
- Python 3.10
- Django
- mysqlclient

## Instrucciones
1. (Opcional), crear un nuevo entorno de Python
2. Instalar las dependencias del proyecto con `pip install -r requirements.txt`
3. Editar el archivo `simple_eccomerce/settings.py`, en la sección `DATABASES` para subministrar el `USER` y `PASSWORD` adecuados, de acuerdo a las configuraciones locales
4. Inicializar las migraciones propias para preparar la base de datos
    ```cmd
    python manage.py makemigrations ecommerce
    ```
5. Inicializar las migraciones adicionales de Django para finalizar el proceso
    ```cmd
    python manage.py migrate
    ```
6. Inicializar el servidor Django con el siguiente comando `python manage.py runserver`