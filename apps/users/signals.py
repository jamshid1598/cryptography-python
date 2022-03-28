from django.utils import timezone


def save_user_last_logged_in_datetime(sender, request, user, **kwargs):
    """
        'save_user_last_logged_in_datetime' function is called 
        when 'user_logged_in' signal is send and saves the 
        datetime to the user's last_login field 
    Args:
        sender (model): User model
        request (request object): 
        user (instance): User model instance
    """
    user.last_login = timezone.localtime()
    user.save(update_fields=['last_login',])
