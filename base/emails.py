from django.conf import settings
from django.core.mail import send_mail

def send_account_activation_email(email, email_token):
    subject = 'Your account needs to be verified'
    email_from = settings.EMAIL_HOST_USER
    message = f'Hello, click on the link to activate your account. http://127.0.0.1:8000/accounts/activate/{email_token}'
    # message = 'Hello, You have been registered.'
    send_mail(subject, message, email_from, [email])


# from django.core.mail import send_mail
# from django.conf import settings

# def send_account_activation_email(email, email_token):
#     subject = 'Your account needs to be verified'
#     email_from = settings.EMAIL_HOST_USER
#     message = f'Hello, click on the link to activate your account: http://127.0.0.1:8000/accounts/activate/{email_token}'

#     try:
#         print("Attempting to send email...")
#         print(f"From: {email_from}, To: {email}, Message: {message}")
#         send_mail(subject, message, email_from, [email])
#         print("Email sent successfully")
#     except Exception as e:
#         print(f"Failed to send email: {e}")
