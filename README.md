# webcloudforge-app

Bienvenido a webcloudforge.com


## Proyecto Dockerizado

Este proyecto utiliza **Docker Compose** para levantar un entorno completo que incluye **PostgreSQL**, **pgAdmin** y un **frontend**.  

---

### 🚀 Configuración inicial

1. Clonar el repositorio.  
2. Renombrar el archivo `.env_example` a `.env`.  
3. Completar las variables de entorno según la siguiente tabla.  

---

### 📌 Variables de entorno

| Variable                 | Tipo de dato | Descripción                                      | Ejemplo               |
|--------------------------|-------------|--------------------------------------------------|-----------------------|
| `POSTGRES_CONTAINER_NAME` | string      | Nombre del contenedor de PostgreSQL              | `postgres_db`         |
| `POSTGRES_PORT_EXPOSE`    | número      | Puerto expuesto para acceder desde el host       | `5432`                |
| `POSTGRES_PORT_INTERN`    | número      | Puerto interno del contenedor PostgreSQL         | `5432`                |
| `POSTGRES_PASSWORD`       | string      | Contraseña para el usuario de PostgreSQL         | `mysecretpassword`    |
| `POSTGRES_USER`           | string      | Usuario administrador de PostgreSQL              | `admin`               |
| `PGADMIN_POSTGRES_DB`     | string      | Base de datos por defecto accesible desde pgAdmin | `mydatabase`          |
| `PGADMIN_CONTAINER_NAME`  | string      | Nombre del contenedor de pgAdmin                 | `pgadmin`             |
| `PGADMIN_PORT_EXPOSE`     | número      | Puerto expuesto para pgAdmin en el host          | `8080`                |
| `PGADMIN_PORT_INTERN`     | número      | Puerto interno del contenedor pgAdmin            | `80`                  |
| `PGADMIN_DEFAULT_PASSWORD`| string      | Contraseña del usuario administrador de pgAdmin  | `admin123`            |
| `PGADMIN_DEFAULT_EMAIL`   | string (email)| Email de acceso a pgAdmin                       | `admin@admin.com`     |
| `FRONTEND_CONTAINER_NAME` | string      | Nombre del contenedor del frontend               | `frontend_app`        |
| `FRONTEND_HOST`           | string (url o ip)| Host donde se sirve el frontend                | `127.0.0.1`         |
| `FRONTEND_PORT_EXPOSE`    | número      | Puerto expuesto del frontend en el host          | `3000`                |
| `FRONTEND_PORT_INTERN`    | número      | Puerto interno del contenedor frontend           | `3000`                |

---

### ▶️ Levantar el entorno

Una vez completado el archivo `.env`, ejecutar:


```bash
docker compose up -d
```

### Terminar la ejecución 

```bash
docker compose down
```