# Conversor de Texto a ASCII y Binario

El repositorio contiene un programa en Python que convierte cadenas de carateres a su correspondiente número en ASCII tanto en decimal como en binario, desplegando todo en un formato de tabla en $\LaTeX$.

## Uso 
### En Overleaf

1. Descargue el código de este repositorio.
    
    Forma simple: Use el botón verde `Code` **>** `Download ZIP` y después descomprima el ZIP.

2. Cree un nuevo proyecto en [Overleaf](https://es.overleaf.com/).

3. Suba el archivo [`ascii.py`](./fuentes/ascii.py) a su proyecto en Overleaf.

4. Use la siguiente línea en su archivo fuente de $\LaTeX$ :

    `\input{|python ascii.py Ejemplo Cadena}`

    Remplace `Ejemplo` y `Cadena` por el texto que desea convertir y al compilar obtendrá una tabla similar al [ejemplo](./ejemplo/ejemplo.pdf).

