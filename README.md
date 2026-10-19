# Sistema de Gestión de Servicios — Autenticación, Sesiones y Seguridad

Este repositorio contiene la entrega correspondiente a la **Semana 6 de la Unidad 3** de la materia **AplicaWeb**. En esta práctica se implementa un sistema de autenticación propio utilizando `django.contrib.auth`, control de sesiones mediante cookies en servidor, aislamiento de datos por usuario y un checklist de seguridad para despliegue en producción.

---

## 🚀 Demo en Vivo

La aplicación se encuentra desplegada en Render y puede consultarse en el siguiente enlace:


---

## 🛠️ Tecnologías y Herramientas Utilizadas

* **Lenguaje:** Python 3.10+
* **Framework Web:** Django 5.x
* **Autenticación:** `django.contrib.auth` (Modelos `User`, `UserCreationForm`, `AuthenticationForm` y decorador `@login_required`)
* **Base de Datos:** SQLite (Local) / MySQL / PostgreSQL (Render)
* **Estilos:** Tailwind CSS (vía Play CDN)
* **Hosting / PaaS:** Render

---

## 📌 Funcionalidades Principales

1. **Gestión de Cuentas y Credenciales (`django.contrib.auth`)**:
   * Pantallas personalizadas de **Registro**, **Inicio de Sesión** y **Cierre de Sesión**.
   * Hashing seguro de contraseñas mediante PBKDF2 (ninguna credencial se almacena en texto plano).
   * Control de sesiones activas mediante identificadores seguros en cookies.
   * Mensajes flash (`django.contrib.messages`) para notificar eventos de éxito o cierre de sesión de forma dinámica.

2. **Aislamiento de Datos por Usuario**:
   * Cada registro creado en el sistema pertenece de forma exclusiva al usuario autenticado (`request.user`).
   * Las consultas a la base de datos y las restricciones en vistas evitan que un usuario pueda visualizar, editar o eliminar información ajena.

3. **Interfaz Adaptativa con Tailwind CSS**:
   * Tarjetas centradas y formularios estilizados para los procesos de autenticación y el CRUD de servicios.
   * Barra de navegación dinámica que detecta si el visitante es anónimo (`AnonymousUser`) o un usuario con sesión activa.

