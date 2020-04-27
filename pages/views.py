from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args , **kwargs):
    # usrname = request.user
    # print (usrname)
    # return HttpResponse("<h1>Hello " + str(usrname) + "</h1>") #string of html not actual html
    return render (request, "home.html", {})

def contact_view(request, *args , **kwargs):
    # return HttpResponse("<h1>Contact Info: 778-XXX-XXXXX</h1>") #string of html not actual html
    return render (request, "contact.html", {})

def about_view(request, *args , **kwargs):
    # return HttpResponse("<h1>About The Page:</h1>") #string of html not actual html
    my_context = {
        "my_text" : "this is my text",
        "this_is_true" : True,
        "my_number" : 99,
        "my_list" : [10,20,30,40, "abc"],
        "my_html" : "<h1> Passing html sring using safe template filter</h1>"
    }
    return render (request, "about.html", my_context)

def social_view(request, *args , **kwargs):
    # return HttpResponse("<h1>Follow us on instagram:</h1>") #string of html not actual html
    return render (request, "social.html", {})
