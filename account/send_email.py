from django.core.mail import send_mail


def send_confirmation_email(user, code):
    # code = user.activation_code
    code = code
    full_link = f'http://localhost:8000/api/v1/account/activate/{code}/'
    # to_email = user.email
    to_email = user
    send_mail(
            'Здравствуйте ваш аккаунт!',
            f'Чтобы активировать ваш аккаунт нужно перейти по ссылке: {full_link}',
            'nurmuhamed3222@gmail.com',
            [to_email,],
            fail_silently=False)


def send_reset_password(user):
    code = user.activation_code
    to_email = user.email
    send_mail(
            'Subject',
            f'Your code for reset password: {code}',
            'from@example.com',
            [to_email,],
            fail_silently=False)


def send_notification(user,id):
    to_email = user.email
    send_mail(
            'Уведомление о создании заказа!',
            f'Вы сделали заказ, номер вашего заказа №{id}, ожидайте звонка!',
            'from@example.com',
            [to_email,],
            fail_silently=False)