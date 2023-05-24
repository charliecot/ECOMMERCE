from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
#from django.utils.text import slugify
# Create your models here.


class Category(models.Model):

    name= models.CharField(max_length=255 , db_index=True)

    slug= models.SlugField(max_length=255, unique=True, )
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.name)
    #     super(Category, self).save(*args, **kwargs)      

    class Meta:

        verbose_name_plural = "Categories"

    def  get_absolute_url(self):

        return reverse('ECOM:category', args=[self.slug])

    def __str__(self):

        return self.name    



class Product(models.Model):

    category= models.ForeignKey(Category, related_name="product",on_delete=models.CASCADE)        

    created_by= models.ForeignKey(User, related_name="product_creator",on_delete=models.CASCADE)        

    title=models.CharField(max_length=255)

    author=models.CharField(max_length=255, default='Admin')

    description = models.TextField(blank=True)

    image = models.ImageField(upload_to='IMAGE/')

    slug= models.SlugField(max_length=255)

    price= models.DecimalField(decimal_places=2, max_digits=4)

    in_stock= models.BooleanField(default=True)

    is_active= models.BooleanField(default=True)

    created=models.DateTimeField(auto_now_add=True)

    updated= models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural='Products'
        ordering =('-created',)


    def  get_absolute_url(self):

        return reverse('ECOM:product', args=[self.slug])


    def __str__(self):
        return self.title     

