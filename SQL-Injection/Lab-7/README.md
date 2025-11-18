# Lab 7: SQL injection UNION attack, determining the number of columns returned by the query

## Statement

*This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a `UNION` attack to retrieve data from other tables. The first step of such an attack is to determine the number of columns that are being returned by the query. You will then use this technique in subsequent labs to construct the full attack.*

*To solve the lab, determine the number of columns returned by the query by performing a SQL injection `UNION` attack that returns an additional row containing null values.*

## Walkthrough

This lab is quite simple if we have done the previous ones. We do the usual: inject a single quote (`'`) to see if it is vulnerable to SQL injection, use `ORDER BY` to discover the number of columns returned by the query, and use a `UNION` attack to inject the data we want into the query response. We set all columns in our `UNION` attack to `NULL` to solve the lab.

![Solving the lab with a UNION attack](./assets/1.png)

---
<div align="center">
  <a href="../Lab-6/README.md">⬅️ Previous Lab</a>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="../Lab-8/README.md">Next Lab ➡️</a>
</div>
