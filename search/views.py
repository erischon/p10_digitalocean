from django.shortcuts import render, redirect

from database.models import Product, Substitute
from search.search import Search
from search.forms import RequestForm


def search_results(request):
    ''' I search for substitute to the product requested. '''
    form = RequestForm(request.GET)

    if form.is_valid():
        query = form.cleaned_data['user_request']
    else:
        return render(request, 'search/results.html', {'product': "None"})

    search = Search()
    result_infos = []
    search_product = search.find_product(query)

    if not search_product:
        return render(request, 'search/results.html', {'product': "None"})
    else:
        product = search.product_infos(search_product)

        for categorie in product['categories']:
            result_info = search.find_substitute(search_product)
            result_infos.extend(search.result_infos(result_info))

        result_infos = [i for n, i in enumerate(result_infos) if i not in result_infos[n + 1:]]

        return render(request, 'search/results.html', {'product': product, 'results': result_infos})


def search_sub(request):
    ''' I don't know why I'm here... '''
    return render(request, 'webapp/home.html')


def prodinfos(request, prod_id):
    ''' I give the Product Informations. '''
    try:
        product = Product.objects.get(prod_id=prod_id)
        return render(request, 'search/prodinfos.html', {'product': product})
    except Exception as error:
        return redirect('home', {'error': error})


def saving(request, subproduct, oriproduct):
    ''' I'm saving a Product in the User's Myproduct model. '''
    sub_product = Product.objects.get(prod_id=subproduct)
    ori_product = Product.objects.get(prod_id=oriproduct)
    Substitute.objects.create(substitute_product=sub_product, original_product=ori_product, user=request.user)
    return redirect('myproducts')
