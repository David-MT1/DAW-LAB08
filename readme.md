# DAW - LAB08: Django CRUD Destinos Turísticos

Proyecto Django que implementa un CRUD completo para destinos turísticos, usando la plantilla Travello.

## Estructura del Proyecto

```
DAW-LAB08/
├── project/          # Configuración del proyecto Django
├── travello/         # App principal
├── templates/        # Templates HTML
├── static/           # Archivos estáticos (CSS, JS, imágenes)
├── manage.py
├── requirements.txt
└── .gitignore
```

## Funcionalidades

- Listar destinos turísticos
- Añadir nuevo destino (con imagen)
- Modificar destino existente
- Eliminar destino
- Oferta especial (badge "Special Offer")

## Tecnologías

- Python 3.14
- Django 6.0
- SQLite
- Bootstrap 4
- HTML / CSS / JavaScript

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/David-MT1/DAW-LAB08.git
cd DAW-LAB08

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Hacer migraciones
python manage.py makemigrations
python manage.py migrate

# Correr el servidor
python manage.py runserver
```

## URLs disponibles

| Acción | URL |
|--------|-----|
| Inicio | `/travello/` |
| Agregar | `/travello/agregar/` |
| Modificar | `/travello/modificar/<id>/` |
| Eliminar | `/travello/eliminar/<id>/` |
| Admin | `/admin/` |

## Autor

David - [@David-MT1](https://github.com/David-MT1)