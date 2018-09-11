

Quick and dirty mass emailer using Jinja2 Templates and CSV context. 

Using a csv file with a header row and an HTML Jinja2 template, send an email
for each row of the csv, entering data from the csv in the Jinja2 template
as appropriate. 

Simple template example:
```
Dear {{ firstname }},

Hello, how are you?

Regards,
Jonah
```

CSV must have column named email for use as the `To:` email address.

```
firstname,lastname,email
John,Doe,me@here.org
```

```
python3 send_email.py examples\test.csv examples\test.html "Subject Line"
```
