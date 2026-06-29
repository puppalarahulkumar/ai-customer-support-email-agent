

class HumanAgent:
    def __init__(self, name):
        self.customer_email = name

    def send_mail(self, customer_email,email_content):
        print(f"{self.customer_email}: {email_content}")
