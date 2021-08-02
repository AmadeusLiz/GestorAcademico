# GestorAcademico
GESTOR ACADÉMICO, NEGOCIOS WEB 2002 | EQUIPO 5

Usuario: admin
Contraseña: 123abcd!

## Requisitos
Dentro del entorno activo hacer la instalación siguiente:
- ```(entorno1) C:\entornos\entorno1>pip install django-phone-field```
- ```(entorno1) C:\entornos\entorno1>pip install Pillow```
##Diagramas
Flujo de los alumnos:
```mermaid 
graph LR;
    A[Login] --> B{Alumno?}
    B -- Si --> C[Menu Normal]
    C --> E{Opciones}
    E -- Notas -->F[Ver Notas]
    E -- Perfil -->G[Ver Perfil o Editar]
    E -- Clases -->H[Ver Clases Matriculadas]
    E -- Matricula --> I[Agregar clases]
    E -- LogOut -->A
    B -- No --> D[No entras]
    D --> A
```