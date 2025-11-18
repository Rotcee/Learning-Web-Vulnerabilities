# Lab: DOM XSS in `document.write` sink using source `location.search`

## Statement

This lab contains a DOM-based cross-site scripting vulnerability in the search query tracking functionality. It uses the JavaScript `document.write` function, which writes data out to the page. The `document.write` function is called with data from `location.search`, which you can control using the website URL.

To solve this lab, perform a cross-site scripting attack that calls the `alert` function. 

## Walkthrough

 - ### **README**: Este laboratorio no funciona en el momento que estoy creando esto. Hasta que funcione esta seccion no tendra ninguna imagen
------
Que es el DOM? (hacer una breve explicacion y poner link para mas info)

En este laboratorio volvemos a tener la barra de busqueda vulnerable a XSS. Sin embargo ahora, al intentar que se interprete nuestro HTML o codigo javascript parece que no funciona.


Si abrimos la consola del navegador e inspeccionamos la barra de busqueda veremos que nuestro input se esta introduciendo en un campo `<img src="INPUT_HERE">`. Por lo que si en nuestro input ponemos una doble comilla y cerramos la etiqueta (`">`) lo que pongamos a continuacion se tomara como un campo nuevo, pudiendo ejecutar el `alert` y completando asi el laboratorio.