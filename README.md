# Radhe-Radhe
# ai-customer-support-email-agent

The agent should:

- Read incoming customer emails
- Classify them by urgency and topic
- Search relevant documentation to answer questions
- Draft appropriate responses
- Escalate complex issues to human agents
- Schedule follow-ups when needed

Example scenarios to handle:

1. Simple product question: "How do I reset my password?"
2. Bug report: "The export feature crashes when I select PDF format"
3. Urgent billing issue: "I was charged twice for my subscription!"
4. Feature request: "Can you add dark mode to the mobile app?"
5. Complex technical issue: "Our API integration fails intermittently with 504 errors"



To run the project,

1. install pip in your desktop,

2. create virtual environment and .env file, then run the virtual environment.

3. these are the required fields for .env:

`OPENAI_API_KEY`

4. pip install -r requirements.txt

5. run `python manage.py migrate` <- for first time only

6. run `python manage.py runserver` <- every time to start the project

7. Open postman and test using these apis: 

POST Method:	
API: POST /api/process-email
 {
        "email_content": "How do I reset my password?",
        "sender_email": "contact.rahulpuppala@gmail.com",
        "email_id": "email_12345"
    }

Response:

{
    "email_content": "How do i reset the password?",
    "sender_email": "rahul@gmail.com",
    "email_id": "email_32123",
    "classification": {
        "intent": "question",
        "urgency": "low",
        "topic": "Password reset",
        "summary": "Inquiry about resetting password"
    },
    "draft_response": "To reset your password, please follow these general steps:\n\n1. Go to the login page of the website or app.\n2. Click on the \"Forgot Password\" or \"Reset Password\" link.\n3. Enter your registered email address or username.\n4. Check your email inbox for a password reset email.\n5. Follow the instructions in the email, which typically involves clicking a link to create a new password.\n6. Enter your new password and confirm it.\n\nIf you encounter any issues or do not receive the email, consider contacting the support team for further assistance."
}



If you want to add new documents to the Vector store:

POST /api/rebuild-rag/ (You need to change the path inside the code for now)


Happy Coding!!