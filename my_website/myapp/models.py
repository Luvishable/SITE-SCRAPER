from django.db import models

# Create your models here.

class Link(models.Model):

    def __str__(self):
        return self.name

    # sometimes certain links might not have a proper address and we need to allow those addresses to be null
    address = models.CharField(max_length=1000, null=True, blank=True)
    name = models.CharField(max_length=1000, null=True, blank=True)

    # After creating the Link model, you have to also make sure that your view - in this case scrape- saves address and
    # name of the links to the database

