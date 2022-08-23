from django.db import models

class Currency(models.Model):
    name = models.CharField(max_length=40)
    symbol = models.CharField(max_length=10)
    base = models.CharField(max_length=10, default='USD')
    bs_sym_rate = models.DecimalField(blank=True, null = True, max_digits=10, decimal_places=5)
    # link = models.URLField(default='/api/<int:pk>')
    likes_total = models.IntegerField(default=0)
    last_update_time = models.DateTimeField(auto_now=True)
    # favouritedBy_user = models.ManyToManyField(User, related_name='user_favourite', blank=True)
    def __str__(self):
        return self.symbol