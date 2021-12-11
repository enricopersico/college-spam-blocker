import imaplib, email
import time
from email.header import decode_header

def Block(my_college_emails, my_email, app_password, other_bad_emails, person):
    print(f"NOW BLOCKING SPAM FOR: {person}")
    start = time.time()
    my_college_domains = []
    for address in my_college_emails:
        my_college_domains.append(address.split('@')[1])
    while True:
        try:
            # create an IMAP4 class with SSL 
            imap = imaplib.IMAP4_SSL("imap.gmail.com")
            # authenticate
            imap.login(my_email, app_password)
            status, messages = imap.select("INBOX")
            last_message_id = int(messages[0])
            # fetch the email message by ID
            res, msg = imap.fetch(str(last_message_id), "(RFC822)")
        except imaplib.error as e:
            print(e)
            print(f"RAN FOR {time.time() - start} seconds")
        for response in msg:
            if isinstance(response, tuple):
                try:
                    # parse a bytes email into a message object
                    msg = email.message_from_bytes(response[1])
                    # decode email sender
                    From, encoding = decode_header(msg.get("From"))[0]
                    if isinstance(From, bytes):
                        From = From.decode(encoding)
                    name = From.split('<')[0]
                    address = From.split('<')[1].replace('>', '')
                    # print(f"=================Latest Email is From: {address}===================", end='\r')
                    domain = address.split('@')[1]
                    if '.edu' in domain or ('university' in From.lower() or 'admissions' in From.lower()):
                        if domain not in my_college_domains:
                            print(f"Blocked College Spam from {name} for {person}")
                            imap.store(str(last_message_id), "+FLAGS", "\\Deleted")
                    elif address in other_bad_emails:
                        print(f"Blocked Other Spam From: {name} for {person}")
                        imap.store(str(last_message_id), "+FLAGS", "\\Deleted")
                except: pass
                imap.expunge()
                imap.close()
                imap.logout()
