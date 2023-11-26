# Analizador Sintactico Ascendente SQL


__Este es el repositorio de:__


- Muñoz Tapia Alan Arath

- Reyes López Maximiliano

- Santos Alan Eduardo

__Gramatica Utilizada:__

1. Q → **select** D **from** T
2. D → **distinct** P | P
3. P → * | A
4. A → A __,__ A<sub>1</sub> | A<sub>1</sub>
5. A<sub>1</sub> → __id__ A<sub>2</sub>
6. A<sub>2</sub> → __.__ __id__ | Ɛ
7. T → T __,__ T<sub>1</sub> | T<sub>1</sub>
8. T<sub>1</sub> → __id__ T<sub>2</sub>
9. T<sub>2</sub> → __id__ | Ɛ

__Analizar un archivo de texto__

- Para ejecutar `python3 main.py nombre_archivo.txt`

__Analizar texto directamente desde la terminal__

- Para ejecutar `python3 main.py`, ahora solo hay que usar la terminal para introducir las cadenas que se desean analizar. Para salir hay que usar la combinación `ctrl + C`