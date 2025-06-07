# Sistema de Inventario Basico

## Requisitos

-   Python 3.12+
-   pip

## Instalación

```bash
# Clonar y entrar al proyecto
git clone <url-del-repositorio>
cd TechTest

# Crear entorno virtual
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

# Crear superusuario (opcional)
python manage.py createsuperuser
```

## Ejecutar

```bash
python manage.py runserver
```

Acceder a:

-   http://localhost:8000 - Aplicación
