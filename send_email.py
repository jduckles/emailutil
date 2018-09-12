#!/usr/bin/env python3
import util
import sys
import argparse



def main():
    for item in context:
        email_body = template.render(item)
        try:
            print("Sent to " + item['email'])
            if not args.quiet:
                print(email_body)
            if not args.dryrun:
                util.send_email(item['email'],subject, email_body)
        except:
            print("missing email address")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("context", help="Path to a CSV file with the data context for the template. Each row in the CSV will result in one sent email. The template is filled with associated data from a given row. Must have a column named 'email' for To: address.")
    parser.add_argument("template",help="Path to a Jinja2 template file that can be filled by the context")
    parser.add_argument("subject", help="Quoted string with email's subject line, subject string is NOT filled as a template")
    parser.add_argument("-q","--quiet", help="Supress printing of all filled templates.", action="store_true")
    parser.add_argument("-d", "--dryrun", help="Don't actually send emails, just print them to screen.", action="store_true")
    args = parser.parse_args()
    context = util.csv2dict(args.context)
    template = util.readtemplate(args.template)
    subject = args.subject
    main()
