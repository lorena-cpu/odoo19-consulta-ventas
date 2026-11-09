
# Consulta de Ventas - Odoo 19

## Descripción

Módulo personalizado para Odoo 19 que permite
consultar los pedidos de venta confirmados de un
cliente durante un mes mediante una API HTTP.

## Objetivo

Demostrar la extensión de un ERP mediante su
arquitectura modular, reutilizando las funcionalidades
del módulo Sales sin modificar el núcleo de Odoo.

## Tecnologías

- Odoo 19
- Python
- PostgreSQL
- API HTTP con respuestas JSON
- OpenAPI 3.0
- Git y GitHub

## Arquitectura

El proyecto utiliza la arquitectura modular de Odoo,
basada en módulos o addons.

El módulo consulta_ventas depende de:
- base: funcionalidades principales de Odoo.
- sale: gestión de pedidos de venta.

La API se implementa en un controlador Python y
utiliza el ORM de Odoo para consultar sale.order.

## Endpoint

GET /api/consulta-ventas

Parámetros:
- cliente_id: identificador del cliente.
- anio: año de consulta.
- mes: mes de consulta (1 al 12).

Ejemplo:

http://localhost:8069/api/consulta-ventas?cliente_id=6&anio=2026&mes=11

## Resultado de prueba

Cliente: Cliente prueba

Periodo: noviembre de 2026

Cantidad de pedidos confirmados: 1

Total: S/ 118.00

## Seguridad

La API requiere una sesión autenticada de Odoo.

Se comprueba la pertenencia al grupo de usuarios
de Ventas y se respetan los permisos del ORM.

## Pruebas realizadas

- Consulta mensual correcta.
- Validación de parámetros obligatorios: HTTP 400.
- Redirección al login sin autenticación.
- Acceso denegado sin permisos de Ventas: HTTP 403.

## Documentación OpenAPI

Consultar docs/openapi.yaml.

## Instalación

1. Tener Odoo 19 con PostgreSQL.
2. Instalar el módulo Sales.
3. Copiar consulta_ventas al directorio de addons personalizados.
4. Incorporar esa ruta en addons_path de odoo.conf.
5. Reiniciar el servicio de Odoo.
6. Actualizar la lista de aplicaciones.
7. Instalar Consulta de Ventas.

No incluir contraseñas ni configuraciones privadas
en el repositorio.
