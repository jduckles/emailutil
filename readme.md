

Quick and dirty mass emailer using Jinja2 Templates and CSV context. 


**Note:** With today's anti-spam measures in place at many mail servers, it is probably best that you don't use your Gmail or other business mail accounts with this script for more than 10s of emails. Uses something like MailGun to do your bulk sending. 

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

```
smtp_user="" # Username for SMTP server
smtp_passwd="" # Password for SMTP server
smtp_host="host:port" # Assumes StartTLS support at server
default_sender="me@there.org <My Name>" # Who should the emails be from?
```

## Step2 - Setup a Template

Using a csv file with a header row and an HTML Jinja2 template ([docs](http://jinja.pocoo.org/docs/2.10/templates/)), 
send an email
for each row of the csv, filling the template with data from the csv. 

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

# Step 3.5 - Dry-run then test on yourself
Using a CSV which has only your email as the recipient and some test data, send a test email to yourself to confirm formatting and template merge is working correctly. 

```
# Dry run (no emails sent, test template/context merge)
./send_email.py -d examples\test.csv examples\test.html "Subject Line"
```


## Step 4 - Send many emails!  

```
./send_email.py examples\test.csv examples\test.html "Subject Line"
# or
./send_email.py -q examples\test.csv examples\test.html "Subject Line"
# to supress all email's being printed to stdout as well as being sent via SMTP
```
