from typing import List, Optional
import uuid
from pydantic import EmailStr
from sqlmodel import Field, Relationship, SQLModel

# === Tablas Intermedias (Link Models) para M:N ===

class UsersCatTecnoLink(SQLModel, table=True):
    """M:N Link entre Users y CatTecnologias"""
    __tablename__ = "users_cat_tecno"
    # id no es estrictamente necesario, pero lo mantengo por tu esquema
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    id_users: uuid.UUID = Field(foreign_key="users.id")
    id_cat_tecnologias: uuid.UUID = Field(foreign_key="cat_tecnologias.id")


class ServiciosCatTecnoLink(SQLModel, table=True):
    """M:N Link entre Servicios y CatTecnologias"""
    __tablename__ = "servicios_cat_tecno"
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    id_servicios: uuid.UUID = Field(foreign_key="servicios.id")
    id_cat_tecnologias: uuid.UUID = Field(foreign_key="cat_tecnologias.id")


class ProyectosCatTecnoLink(SQLModel, table=True):
    """M:N Link entre Proyectos y CatTecnologias"""
    __tablename__ = "proy_cat_tecno"
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    id_proyecto: uuid.UUID = Field(foreign_key="proyectos.id")
    id_cat_tecnologias: uuid.UUID = Field(foreign_key="cat_tecnologias.id")

# ---

# === Catálogos ===

class CatTecnologia(SQLModel, table=True):
    """Modelo para la tabla cat_tecnologias."""
    __tablename__ = "cat_tecnologias"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    icono: str
    titulo: str
    descripcion: str

    # Relaciones M:N con back_populates a las tablas principales
    usuarios: List["Users"] = Relationship(
        back_populates="tecnologias", link_model=UsersCatTecnoLink
    )
    servicios: List["Servicios"] = Relationship(
        back_populates="tecnologias", link_model=ServiciosCatTecnoLink
    )
    proyectos: List["Proyectos"] = Relationship(
        back_populates="tecnologias", link_model=ProyectosCatTecnoLink
    )

# ---

# === Modelos de Contenido Relacionado (1:N) ===

class Servicios(SQLModel, table=True):
    """Modelo para la tabla servicios."""
    __tablename__ = "servicios"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    
    # Clave Foránea a Users
    id_user: uuid.UUID = Field(foreign_key="users.id")
    
    icon: str
    titulo: str

    # Relación N:1 con Users
    user: Optional["Users"] = Relationship(back_populates="servicios")

    # Relación M:N con CatTecnologia
    tecnologias: List[CatTecnologia] = Relationship(
        back_populates="servicios", link_model=ServiciosCatTecnoLink
    )


class Proyectos(SQLModel, table=True):
    """Modelo para la tabla proyectos."""
    __tablename__ = "proyectos"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    
    # Clave Foránea a Users
    id_user: uuid.UUID = Field(foreign_key="users.id")
    
    img: str
    titulo: str
    descripcion: str
    repositorio: str
    demo: str

    # Relación N:1 con Users
    user: Optional["Users"] = Relationship(back_populates="proyectos")

    # Relación M:N con CatTecnologia
    tecnologias: List[CatTecnologia] = Relationship(
        back_populates="proyectos", link_model=ProyectosCatTecnoLink
    )


class Contactos(SQLModel, table=True):
    """Modelo para la tabla contactos."""
    __tablename__ = "contactos"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    
    # Clave Foránea a Users
    id_user: uuid.UUID = Field(foreign_key="users.id")
    
    titulo: str
    url: str
    icono: str

    # Relación N:1 con Users
    user: Optional["Users"] = Relationship(back_populates="contactos")


class Experiencia(SQLModel, table=True):
    """Modelo para la tabla experiencia."""
    __tablename__ = "experiencia"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    
    # Clave Foránea a Users
    id_user: uuid.UUID = Field(foreign_key="users.id")
    
    puesto: str
    empresa: str
    periodo: str
    descripcion: str

    # Relación N:1 con Users
    user: Optional["Users"] = Relationship(back_populates="experiencia")


class Educacion(SQLModel, table=True):
    """Modelo para la tabla educacion."""
    __tablename__ = "educacion"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    
    # Clave Foránea a Users
    id_user: uuid.UUID = Field(foreign_key="users.id")
    
    escuela: str
    carrera: str
    fecha: str
    descripcion: str

    # Relación N:1 con Users
    user: Optional["Users"] = Relationship(back_populates="educacion")
