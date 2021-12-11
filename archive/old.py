import imaplib
import pandas
from email.header import decode_header

address = "//span[@class='go']"
emails = "//div[@class='Cp']/div/table/tbody/tr"
more = "//*[@id=':19h']"
yes = "//button[@name='yes']"

"""

    "admission@gatech.edu",
    #"undergrad-admissions@ncsu.edu",
    #"ug-admission@northwestern.edu",
    #"admissions@psu.edu",
    "admissions@purdue.edu",
    #"askabuckeye@osu.edu",
    "admissions@illinois.edu",
    #"unchelp@admissions.unc.edu",
    "onwisconsin@admissions.wisc.edu",
    #"admissions@vt.edu",
    "be-a-hawkeye@uiowa.edu",
    "applicants@admissions.upenn.edu",
    "help@admissions.ufl.edu",
    "app.enquiries@monash.edu"
    #"admissions@austin.utexas.edu"
"""

# account credentials
username = "enricofpersico@gmail.com"
password = "qrlqmnjujvecdgmp"

# create an IMAP4 class with SSL 
imap = imaplib.IMAP4_SSL("imap.gmail.com")
# authenticate
imap.login(username, password)
imap.select("INBOX")

my_college_emails = [
    "admission@gatech.edu",
    "undergrad-admissions@ncsu.edu",
    "ug-admission@northwestern.edu",
    "admissions@psu.edu",
    "admissions@purdue.edu",
    "askabuckeye@osu.edu",
    "admissions@illinois.edu",
    "unchelp@admissions.unc.edu",
    "onwisconsin@admissions.wisc.edu",
    "admissions@vt.edu",
    "admissions@austin.utexas.edu"
]

spam_count = 0
df = pandas.read_csv("college_emails_list.csv")
for index, college in df.iterrows():
    domain = college['Email'].split('@')[1]
    name = college['College']
    
    ok_domains = []
    for email in my_college_emails:
        ok_domains.append(email.split('@')[1])

    if domain not in ok_domains:
        status, messages = imap.search(None, f'FROM "{domain}"')
        ids = messages[0].split(b' ')
        if ids[0] != b'':
            spam_count += len(ids)
            print(f"Deleting {len(ids)} spam emails from {name}")
            for mail in ids:
                imap.store(mail, "+FLAGS", "\\Deleted")
    else: print(f"OK DOMAIN ({domain}) - OVERLOOKED")

imap.expunge()
imap.close()
imap.logout()
print(f"SPAM EMAILS DELETED: {spam_count}")
