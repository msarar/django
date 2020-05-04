from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm #, RawProductForm
# Create your views here.

def product_create_view(request, *args , **kwargs):
    initial_data = {
        'title' : "X"
    }
    form = ProductForm (request.POST or None, initial = initial_data)
    if form.is_valid():
        form.save()
        form = ProductForm ()
    context = {
        "form" : form
    }
    return render (request, "products/product_create.html", context)

def product_update_view(request, id=id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)

def dynamic_lookup_view(request, my_id):
    # obj = Product.objects.get(id =my_id)
    obj = get_object_or_404 (Product, id = my_id)
    context = {
        "object" : obj
    }
    return render (request, "products/product_detail.html", context)

def product_delete_view(request, my_id):
    # obj = Product.objects.get(id =my_id)
    obj = get_object_or_404 (Product, id = my_id)
    if (request.method == "POST"):
        obj.delete()
        return redirect ('../../../')
    context = {
        "object" : obj
    }
    return render (request, "products/product_delete.html", context)

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list" : queryset
    }
    return render (request, "products/product_list.html", context)

# def product_create_view(request, *args , **kwargs):
#     #function broken down : RAWHTML FORM
#
#     print (request.POST)
#     print (request.GET)
#     if request.method == "POST":
#         my_new_title = request.POST.get('title')
#         print (my_new_title)
#         # Product.objects.create(title = my_new_title)
#     context = {}
#     return render (request, "products/product_create.html", context)

# def product_create_view(request, *args , **kwargs):
#     #function broken down : Pure Django Form FORM
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             print (my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print (my_form.errors)
#     context = {
#         "form":my_form
#     }
#     return render (request, "products/product_create.html", context)

# def product_detail_view(request, *args , **kwargs):
#     # return HttpResponse("<h1>About The Page:</h1>") #string of html not actual html
#     obj = Product.objects.get(id = 1)
#     # context = {
#     #     "title" : obj.title,
#     #     "description" : obj.description,
#     #     "price" : obj.price,
#     #     "summary" : obj.summary,
#     # }
#     context = {
#         "object" : obj
#     }
#     return render (request, "products/product_detail.html", context)
