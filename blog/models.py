from django.db import models

# Create your models here.
class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=True, blank=True, default="")
    head0 = models.CharField(max_length=500, null=True, blank=True, default="")
    chead0 = models.CharField(max_length=5000, null=True, blank=True, default="")
    head1 = models.CharField(max_length=500, null=True, blank=True, default="")
    chead1 = models.CharField(max_length=5000, null=True, blank=True, default="")
    head2 = models.CharField(max_length=500, null=True, blank=True, default="")
    chead2 = models.CharField(max_length=5000, null=True, blank=True, default="")
    pub_date = models.DateField(null=True, blank=True, default="")
    thumbnail = models.ImageField(upload_to='blog/images',default="", blank=True, null=True)

    def __str__(self):
        return self.title