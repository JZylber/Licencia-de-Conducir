# Licencia de Conducir

## Introducción
Muchos de ustedes van a sacar la licencia este año. ¿Saben los lugares para hacer los distintos trámites? Para eso, el gobierno de la ciudad nos pidió que hagamos un boceto de aplicación que permita consultar por sedes en base a barrio o en base a la actividad, y que registre las impresiones (vistas) de cada sede. El programa fue terminado, pero se le pidió a *Chano* que lo lleve, chocó, y ¡Perdimos algunas funciones! Ahora queda arreglar el programa con las funciones faltantes.

## Explicación del programa
1. Se toma un archivo csv con la información de las sedes (`cargar_csv`)
2. Con los datos, se construye una lista de sedes, donde cada sede es un diccionario:
    ```python
    Sede = {
    'nombre': str,
    'actividad': str,
    'direccion': str,
    'barrio': str,
    'impresiones': int
    }
    ```
   `impresiones` no se incluye, solo aparece si al menos alguien averigua por dicha sede.

3. Se construyen otros 2 diccionarios a modo de índice:
   - `sedes_por_barrio`: Toma la lista de sedes, y construye un diccionario con pares `barrio:lista de sedes`
   - `sedes_por_actividad`: Toma la lista de sedes, y construye un diccionario con pares `actividad:lista de sedes`
4. Se le pide al usuario que ingrese una opcion, entre elegir por barrio, por actividad, o terminar el programa
5. En caso de que se elija barrio o actividad, se llama a la función `seleccionar_desde_opciones` que permite seleccionar una sede desde alguno de los diccionarios índice (`por barrio` o `por actividad`)
6. Se muestra la información de la sede y se marca la impresión/vista
7. Al finalizar el programa, se muestran los nombres de las sedes y sus impresiones/vistas.

## Consigna

Reconstruir el programa creando las funciones perdidas:
- `sedes_por_barrio`: Toma la lista de sedes, y construye un diccionario con pares `barrio:lista de sedes`.
- `sedes_por_actividad`: Toma la lista de sedes, y construye un diccionario con pares `actividad:lista de sedes`.
- `marcar_impresion`: Toma una sede y marca que alguien realizó una impresión/vista. Recuerden que las sedes no tienen la clave `impresiones` si nadie consultó por ella hasta ahora.

## Extra
1. `sedes_por_barrio` y `sedes_por_actividad` son muy parecidas. ¿Se animan a hacerlas una única función?
2. Opciones 1 y 2 son muy parecidas. Modificar el programa para que no haga falta usar `if` para distinguir entre opciones 1 y 2, osea, en vez de tener
    ```python
    if opcion == 1:
        # Cosas que hace opcion 1
    elif opcion == 2:
        # Cosas que hace opcion 2
    elif opcion == 3:
        # Terminar el programa
    ```
    tener algo así:
    ```python
    if opcion >= 1 and opcion <= 2:
        # Cosas que hace opcion 1 o opcion 2
    elif opcion == 3:
        # Terminar el programa
    ```