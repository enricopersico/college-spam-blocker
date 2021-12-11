import imaplib, email
from email.header import decode_header

def Clean(my_college_emails, my_email, app_password, other_bad_emails, person):
    print(f"CLEANING INBOX OF: {person}")
    my_college_domains = []
    for address in my_college_emails:
        my_college_domains.append(address.split('@')[1])
    # create an IMAP4 class with SSL 
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    # authenticate
    imap.login(my_email, app_password)
    status, messages = imap.select("INBOX")
    messages = int(messages[0])

    spam_count = 0
    for i in range(messages, 0, -1):
        # fetch the email message by ID
        res, msg = imap.fetch(str(i), "(RFC822)")
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
                    domain = address.split('@')[1]
                    if ('.edu' in domain or 'university' in From.lower() or 'admissions' in From.lower()) and domain not in my_college_domains:
                        print(f"Deleted College Spam from {name} for {person}")
                        spam_count += 1
                        imap.store(str(i), "+FLAGS", "\\Deleted")
                    elif address in other_bad_emails:
                        print(f"Deleted Other Spam from {name} for {person}")
                        imap.store(str(i), "+FLAGS", "\\Deleted")
                except: pass
    
    # close the connection and logout
    imap.expunge()
    imap.close()
    imap.logout()
    print(f"SPAM EMAILS DELETED DURING CLEAN FOR {person}: {spam_count}")
