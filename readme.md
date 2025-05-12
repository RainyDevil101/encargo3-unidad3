# Encargo 3 / Evaluación Unidad 3: Aplicación Flask para Cálculo de Notas y Comparador de Nombres

Esta es una aplicación web desarrollada con Flask que consta de dos ejercicios:

- Un calculador de promedios con evaluación de aprobación según notas y asistencia
- Un comparador que identifica el nombre más largo entre tres opciones

## Requisitos previos

Antes de ejecutar la aplicación, es necesario tener instalado:

- Python 3.6 o superior - [Descargar Python](https://www.python.org/downloads/)
- pip (generalmente viene instalado con Python)

## Instalación

Sigue estos pasos para configurar el entorno y ejecutar la aplicación:

1. Clona o descarga este repositorio
2. Abre una terminal o línea de comandos
3. Navega hasta la carpeta del proyecto

```bash
cd ruta/a/la/carpeta
```

4. Instala las dependencias

```bash
pip install flask
```

## Estructura del proyecto

Asegúrate de que la estructura de archivos sea la siguiente:

```
proyecto/
│
├── main.py (o app.py)
├── templates/
│   ├── index.html
│   ├── ejercicio1.html
│   └── ejercicio2.html
└── static/
   └── css/
      └── style.css
```

## Ejecución de la aplicación

1. Ejecuta el archivo principal

```bash
python main.py
```

2. Abre un navegador web y ve a la siguiente dirección

```
http://127.0.0.1:5000/
```

3. Interactúa con la aplicación

- Selecciona "Ejercicio 1" para calcular promedios y evaluación
- Selecciona "Ejercicio 2" para comparar longitud de nombres

## Uso de Visual Studio Code (Opcional)

Si utilizas Visual Studio Code para desarrollar este proyecto:

1. Abre la carpeta del proyecto en VS Code
2. Instala la extensión de Python

- Busca "Python" en la pestaña de extensiones e instálala

## Ejercicios

### Ejercicio 1: Cálculo de Notas

- Ingresa 3 notas (entre 10 y 70)
- Ingresa el porcentaje de asistencia (entre 0 y 100)
- El sistema calculará el promedio y determinará si el estudiante está aprobado (promedio ≥ 40 y asistencia ≥ 75%)

### Ejercicio 2: Comparador de Nombres

- Ingresa 3 nombres diferentes
- El sistema identificará cuál es el nombre más largo y mostrará su longitud (cantidad de caracteres)

## Notas adicionales

- La aplicación está configurada en modo debug, lo que permite recargar automáticamente cuando se realizan cambios en el código