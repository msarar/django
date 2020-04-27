from django.shortcuts import render
from .models import Product
from .forms import ProductForm
# Create your views here.
def product_create_view(request, *args , **kwargs):
    form = ProductForm (request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm ()
    context = {
        "form" : form
    }
    return render (request, "products/product_create.html", context)



def product_detail_view(request, *args , **kwargs):
    # return HttpResponse("<h1>About The Page:</h1>") #string of html not actual html
    obj = Product.objects.get(id = 1)
    # context = {
    #     "title" : obj.title,
    #     "description" : obj.description,
    #     "price" : obj.price,
    #     "summary" : obj.summary,
    # }
    context = {
        "object" : obj
    }
    return render (request, "products/product_detail.html", context)
