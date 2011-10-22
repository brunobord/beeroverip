from django.contrib.syndication.feeds import Feed
from django.utils.translation import ugettext_lazy as _
from models import Beer


class BeerFlow(Feed):
    """Basic beer flow."""
    title = _("Beer flow, latest")
    link = "/all/"
    description = _("Latest Beers available for IP Transport")

    def items(self):
        return Beer.objects.order_by('-id')[:10]
