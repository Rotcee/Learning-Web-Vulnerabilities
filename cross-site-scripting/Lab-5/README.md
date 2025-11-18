# Lab 5: DOM XSS in jQuery anchor `href` attribute sink using `location.search` source

## Statement

This lab contains a DOM-based cross-site scripting vulnerability in the submit feedback page. It uses the jQuery library's `$` selector function to find an anchor element, and changes its `href` attribute using data from `location.search`.

To solve this lab, make the "back" link alert `document.cookie`. 

## Walkthrough

En este laboratorio la vulnerabilidad se encuentra en la submit feedback page. Si accedemos a ella veremos que en la parte inferior hay un boton `Back` que nos devuelve a la raiz

[1]

Si abrimos la consola y inspeccionamos el boton observamos lo siguente

[2]

que es lo mismo que vemos en la URL

[3]

Esto nos hace pensar si puede ser que podamos modificar el `returnPath` para que nos ejecute una instruccion en js. Podemos probar con `javascript:alert("XSS")`.

[4]

Tras recargar la pagina completamos el laboratorio. Si hacemos hovering sobre el boton de `Back` veremos que si hacemos click en el nos ejecutara la instruccion en javascript.

[5]

[6]