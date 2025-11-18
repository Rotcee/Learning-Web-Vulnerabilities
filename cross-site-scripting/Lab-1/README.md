# Lab 1: Reflected XSS into HTML context with nothing encoded

## Statement

This lab contains a simple reflected cross-site scripting vulnerability in the search functionality.

To solve the lab, perform a cross-site scripting attack that calls the `alert` function. 

## Walkthrough

Al entrar al laboratorio nos encontramos con un blog con seccion de busqueda. La si probamos a introducir codigo HTML en la barra de busqueda, vemos que se ejecuta.

[1]

[2]

Probamos a poner codigo javascript para ver si nos lo interpreta

[3]

Al darle a buscar el codigo js es interpretado y nos aparece el `alert`

[4]

Con esto hemos completado el laboratorio.