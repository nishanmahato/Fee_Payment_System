from .background_tasks import send_otp

def is_email_valid(email):
    if email is not None and email != "" and "@" not in email and "." not in email:
        return False
    return True


def forgot_password_email(email):
    from django.core.mail import send_mail
    from django.conf import settings
    from .models import OTP

    try:
        new_otp = OTP.generate_otp(email)
    except Exception as e:
        raise Exception(str(e))
    
    send_otp(email, new_otp)

    



def send_password_change_email(user):
    from django.core.mail import send_mail
    from django.conf import settings

    
    """Send notification when the user changes their password."""
    send_mail(
        subject="Your password has been changed",
        message=(
            f"Hello {user.first_name},\n\n"
            "Your account password was successfully changed.\n"
            "If this wasn’t you, please contact our support team immediately."
        ),
        from_email=settings.EMAIL_HOST_USER,  # Uses your EMAIL_HOST_USER from settings.py
        recipient_list=[user.email],
        fail_silently=False,
    )