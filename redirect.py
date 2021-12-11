from block import Block
from clean import Clean

def Execute(my_college_emails, my_email, app_password, other_bad_emails, person):
    Clean(my_college_emails, my_email, app_password, other_bad_emails, person)
    Block(my_college_emails, my_email, app_password, other_bad_emails, person)
