# Lab 8: Stored XSS into anchor `href` attribute with double quotes HTML-encoded

## Statement

*This lab contains a stored cross-site scripting vulnerability in the comment functionality. To solve this lab, submit a comment that calls the `alert` function when the comment author name is clicked.*

## Walkthrough

In this lab, we again have an XSS vulnerability present in the comment functionality of the posts. We will enter any comment to see how the data is stored.

![Submitting a comment](assets/1.png)

If we inspect our own comment, we will see that the website we have entered is stored within the `href` attribute.

![href attribute in inspector](assets/2.png)

We can try to create another comment by entering a javascript instruction in the website field.

![javascript payload](assets/3.png)

If we check the comments again and hover over the one we just uploaded, we will see that it no longer contains a URL, but a script.

![script in href](assets/4.png)

Now if someone clicks on our name the `alert` will pop up.

![alert pops up](assets/5.png)

With this we will have completed the lab.

---
<div align="center">
  <a href="../Lab-7/README.md">⬅️ Previous Lab</a>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="../Lab-9/README.md">Next Lab ➡️</a>
</div>
