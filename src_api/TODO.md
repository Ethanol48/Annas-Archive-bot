cuando se le llame al API que utilice los distintos mirros que haya de anna's archive, tener una lista de links en un .txt o algo y que python parse por encima, 

default: 

```
  annas*.org

  if requests.get(annas.org).status_code != 200:

    parse the list(.txt):

      requests hasta que uno funcione

    y cuando uno funcione se añade a la lista de formato:
    y cambiar la lista

    link1: False
    link2: False
    link3: False 
    link4: True

    if ninguno funciona

   soltar un erro que hay un problema con annas-archive
  ```

(lo de arriba en una función para poder llamar cada vez y checar cada vez si el link es válido)

cuando el default link no va, variable global que indique de utilizar otro, a lo mejor utilizar una función que te de el link en sí. 
