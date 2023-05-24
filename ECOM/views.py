from django.shortcuts import render,get_object_or_404
from .models import Category,Product

# Create your views here.





def all_products(request):
    products=Product.objects.filter(is_active=True)
    categories = Category.objects.all()
        
    
    content={
       "products":products,
       'categories': categories
    }
    
    return render(request,'ecom/home.html' , content)


def product_detail(request ,slug):
   categories = Category.objects.all()
   products = Product.objects.get(slug=slug, in_stock=True)
   content={
       "products": products,
       'categories': categories
    }
   return render(request,'ecom/product/detail.html', content)


def category_detail(request ,cat_slug):
   categories = Category.objects.all()
   category = get_object_or_404(Category,slug=cat_slug)
   product = Product.objects.filter(category=category)
   content={
       "products": product,
       "category": category,
       'categories': categories
       
    }

   return render(request,'ecom/product/category.html', content)