# Lab 10: SQL injection UNION attack, retrieving multiple values in a single column

## Statement

*This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response so you can use a `UNION` attack to retrieve data from other tables.*

*The database contains a different table called `users`, with columns called `username` and `password`.*

*To solve the lab, perform a SQL injection UNION attack that retrieves all usernames and passwords, and use the information to log in as the administrator user.*

## Walkthrough

We do the usual: inject a single quote (`'`) to check for the vulnerability, use `ORDER BY` to discover the number of columns returned by the query, and then use a `UNION` attack to inject data. In this case, we are told to access the `username` and `password` columns from the `users` table to obtain the administrator's credentials, but we are ordered to retrieve them in a single column. We can use the concatenation operator (`||`) to accomplish this. In one of the fields, we will put the following:

`username||'-->'||password`

The character between the single quotes will be used to join the data from the columns.

![Concatenating columns in a UNION attack](./assets/1.png)

We see that this returns the credentials in the same column. Among the information, we find what is necessary to log in as `administrator` and complete the lab.

![Logging in as administrator](./assets/2.png)

---
<div align="center">
  <a href="../Lab-9/README.md">⬅️ Previous Lab</a>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="../Lab-11/README.md">Next Lab ➡️</a>
</div>
