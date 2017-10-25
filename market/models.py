from django.db import models
from django.conf import setting
## This contains the main 
class Stock(models.Model):
    symbol = models.CharField(max_length = 4, primary_key = True)
    current_price = models.IntegerField()
    close_price = models.IntegerField()
    open_price = models.IntegerField()
    high_price = models.IntegerField()
    low_price = models.IntegerField()
    volume = models.IntegerField()
    owner = models.ManyToManyField(Customer, through = 'Portfolio')
    
    def __str__(self):
        return self.symbol
        
class Portfolio(models.Model):
    owner = models.ForeignKey(Customers, on_delete = models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete = models.CASCADE)
    volume = models.IntegerField()
    boughtat = models.IntegerField()

class Customers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField()
    
    def buy(self,symbol,volume):
        stock=Stock.objects.get(symbol=symbol)
        if self.balance>(stock.current_price*volume) and stock.volume>volume:
            self.balance-=(stock.current_price*volume)
            stock.current_price+=(0.01*stock.current_price*volume)
            stock.volume-=volume
            portfolio = Portfolio(volume=volume,boughtat=stock.current_price)
            portfolio.save()
            portfolio.owner=self
            portfolio.stock=stock
            return True
       else:
            return False
    def sell(self,symbol,volume):
# Create your models here.
