

Quick and dirty mass emailer using Jinja2 Templates and CSV context. 

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
firstname,lastname,email
John,Doe,me@here.org
```

# Step 3.5 - Test on yourself
Using a CSV which has jus you as the sender and test data, send a test email to yourself to confirm formatting and template merge is working correctly. 


## Step 4 - Send many emails!  

```
python3 send_email.py examples\test.csv examples\test.html "Subject Line"
```
