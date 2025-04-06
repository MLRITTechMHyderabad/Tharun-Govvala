import re

def valid_emails(text):
    
    email_pattern = r"[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    valid_emails1 = re.findall(email_pattern, text)
    
    return valid_emails1

text = "Contact us at support@example.com, john.doe123@company.org, or invalid-email@com. Also, try jane_doe@domain.co.uk."

valid_email = valid_emails(text)
print(valid_email)
