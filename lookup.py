from amazon.api import AmazonAPI

amazon = AmazonAPI('AKIAJUEBQSRYM67EZTAA', 'PzSanYuYOnu1OgZXsYe0WRCYbPSZjBuPEcIVqvHX', 'datawareho0a3-20')

product = amazon.lookup(ItemId='6305508569')
print((product))