from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Frut(models.Model):
    product_image=models.ImageField(upload_to="product_image/",default='product_image/nodata.png')
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    manufacture_date=models.DateField()
    description=models.TextField()
    is_fresh=models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

    # class Meta:
    #     vor