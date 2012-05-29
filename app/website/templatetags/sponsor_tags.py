from django import template
register = template.Library()

from app.website.models import Sponsor
from datetime import date

@register.inclusion_tag('website/sponsorsList.html')
def list_sponsors():
    sponsors = Sponsor.objects.order_by('amount_paid').reverse().filter(expiry_date__gte=date.today)
    return {'sponsors': sponsors}