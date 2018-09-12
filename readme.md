

Quick and dirty mass emailer using Jinja2 Templates and CSV context. 

Help text:

```
usage: send_email.py [-h] [-q] [-d] context template subject

positional arguments:
  context       Path to a CSV file with the data context for the template.
                Each row in the CSV will result in one sent email. The
                template is filled with associated data from a given row. Must
                have a column named 'email' for To: address.
  template      Path to a Jinja2 template file that can be filled by the
                context
  subject       Quoted string with email's subject line, subject string is NOT
                filled as a template

optional arguments:
  -h, --help    show this help message and exit
  -q, --quiet   Supress printing of all filled templates.
  -d, --dryrun  Don't actually send emails, just print them to screen.
```



## Step 0 - requirements

```
pip install -r requirements.txt
```

## Step 1 - configure settings

```
mv local_settings.py.example local_settings.py
```
Edit local settings as appropriate for your configuration

## Step2 - setup Template

Using a csv file with a header row and an HTML Jinja2 template, send an email
for each row of the csv, entering data from the csv in the Jinja2 template
as appropriate. 

Simple template example:
```
Dear {{ firstname }},

Hello, how are you? How are things at {{ organization }}?

Regards,
Jonah
```

## Step 3 - Setup CSV file

CSV must have column named email for use as the `To:` email address.

```
firstname,lastname,email,
John,Doe,me@here.org,Awesome Inc.
```

# Step 3.5 - Test on yourself
Using a CSV which has only your email as the recipient and some test data, send a test email to yourself to confirm formatting and template merge is working correctly. 


## Step 4 - Send many emails!  

```
python3 send_email.py examples\test.csv examples\test.html "Subject Line"
```
