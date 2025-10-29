# Proyecto de API REST con FastAPI

Este es un proyecto de ejemplo de una API REST desarrollada con FastAPI.

## Descripción

El proyecto implementa una API para gestionar usuarios, con operaciones básicas de Crear, Leer, Actualizar y Eliminar (CRUD).

## Tecnologías utilizadas

* **Python:** Lenguaje de programación principal.
* **FastAPI:** Framework web moderno y de alto rendimiento para construir APIs con Python.
* **SQLAlchemy:** ORM (Object Relational Mapper) para interactuar con la base de datos.
* **Pydantic:** Librería para validación de datos.
* **Uvicorn:** Servidor ASGI para ejecutar la aplicación FastAPI.
* **SQLite:** Base de datos ligera y sin servidor utilizada en este ejemplo.

## Estructura del proyecto

* `main.py`: Punto de entrada de la aplicación FastAPI.
* `database.db`: Archivo de la base de datos SQLite.
* `requirements.txt`: Lista de dependencias de Python.
* `config/db.py`: Configuración de la conexión a la base de datos.
* `models/user.py`: Modelo de SQLAlchemy para la tabla de usuarios.
* `routers/user.py`: Rutas de la API relacionadas con los usuarios.
* `schemas/user.py`: Esquemas de Pydantic para la validación de datos de usuario.

## Cómo ejecutar el proyecto

Para ejecutar el proyecto, sigue estos pasos:

1.  **Crea un entorno virtual:**
    ```bash
    python3 -m venv venv
    ```

2.  **Activa el entorno virtual:**
    ```bash
    source venv/bin/activate
    ```

3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecuta la aplicación:**
    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8080
    ```

5.  **Accede a la interfaz de FastAPI:**
    Abre tu navegador y visita [http://localhost:8080/docs](http://localhost:8080/docs).
