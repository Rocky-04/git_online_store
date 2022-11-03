from .forms import SubscriberEmailForm


def getting_subscribe_email_form(request):
    form = SubscriberEmailForm
    return locals()
