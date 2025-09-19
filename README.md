# WebCloudForge.com - Portafolio Full-Stack Auto-Alojado

![Captura de pantalla de WebCloudForge.com](URL_DE_TU_CAPTURA_DE_PANTALLA.png)

**➡️ Ver Demo en Vivo: [https://webcloudforge.com/](https://webcloudforge.com/)**

---

## 🎯 La Misión de WebCloudForge

Este proyecto es más que un portafolio; es una prueba de concepto y una guía práctica. Nace de la misión de **forjar una solución web completa, segura y escalable sin depender de los altos costos y las arquitecturas cerradas de los servicios en la nube tradicionales.**

El objetivo es demostrar que cualquier desarrollador, con una inversión mínima y recursos propios (como una Raspberry Pi), puede construir y mantener una presencia online profesional, soberana y de alto rendimiento.

## ✨ Características Principales

* **Frontend Estático de Alto Rendimiento:** Una landing page construida con React y Vite, optimizada para una velocidad de carga instantánea.
* **Panel de Administración (Headless):** Una aplicación privada para gestionar todo el contenido del sitio (proyectos, habilidades, etc.) en tiempo real.
* **Infraestructura 100% Auto-Alojada (Self-Hosted):** Todo el sistema corre en una Raspberry Pi, utilizando Cloudflare Tunnels para una exposición segura a internet.
* **Seguridad por Diseño:** Implementación de reglas de firewall y mejores prácticas para mitigar ataques y scans de vulnerabilidades.

## 🛠️ Stack Tecnológico

* **Frontend:** React, Vite, Tailwind CSS
* **Backend:** Node.js, Express (*o las que elijas*)
* **Base de Datos:** PostgreSQL (*o la que elijas*)
* **Infraestructura:** Docker, Raspberry Pi, Ubuntu Server, Nginx, Cloudflare

---

## 🚀 Arrancar el Proyecto Localmente

Esta guía te permitirá levantar una réplica del entorno de `WebCloudForge` en tu máquina local usando Docker Compose.

### 1. Configuración Inicial

1.  Clona el repositorio: `git clone https://github.com/SoyLuisM/webcloudforge-app.git`
2.  Navega al directorio del proyecto: `cd webcloudforge-app`
3.  Renombra el archivo `.env_example` a `.env`.
4.  Completa las variables de entorno en el archivo `.env` según la siguiente tabla.

### 2. Variables de Entorno

| Variable | Descripción | Ejemplo |
|---|---|---|
| `POSTGRES_CONTAINER_NAME` | Nombre del contenedor de PostgreSQL | `postgres_db` |
| `POSTGRES_PORT_EXPOSE` | Puerto expuesto para acceder desde el host | `5432` |
| `POSTGRES_PORT_INTERN` | Puerto interno del contenedor PostgreSQL | `5432` |
| `POSTGRES_PASSWORD` | Contraseña para el usuario de PostgreSQL | `mysecretpassword` |
| `POSTGRES_USER` | Usuario administrador de PostgreSQL | `admin` |
| `PGADMIN_POSTGRES_DB` | Base de datos por defecto accesible desde pgAdmin | `mydatabase` |
| `PGADMIN_CONTAINER_NAME` | Nombre del contenedor de pgAdmin | `pgadmin` |
| `PGADMIN_PORT_EXPOSE` | Puerto expuesto para pgAdmin en el host | `8080` |
| `PGADMIN_PORT_INTERN` | Puerto interno del contenedor pgAdmin | `80` |
| `PGADMIN_DEFAULT_PASSWORD`| Contraseña del usuario administrador de pgAdmin | `admin123` |
| `PGADMIN_DEFAULT_EMAIL` | Email de acceso a pgAdmin | `admin@admin.com` |
| `FRONTEND_CONTAINER_NAME` | Nombre del contenedor del frontend | `frontend_app` |
| `FRONTEND_HOST` | Host donde se sirve el frontend | `127.0.0.1` |
| `FRONTEND_PORT_EXPOSE` | Puerto expuesto del frontend en el host | `3000` |
| `FRONTEND_PORT_INTERN` | Puerto interno del contenedor frontend | `3000` |

### 3. Levantar y Detener el Entorno

* Una vez completado el archivo `.env`, ejecuta para **iniciar**:
    ```bash
    docker compose up -d
    ```

* Para **detener** la ejecución:
    ```bash
    docker compose down
    ```

---

## 💬 Contacto

Si tienes alguna pregunta sobre el proyecto, ¡no dudes en contactarme!

* **LinkedIn:** https://www.linkedin.com/in/jorge-l-martinez-hernandez/
* **Email:** luismartinezh@webcloudforge.com
