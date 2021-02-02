En este directorio se encuentra el código fuente

## 📄 **Índice de Contenidos** 

- [ Formato ](#format)
- [ Preparación ](#preparation)
- [ Ejecución ](#run)


<a name="format"></a>
## 📚 **Formato** 

Hay varios tipos de ficheros, los cuales están diferenciados por el formato de su nombre.

* **cd<número>_cuaternion.py** corresponden a cada uno de los ejecicios resueltos en clases de prácticas utilizando matrices, que se conoce como Denavit-Hartenberg, pero en este caso son resueltos con cuaterniones.

* **cdX_cuaternion.py** y **cin_dir_x.py** corresponden a la resolución de la cinemática directa con cuaterniones y matrices respectivamente, pero a una escala mucho mayor y solo centrada en la cantidad de operaciones, lo que nos permite hacer las comparaciones entre ambos métodos.

<a name="preparation"></a>
## ⚙️ **Preparación** 

Debes instalar todas las dependencias que se encuentran en [requirements.txt](./requirements.txt)

Para ello, puedes crear y activar un entorno virtual, para que no haya conflicto con otras dependencias.

```bash
.../CD_Cuaternios/code » virtualenv entorno-rc -p python3 
.../CD_Cuaternios/code » source entorno-rc/bin/activate
```

Luego, instala todas las dependencias

```bash
.../CD_Cuaternios/code » pip install -r requirements.txt 
```

<a name="run"></a>
## 💾 **Ejecución** 

Hay varios manipuladores que se pueden ejecutar, que tienen el siguiente formato:

> ### **cd<número>_cuaternion.py**

Para ejecutar el primer ejemplo sería:

```bash
.../CD_Cuaternios/code » python cd1_cuaternion.py
```

