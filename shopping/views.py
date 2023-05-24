from django.shortcuts import render, get_object_or_404
from ECOM.models import  Category, Product
from .basket import  Basket
from django.http import JsonResponse

# Create your views here.
def all_shopping_items(request):
    categories = Category.objects.all()
    basket = Basket(request)
   #  product=Product.objects.all()
    content={
       "categories":categories,
       "basket":basket,
      #"products":product
    }

    return render(request,'ecom/basket/summary.html', content)

def add_items(request):
   basket= Basket(request)
   if request.POST.get('action') == 'post':
      product_id= int(request.POST.get('productid'))   
      product_qty = int(request.POST.get('productQTY'))  
      product=get_object_or_404(Product , id=product_id)
      basket.add(product=product,product_qty=product_qty)
      basket_qty=basket.__len__()
      response= JsonResponse({'qty' : basket_qty})
      return response





def delete_items(request):
   basket= Basket(request)
   if request.POST.get('action') == 'post':
      product_id= int(request.POST.get('productid'))
      basket.delete(product=product_id)
      response= JsonResponse({'Success' : True })
      return response



def update_items(request):
   basket= Basket(request)
   if request.POST.get('action') == 'post':
      product_id= int(request.POST.get('productid'))
      product_qty =int(request.POST.get('productqty'))
      basket.update(product_id=product_id, product_qty=product_qty)
      response= JsonResponse({'Success' : True })
      return response


 
