from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length = 50)
    category = models.CharField(max_length = 50, default="")
    subcategory = models.CharField(max_length = 50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length = 500)
    pub_date = models.DateField()
    image = models.ImageField(upload_to = "shop/images", default="")

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 50)
    desc = models.CharField(max_length = 500)

    def __str__(self):
        return self.name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000, null=True, blank=True, default="")
    name = models.CharField(max_length=90, null=True, blank=True, default="")
    email = models.CharField(max_length=111, null=True, blank=True, default="")
    address = models.CharField(max_length=111, null=True, blank=True, default="")
    city = models.CharField(max_length=111, null=True, blank=True, default="")
    state = models.CharField(max_length=111, null=True, blank=True, default="")
    zip_code = models.CharField(max_length=111, null=True, blank=True, default="")
    mobile = models.BigIntegerField(default=0, null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.name

        