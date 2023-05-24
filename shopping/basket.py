from ECOM.models import  Product
from decimal import Decimal




class Basket():




    def __init__(self, request):

        self.session = request.session
        basket= self.session.get('key')
        if "key" not in request.session:
            basket= self.session['key'] = {}
        self.basket =basket    

    def add(self, product,product_qty):

        product_id = product.id

        if product_id not in self.basket :
            self.basket[product_id]={'price': float(product.price),'qty': int(product_qty)}
        self.save() 
    
    def __iter__(self ):
        product_ids =self.basket.keys()
        Products=Product.objects.filter(id__in=product_ids)
        basket=self.basket.copy()

        for products in Products:
            self.basket[ str(products.id)]['products']=products

        for item in basket.values():
            item['price'] =item['price']
            item['total_price']= item['price']*item['qty']
            yield item



    def __len__(self):
        

        return sum(item['qty'] for item in self.basket.values())


    def  get_total_price(self):

        return sum(item['price'] *  item['qty'] for item in self.basket.values())


    def delete(self, product):
        product_id=str(product)
      
        if product_id in self.basket:
            del self.basket[product_id]
        self.save()


    def update(self , product , qty):
        product_id=product
        qty=qty
        if product_id in self.basket:
            self.basket[product_id]['qty']=qty
        self.save()    

    def save(self):
        self.session.modified =True


    