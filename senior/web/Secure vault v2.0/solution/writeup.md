# Secure vault v2.0 writeup
There is a login form on site. After some researches we understand it's SQL and it's injectable (passowrd field). Also, we may find _admin_ user and try simple SQL injection:

```SQL
1' OR '1' = '1
```

But it doesn't work, we get message about hack attempt. After analysis, we get list of banned words: '`"`',  '`OR`' We can bypass it:

```SQL
1' or '1' = '1
```

Enter this injection in password field, username=_admin_, and see message that all secret data were moved to _sultanowskii_.

Login to _sultanowskii_ using SQL-injection, but after we understand that there are more filters for this account. Analyse again, and get list of banned words: '`"`', '` `', '`OR`', '`or`', '`1`'. They all are exchangable, so, in the end we have this one:

```SQL
2'/**/oR/**/'2'/**/=/**/'2
```

Flag is in _sultanowskii_'s storage

Flag: **flag{4b50lu73ly\_53cur3\_v4ul7\_y34h}**
