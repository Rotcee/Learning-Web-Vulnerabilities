# Lab 4: DOM XSS in `innerHTML` sink using source `location.search`

## Statement

This lab contains a DOM-based cross-site scripting vulnerability in the search blog functionality. It uses an `innerHTML` assignment, which changes the HTML contents of a `div` element, using data from `location.search`.

To solve this lab, perform a cross-site scripting attack that calls the `alert` function. 

## Walkthrough

En este laboratorio volvemos a encontrarnos la vulnerabilidad en la barra de busqueda. Al probar a escribir codigo HTML vemos que nos lo interpreta.

[1]

[2]

Sin embargo, al probar con un script, no se nos interpreta.

[3]

[4]

No obstante, tenemos otras formas de provocar un XSS. Una de ellas seria utilizar un `<img src>` que produzca un error. Por ejemplo 

```html
<img src=0 onerror=alert("XSS")>
```

`onerror` nos sirve para indicar que debe hacer cuando se produzca un error y interpreta codigo js, por lo que podemos introducir ahi nuestra instruccion. Al enviarlo vemos que se produce el XSS y completamos el laboratorio.

[5]