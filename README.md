<div align="center">

# 🎓 Sistema de Gestión de Estudiantes con Persistencia de Datos

**Solución Modular en Python para Administración de Estudiantes con Persistencia en Archivos CSV**

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Storage: CSV](https://img.shields.io/badge/Storage-CSV-2ea44f?style=for-the-badge&logo=csv)](https://en.wikipedia.org/wiki/Comma-separated_values)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

</div>

---

## 📖 Descripción

**Sistema de Gestión de Estudiantes con Persistencia de Datos** es una solución integral en **Python 3** diseñada para satisfacer las necesidades de administración de registros estudiantiles, permitiendo operaciones CRUD completas en memoria y persistencia bidireccional mediante archivos estructurados en formato **CSV**.

El proyecto se estructura con una clara separación entre la interfaz de usuario en consola (`app.py`), los servicios de lógica de negocio y validación (`services.py`), la capa de acceso y manejo de archivos (`files.py`) y el almacén del estado en memoria (`students.py`).

---

## 🚀 Características Principales

- **Gestión Estudiantil Completa (CRUD):**
  - **Registrar nuevos estudiantes:** Captura de ID, nombre, edad, curso y estado académico (`active` / `inactive`).
  - **Consultar listado general:** Presentación tabulada de todos los estudiantes registrados.
  - **Buscar estudiante:** Localización rápida por documento de identificación.
  - **Actualizar datos:** Edición controlada de nombre, edad, curso y estado.
  - **Eliminar estudiante:** Baja de registros de la lista activa.
- **Persistencia en Archivos CSV:**
  - **Guardar en CSV:** Exporta el listado en memoria directamente al archivo `data/students_list.csv`.
  - **Cargar desde CSV:** Importa automáticamente registros previos al iniciar o por comando del usuario.
- **Arquitectura Limpia y Modular:** Código ordenado por responsabilidades para facilitar el mantenimiento y la extensibilidad.

---

## 📂 Estructura del Proyecto

```text
Sistema-de-Gestion-de-Estudiantes-con-Persistencia-de-Datos/
├── app.py                      # Menú principal y flujo de usuario
├── data/
│   └── students_list.csv       # Archivo CSV de persistencia de datos
├── files.py                    # Operaciones de lectura y escritura en CSV
├── services.py                 # Lógica de negocio y validaciones CRUD
├── students.py                 # Almacén de estudiantes en memoria
├── LICENSE                     # Licencia MIT
└── README.md                   # Documentación técnica
```

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.x**
- **CSV Built-in Library**

---

## ⚙️ Puesta en Marcha

### 1. Clonar el repositorio
```bash
git clone https://github.com/Danilo-Doria/Sistema-de-Gestion-de-Estudiantes-con-Persistencia-de-Datos.git
cd Sistema-de-Gestion-de-Estudiantes-con-Persistencia-de-Datos
```

### 2. Ejecutar el programa
```bash
python3 app.py
```

### 3. Opciones Disponibles
1. Registrar nuevo estudiante
2. Consultar lista de estudiantes
3. Buscar estudiante por ID
4. Actualizar datos de un estudiante
5. Eliminar estudiante
6. Guardar en archivo CSV
7. Cargar desde archivo CSV
8. Salir

---

## 👨💻 Author

- GitHub: **[Danilo-Doria](https://github.com/Danilo-Doria)**
- LinkedIn: **[Danilo Doria Diaz](https://www.linkedin.com/in/danilo-doria-diaz)**
- Mail: **danilodoria519@gmail.com**

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
