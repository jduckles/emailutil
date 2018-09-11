import util
import sys


def main():
    for item in context:
        email_body = template.render(item)
        try:
            print("Sent to " + item['email'])
            print(email_body)
            util.send_email(item['email'],subject, email_body)
        except:
            print("missing email address")


if __name__ == '__main__':
    context = util.csv2dict(sys.argv[1])
    template = util.readtemplate(sys.argv[2])
    subject= sys.argv[3]
    main()
