from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from shop.forms import BuyProductForm

from shop.models import Product

# Create your views here.
def index(request):
    filters = {
        'quantity__gt': 0
    }

    if 'search' in request.GET:
        filters["title__contains"] = request.GET["search"]

    products = Product.objects.filter(**filters)
    return render(request, 'shop/index.html', {'products': products})

def get(request, id):
   
    product = get_object_or_404(Product, id=id, quantity__gt=0)
    form = BuyProductForm()
    
    return render(request, "shop/product.html", { 'product' : product, 'form': form })

def buy(request, id):

    if request.method != 'POST':
        return HttpResponseBadRequest("The Http method must be POST")

    
    product = get_object_or_404(Product, id=id, quantity__gt=0)
    form = BuyProductForm(request.POST)

    if form.is_valid():

        if product.quantity < form.cleaned_data["quantity"] :
            return HttpResponseRedirect("/shop/{}?error=too-much-quantity".format(product.id))

        product.removeQuantity(form.cleaned_data["quantity"])
        product.save()
        return HttpResponseRedirect("/shop")
    
    return HttpResponseRedirect("/shop/{}".format(product.id))

        
def messenger(request):
    return render(request, "shop/messenger.html")