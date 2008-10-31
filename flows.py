from django.contrib.syndication.feeds import Feed
from django.utils.translation import ugettext as _
from models import Beer

class BeerFlow(Feed):
    title = _("Beer flow, latest")
    link = "/all/"
    description = _("Latest Beers available for IP Transport")

    def items(self):
        return Beer.objects.order_by('-upload_date')[:10]

