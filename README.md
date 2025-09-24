# 📦 Proyecto Django - Sistema de Inventario

Este es un proyecto desarrollado con **Django 5** y **MySQL** que implementa un sistema de inventario con las siguientes aplicaciones:

- `categoria` → Gestión de categorías de productos.  
- `proveedor` → Gestión de proveedores.  
- `bodega` → Gestión de bodegas.  
- `producto` → Gestión de productos.  
- `movimiento` → Registro de movimientos de stock (entrada, salida, merma).  

---

## 🚀 Requisitos previos

Antes de comenzar, asegúrate de tener instalado:

- [Python 3.12+](https://www.python.org/downloads/)
- [MySQL Server](https://dev.mysql.com/downloads/)
- [Pip](https://pip.pypa.io/en/stable/)
- [Virtualenv](https://docs.python.org/3/library/venv.html)

---

## ⚙️ Instalación y configuración

1. **Clona el repositorio**
   ```bash
   git clone https://github.com/usuario/proyecto-inventario.git
   cd proyecto-inventario

2. Crea y activa un entorno virtual

python3 -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows (PowerShell)

3.Instala dependencias

pip install --upgrade pip
pip install -r requirements.txt

4. Crea la base de datos en MySQL
Entra a MySQL desde la terminal:

mysql -u root -p

5. Creación de la base de datos en MySQL
CREATE DATABASE evaluacion

6. Configura la conexión en settings.py
Edita evaluacion/settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'inventario',
        'USER': 'root',
        'PASSWORD': 'tu_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

6. Aplica las migraciones

python manage.py makemigrations
python manage.py migrate

7. Crea un superusuario (opcional, para usar /admin)

python manage.py createsuperuser

8. Ejecuta el servidor
python manage.py runserver
