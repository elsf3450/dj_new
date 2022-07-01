from django.db import models

# Create your models here.
class Product(models.Model):
    #owner = models.ForeignKey(User)
    title = models.CharField(max_length=120)
    content=models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=15,decimal_places=2,default=99.99)

    #@property
    def sale_price(self):
        return "%2f" %(float(self.price)*0.8)
    def get_discount(self):
        return "2323"

class User(models.Model):
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=32)
    user_type=models.IntegerField(choices=((1,'超级用户'),(2,'普通用户'),(3,'二笔用户')))
    @property
    def is_authenticated(self):
        return True
class UserToken(models.Model):
    user=models.OneToOneField(to='User',on_delete=models.CASCADE)
    token=models.CharField(max_length=64)