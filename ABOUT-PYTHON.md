# Sobre Python

Respuestas a preguntas sobre python

1.  Python es un lenguajes de programación interpretado multipropósito y multiparadigma de alto nivel.
2.  Python fué creado por Guido Van Rossum en 1991.
3.  Python es un tipo de lenguaje interpretado, fuertemente tipado y dinámico.
4.  int, float, string, boolean, lists, tuple, dictionary.
5.  Python soporta paradigmas: imperativo, orientado a objetos y funcional.
6.  Código abajo:
```python
class Ejemplo:
    __init__(self):
        self._contador = 0
```
7. Es un dunder (método especial de python) que permite definir un constructor para la clase donde se encuentra.
8. Es un dunder de python que permite especificar código a ejecutar en el momento en que todas las refencias al objeto creado a partir de dicha clase son eliminadas, es decir, cuando el objeto es alcanzado por el garbage collector.
9. Es una referencia a la instancia que será creada a partir de la clase. Self es una especie de equivalente a `this` en otros lenguajes de programación.
10. Un iterable es un objeto que implementa el dunder `__iter__` normalmente estos objetos devuelven otro objeto que implementa el dunder `__next__`.
11. En python podemos escribir comentarios sintácticamente de tres formas distintas:
    1.  Comentario de una sola línea (código abajo):
    ```python
    # Esto es un comentario de una sola línea
    ```
    2.  Multilinea se interpretan como PyDocs si estos se encuentran en la primera línea del blóque que documentan, dentro de estos comentarios podemos insertar **doctests** que normalmente sirven para documentar ejemplos de uso (Código abajo):
    ```python
    '''
    Esto es un 
    comentario
    multilinea
    '''
    ```
    3. Multilinea (Código abajo):
    ```
    """
    Esto es un
    comentario
    multilinea 
    """ 
    ``` 
12. Un decorador es sugar sintaxt que permite definir una funcion que envuelve a otra y normalmente se utiliza para poder realizar tareas antes o después que se ejecute la función decorada o simplemente para modificar la salida de dicha función. Una forma básica de decoradores es:
```python
def decorator(func):
    def wrapper(*args, **kargs):
        # TODO before code
        return func(*args, **kargs)
    
    return wrapper

@decorator
def decorated(arg):
    # TODO something
    return something
```
13. Son los **python enhancement proposal** y son propuestas para mejorar el lenguaje. El **PEP-8** define la guía de estilos.
14. Entiendo que puede ser una función en python. Si no es lo anterior, entonces desconosco.
15. El **PEP-0** define un índice de todos los demás **PEP**