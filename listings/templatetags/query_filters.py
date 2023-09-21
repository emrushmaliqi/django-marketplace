from django import template
from django.db.models import Q

register = template.Library()


@register.filter(name='is_sold')
def is_sold(listings, is_sold):
    return listings.filter(is_sold=is_sold)


@register.filter(name='others_sold')
def others_sold(listings, user):
    if (user is None):
        return listings.filter(is_sold=False)
    print(user)
    return listings.filter(~Q(user_id=user), is_sold=False)
