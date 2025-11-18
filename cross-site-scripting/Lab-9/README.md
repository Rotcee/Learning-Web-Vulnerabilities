# Lab 9: Reflected XSS into a JavaScript string with angle brackets HTML encoded

## Statement

*This lab contains a reflected cross-site scripting vulnerability in the search query tracking functionality where angle brackets are encoded. The reflection occurs inside a JavaScript string. To solve this lab, perform a cross-site scripting attack that breaks out of the JavaScript string and calls the `alert` function.*

## Walkthrough

In this lab, the vulnerable field is again the article search bar. We can try different HTML injections and try to execute some script, but it will not work.

![No result](assets/1.png)

If we inspect the element, we will find the following script:

```js
var searchTerms = 'OUR-INPUT';
document.write('<img src="/resources/images/tracker.gif?searchTerms='+encodeURIComponent(searchTerms)+'">');
```

![script in inspector](assets/2.png)

We see that our input is being included in the javascript code, although the angle brackets are being encoded. We can try to use a quote to close the field and concatenate another instruction. We will also have to close the loose quote, creating another variable for example.

![payload](assets/3.png)

When you hit enter, the code will be entered into the script as follows:

![injected script](assets/4.png)

With this, we produce the `alert` and complete the lab.

![alert pops up](assets/5.png)

---
<div align="center">
  <a href="../Lab-8/README.md">⬅️ Previous Lab</a>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="../Lab-10/README.md">Next Lab ➡️</a>
</div>
