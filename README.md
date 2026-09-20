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

Primero se debe clonar el repositorio:
    git clone URL_DEL_REPOSITORIO

Después, ingresar a la carpeta del proyecto:
    cd Cambio-clim-tico

Crear un entorno virtual:
    python -m venv venv

Activarlo en Windows:
    venv\Scripts\activate

En macOS o Linux:
    source venv/bin/activate

Instalar las dependencias:
    pip install -r requirements.txt

El archivo requirements.txt debe contener:
    Flask
    
5. Configuración

El proyecto no necesita variables de entorno, archivos .env ni conexiones con bases de datos.

El logo debe guardarse en la siguiente ubicación:
    static/images/ecohuella.svg

Las imágenes de las tarjetas se obtienen desde enlaces externos de Unsplash, por lo que se necesita conexión a internet para visualizarlas.

Durante el desarrollo, Flask se ejecuta con el modo de depuración activado:
    app.run(debug=True)

El modo de depuración permite ver los errores y reiniciar automáticamente el servidor cuando se modifica el código. No se recomienda activarlo al publicar una página para uso real.

6. Estructura del proyecto

./
├── static/
|    ├── css/
|        └── style.css
|    └── images/
|        └── ecohuella.svg
├── templates/
|   └── index.html
├── tests/
│   └── test_main.py
├── main.py
├── requirements.txt 
└── README.md

**Función de cada uno**

main.py: contiene el servidor, calcula el puntaje y crea las recomendaciones.
templates/index.html: contiene la estructura y el contenido de la página.
static/css/style.css: contiene los colores, tamaños, espacios y diseño.
static/images/ecohuella.svg: contiene el logo de EcoHuella.
requirements.txt: indica las librerías que deben instalarse.
README.md: explica el funcionamiento y la instalación del proyecto.

7. Uso y ejecución

Para iniciar la página se debe ejecutar:
    python main.py

Después, abrir en el navegador:
    http://127.0.0.1:5000

Para detener el servidor, se puede presionar **Ctrl + C** en la terminal.

8. Pruebas

Explicar cómo ejecutar las pruebas.

pytest

9. Contribución

Explicar cómo pueden contribuir otros desarrolladores al proyecto.
10. Licencia

Indicar la licencia utilizada por el proyecto.
