# Lab 9: SQL injection UNION attack, retrieving data from other tables

## Statement

*This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a `UNION` attack to retrieve data from other tables. To construct such an attack, you need to combine some of the techniques you learned in previous labs.*

*The database contains a different table called `users`, with columns called `username` and `password`.*

*To solve the lab, perform a SQL injection UNION attack that retrieves all usernames and passwords, and use the information to log in as the administrator user.*

## Walkthrough

We do the usual: inject a single quote (`'`) to check for the vulnerability, use `ORDER BY` to discover the number of columns returned by the query, and then use a `UNION` attack to inject data. In this case, we are told to access the `username` and `password` columns from the `users` table to obtain the administrator's credentials.

![Retrieving credentials with a UNION attack](./assets/1.png)

We can see the login credentials for several users, including the one we are looking for. Now we can log in as the `administrator` to complete the lab.

![Logging in as administrator](./assets/2.png)

---
<div align="center">
  <a href="../Lab-8/README.md">⬅️ Previous Lab</a>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="../Lab-10/README.md">Next Lab ➡️</a>
</div>
