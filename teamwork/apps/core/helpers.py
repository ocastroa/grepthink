# Required headers for sendgrid: (sendgrid, os)
import sendgrid
import os
from sendgrid.helpers.mail import *

"""
    Params: recipients -- QuerySet of students
            from_email -- The address that the email will come from (can be anything we want)
            subject    -- subject of the email
            content    -- content of the email

    IF Authorization error occurs its because:
        1. you dont have sendgrid.env file in root. Get from Discord (8/11)
        2. need to run 'source ./sendgrid.env'
"""
def send_email(recipients, gt_email, subject, content):

    student_email_list = []
    # build list of emails of recipients
    for student in recipients:
            if not student.profile.isProf:
                student_email_list.append(Email(student.email))

    # Handle email sending
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))

    # TODO: not sure what to put here in the to_email as of now.  Don't really need this initial email to be added,
    # but I'm not sure how the Mail() constructor below works without it.
    to_email = Email("initial_email@grepthink.com", "GrepThink")

    from_email = Email(gt_email)

    # TODO: Content should be formatted in a professional way. I believe markup is supported.
    final_content = Content("text/plain", content)
    mail = Mail(from_email, subject, to_email, final_content)

    # add multiple emails to the outgoing Mail object
    # creating Personalization instances makes it so everyone can't see everyone elses emails in the 'to:' of the email
    for email in student_email_list:
        p = Personalization()
        p.add_to(email)
        mail.add_personalization(p)

    # The following line was giving SSL Certificate errors.
    # Solution at: https://stackoverflow.com/questions/27835619/urllib-and-ssl-certificate-verify-failed-error/42334357#42334357
    response = sg.client.mail.send.post(request_body=mail.get())

    # print(response.status_code)
    # print(response.body)
    # print(response.headers)
