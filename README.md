# SENA APP - Portal Institucional

Un portal web completo para la gestión de aprendices, instructores, programas de formación y cursos en SENA.

## 🎯 Características Principales

### Módulos Implementados

#### 👨‍🎓 **Aprendices**

- Listado completo de aprendices registrados
- Vista detallada de cada aprendiz
- Crear nuevo aprendiz
- Editar información de aprendices
- Eliminar aprendices con confirmación
- Búsqueda y filtrado

#### 👨‍🏫 **Instructores**

- Gestión completa de instructores
- Información detallada: nivel educativo, especialidad, años de experiencia
- CRUD completo (Crear, Leer, Actualizar, Eliminar)
- Validación de datos en formularios
- Estado de actividad (Activo/Inactivo)

#### 📚 **Programas de Formación**

- Catálogo de programas disponibles
- Detalles de cada programa: nivel, modalidad, duración
- Gestión de centros de formación y regionates
- Requisitos de ingreso y perfil de egreso
- CRUD completo

#### 🎓 **Cursos**

- Listado de cursos activos y programados
- Información del programa y instructor coordinador
- Control de cupos (aprendices inscritos/máximo)
- Estado del curso
- Horarios y ambientes
- CRUD completo

## 🛠️ Tecnologías Utilizadas

- **Backend:** Django 4.2.26
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Base de Datos:** SQLite3
- **Python:** 3.10+
- **Formularios:** Django Forms con Bootstrap styling
- **JavaScript:** Bootstrap Bundle para interactividad

## 📋 Requisitos Previos

- Python 3.10 o superior
- pip (gestor de paquetes de Python)
- Git (opcional, para clonar el repositorio)

## 🚀 Instalación y Configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/TattysB/SENA_APP.git
cd SENA_APP
```

### 2. Crear un entorno virtual

```bash
# En Windows
python -m venv env
env\Scripts\activate

# En macOS/Linux
python3 -m venv env
source env/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar la base de datos

```bash
cd SENA_APP
python manage.py migrate
```

### 5. Crear un superusuario (admin)

```bash
python manage.py createsuperuser
```

### 6. Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

El servidor estará disponible en: `http://localhost:8000`

## 📁 Estructura del Proyecto

```
SENA_APP/
├── env/                          # Entorno virtual
├── SENA_APP/                     # Configuración principal
│   ├── settings.py               # Configuraciones de Django
│   ├── urls.py                   # URLs principales
│   ├── wsgi.py                   # Configuración WSGI
│   └── asgi.py                   # Configuración ASGI
├── aprendices/                   # Aplicación de Aprendices
│   ├── models.py                 # Modelo Aprendiz
│   ├── views.py                  # Vistas y lógica
│   ├── urls.py                   # URLs de aprendices
│   ├── forms.py                  # Formularios
│   ├── templates/                # Plantillas HTML
│   │   ├── main.html
│   │   ├── master.html
│   │   ├── aprendices_list.html
│   │   └── detalle_aprendiz.html
│   ├── migrations/               # Migraciones de BD
│   └── static/                   # Archivos estáticos
├── instructores/                 # Aplicación de Instructores
│   ├── models.py                 # Modelo Instructor
│   ├── views.py                  # Vistas CRUD
│   ├── forms.py                  # Formularios
│   ├── urls.py                   # URLs namespaced
│   └── templates/                # Plantillas HTML
│       ├── lista_instructores.html
│       ├── instructor_detalle.html
│       ├── agregar_instructor.html
│       ├── editar_instructor.html
│       └── eliminar_instructor.html
├── programas/                    # Aplicación de Programas
│   ├── models.py                 # Modelo Programa
│   ├── views.py                  # Vistas CRUD
│   ├── forms.py                  # Formularios
│   ├── urls.py                   # URLs namespaced
│   ├── fixtures/                 # Datos iniciales
│   └── templates/                # Plantillas HTML
├── cursos/                       # Aplicación de Cursos
│   ├── models.py                 # Modelo Curso
│   ├── views.py                  # Vistas CRUD
│   ├── forms.py                  # Formularios
│   ├── urls.py                   # URLs namespaced
│   └── templates/                # Plantillas HTML
├── db.sqlite3                    # Base de datos SQLite
├── manage.py                     # Utilidad de Django
└── requirements.txt              # Dependencias del proyecto
```

## 🔐 URLs Principales

### Navegación

- `/` - Página principal
- `/aprendices/` - Listado de aprendices
- `instructores:lista_instructores` - Listado de instructores
- `programas:programas` - Listado de programas
- `cursos:lista_cursos` - Listado de cursos

### CRUD Aprendices

- `/aprendices/crear/` - Crear aprendiz
- `/aprendices/<id>/editar/` - Editar aprendiz
- `/aprendices/<id>/eliminar/` - Eliminar aprendiz
- `/aprendices/aprendiz/<id>/` - Detalle de aprendiz

### CRUD Instructores

- `instructores:crear_instructor` - Crear instructor
- `instructores:editar_instructor` - Editar instructor
- `instructores:eliminar_instructor` - Eliminar instructor
- `instructores:detalle_instructor` - Detalle de instructor

### CRUD Programas

- `programas:crear_programa` - Crear programa
- `programas:editar_programa` - Editar programa
- `programas:eliminar_programa` - Eliminar programa
- `programas:detalle_programa` - Detalle de programa

### CRUD Cursos

- `cursos:crear_curso` - Crear curso
- `cursos:editar_curso` - Editar curso
- `cursos:eliminar_curso` - Eliminar curso
- `cursos:detalle_curso` - Detalle de curso

## 👥 Modelos de Datos

### Aprendiz

- document_id (CharField, único)
- firstname, lastname
- phone, email
- birthdate (DateField)
- city
- program

### Instructor

- tipo_documento
- documento_id (único)
- nombre, apellido
- telefono, correo
- fecha_nacimiento
- ciudad, dirección
- nivel_educativo (Choices: TEC, TEG, PRE, ESP, MAE, DOC)
- especialidad
- años_experiencia (IntegerField)
- activo (BooleanField)
- fecha_vinculación
- fecha_registro

### Programa

- codigo (único)
- nombre
- nivel_formacion (Choices)
- modalidad (Choices)
- duracion_meses, duracion_horas
- centro_formacion
- regional
- estado (Choices)
- descripción
- competencias
- perfil_egreso
- requisitos_ingreso

### Curso

- codigo (único)
- nombre
- programa (ForeignKey)
- instructor_coordinador (ForeignKey)
- fecha_inicio, fecha_fin
- horario
- aula
- cupos_maximos
- estado (Choices)
- observaciones

## 🎨 Diseño y UX

- **Responsivo:** Compatible con dispositivos móviles y desktop
- **Bootstrap 5:** Framework CSS moderno y accesible
- **Modales:** Confirmación de eliminación con Bootstrap modals
- **Formularios Validados:** Validación client-side y server-side
- **Tabla Responsiva:** Tabla en desktop, cards en móvil

## ⚙️ Configuración Importante

### settings.py

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap5',
    'aprendices',
    'instructores',
    'programas',
    'cursos',
]
```

### URLs Namespaced

Cada aplicación tiene su propio namespace para evitar conflictos:

- `aprendices:`
- `instructores:`
- `programas:`
- `cursos:`

## 🐛 Troubleshooting

### Error: Port 8000 already in use

```bash
python manage.py runserver 8080  # Usar otro puerto
```

### Error: Database locked

```bash
rm db.sqlite3
python manage.py migrate
```

### Cambios no se reflejan

```bash
python manage.py collectstatic --clear --noinput
```

## 📝 Notas de Desarrollo

- Todas las vistas CRUD usan Class-Based Views para mejor mantenimiento
- Los formularios incluyen validación de datos
- Las plantillas heredan de `master.html` para consistencia
- Se usa Bootstrap 5 para estilos uniformes
- URLs namespaced para mejor organización

## 🔒 Seguridad

- CSRF Protection habilitada
- SQL Injection prevenida con ORM de Django
- Validación de formularios en cliente y servidor
- Confirmación modal para acciones destructivas

## 📞 Contacto y Soporte

Proyecto desarrollado para SENA - Servicio Nacional de Aprendizaje

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

---

**Última actualización:** Diciembre 2025
**Versión:** 1.0.0
