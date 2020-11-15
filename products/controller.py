from .models import Product

class ProductController:

    def get_products():
        return Product.objects.all()

    def addProduct():
        return Product(prodtitle = 'product 2').save()
        # print(self.prod)

        # self.prod.prodtitle = params['prodtitle']
        # return self.prod
        # self.save()



