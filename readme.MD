<h1>Cómo ejecutar el servidor<h1>
1. Abrir la carpeta OpenAni base
2. En terminal debe activar el .venv usando el comando ".\venv\Scripts\activate"
3. cd ./OpenAni_DB
4. En terminal: python .\manage.py makemigrations
5. En terminal: python .\manage.py migrate
6. En terminal: python .\manage.py runserver