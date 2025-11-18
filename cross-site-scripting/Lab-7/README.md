# Lab 7: Reflected XSS into attribute with angle brackets HTML-encoded

## Statement

*This lab contains a reflected cross-site scripting vulnerability in the search blog functionality where angle brackets are HTML-encoded. To solve this lab, perform a cross-site scripting attack that injects an attribute and calls the `alert` function.*

## Walkthrough

In this lab, the vulnerability is again in the blog's search functionality. If we test for HTML injection, we see that nothing happens.

![No HTML injection](assets/1.png)

If we open the inspector (`Ctrl + Shift + c`), we will see that our input is being placed in a `value` attribute.

![Input in value attribute](assets/2.png)

We can try to use double quotes `"` to close the attribute and introduce our code, but we see that the angle brackets are encoded.

![Encoded angle brackets](assets/3.png)

![Encoded angle brackets in inspector](assets/4.png)

However, there are other instructions we can use to cause an XSS that do not require angle brackets, for example the `onmouseover` event, which specifies what will happen when the mouse is slid over the field. We can put our instruction there.

![onmouseover payload](assets/5.png)

When we send it, it will seem that nothing has happened, but when we pass the cursor over it, the `alert` will pop up, with which we will have completed the lab.

![Alert pops up](assets/6.png)

---
<div align="center">
  <a href="../Lab-6/README.md">⬅️ Previous Lab</a>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="../Lab-8/README.md">Next Lab ➡️</a>
</div>
