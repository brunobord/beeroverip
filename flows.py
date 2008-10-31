from django.contrib.syndication.feeds import Feed
from models import Beer

class BeerFlow(Feed):
    title = "Beer flow, latest"
    link = "/all/"
    description = "Latest Beers available for IP Transport"

    def items(self):
        return Beer.objects.order_by('-upload_date')[:10]

