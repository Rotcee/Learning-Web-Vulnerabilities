# Lab 8: SQL injection UNION attack, finding a column containing text

## Statement

*This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a `UNION` attack to retrieve data from other tables. To construct such an attack, you first need to determine the number of columns returned by the query. You can do this using a technique you learned in a [previous lab](../Lab-7/README.md). The next step is to identify a column that is compatible with string data.*

*The lab will provide a random value that you need to make appear within the query results. To solve the lab, perform a SQL injection UNION attack that returns an additional row containing the value provided. This technique helps you determine which columns are compatible with string data.*

## Walkthrough

The first thing we see when entering the lab is the string that we must include in our `UNION` attack.

![Provided string to inject](./assets/1.png)

We do the usual: inject a single quote (`'`) to check for the vulnerability, use `ORDER BY` to discover the number of columns returned by the query, and then use a `UNION` attack to inject data. We place the provided string in one of the `NULL` positions in our `UNION SELECT` statement to solve the lab.

![Solving the lab](./assets/2.png)

---
<div align="center">
  <a href="../Lab-7/README.md">⬅️ Previous Lab</a>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="../Lab-9/README.md">Next Lab ➡️</a>
</div>
