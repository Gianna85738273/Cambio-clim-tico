# Cambio-clim-tico
Proyecto final

1. Descripción

EcoHuella es una página web educativa creada con el propósito de hacer que las personas realicen un cambio en sus hábitos diarios.

Dentro de esta podemos encontrar un cuestionario sobre transporte, consumo de energía y manejo de residuos. Este, según las respuestas seleccionadas, calcula un puntaje de impacto ambiental entre 0 y 6:
- De 0 a 2 puntos: impacto bajo.
- De 3 a 4 puntos: impacto medio.
- De 5 a 6 puntos: impacto alto.
Luego de mostrar el resultado, la página muestra recomendaciones personalizadas para reducir el daño generado.
Los resultados no son científicos, sino que son orientativos y educativos.

2. Tecnologías utilizadas

El proyecto fue desarrollado usando:
    Python: procesa las respuestas, calcula el puntaje y genera las recomendaciones.
    Flask: framework utilizado para crear el servidor y conectar Python con la página web.
    HTML5: organiza el contenido y la estructura de la página.
    CSS3: controla los colores, tamaños, espacios y diseño adaptable.
    Jinja2: permite mostrar en el HTML los resultados calculados por Python.

Librerías utilizadas:
    Flask
Jinja2 se instala automáticamente junto con esta.

Base de datos
    Este proyecto no utiliza una base de datos. Las respuestas solo se procesan en el momento y no quedan guardadas.

3. Requisitos previos

Para ejecutar el proyecto se necesita:
    Python 3.x instalado (cualquier versión de Python que se encuentre en la familia de 3).
    pip, incluido normalmente con Python.
    Git, si se desea clonar el repositorio.
    Un navegador web actualizado.
    Conexión a internet para visualizar las fotografías externas.
    Un editor de código, como Visual Studio Code, de manera opcional.
    4. Instalación

Explicar los pasos para instalar y configurar el proyecto.

git clone URL_DEL_REPOSITORIO
cd NOMBRE_DEL_PROYECTO

5. Configuración

Explicar las variables de entorno, archivos .env y demás configuraciones necesarias.
6. Estructura del proyecto

proyecto/
├── src/
├── tests/
├── requirements.txt
├── .env.example
├── main.py
└── README.md

7. Uso y ejecución

Explicar cómo ejecutar el proyecto.

python main.py

8. Pruebas

Explicar cómo ejecutar las pruebas.

pytest

9. Contribución

Explicar cómo pueden contribuir otros desarrolladores al proyecto.
10. Licencia

Indicar la licencia utilizada por el proyecto.
