# Sistema de Inventario Basico

## Requisitos

-   Python 3.12+
-   pip

## Instalación

```bash
# Crear entorno virtual, python3 para linux
python -m venv env

# Activar entorno virtual
# Linux/macOS:
source ./env/bin/activate
# Windows:
env/Scripts/activate

# Instalar dependencias
pip install -r requirements.txt

# Migrar base de datos
python manage.py migrate
```

## Ejecutar

```bash
python manage.py runserver
```

Acceder a:

-   http://localhost:8000 - Aplicación
