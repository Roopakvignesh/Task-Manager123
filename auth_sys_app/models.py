from django.db import models

# Create your models here.
class product(models.Model):
    pname=models.CharField(max_length=100)
    price=models.IntegerField()
    pdesc=models.TextField()
    image=models.ImageField(upload_to='product')
    def __str__(self):
        return f'pname={self.pname},price={self.price},pdesc={self.pdesc}'