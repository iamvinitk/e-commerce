from django.db import connection
from django.db.models.aggregates import Count
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
from kompany.models import Category, Mobiles, Products, Laptops
from user.models import Cart


def home_page(request):
    size = 0
    if request.user.is_authenticated:
        size = cart_count(request.user)
    categories = Category.objects.all()
    print(categories)
    mobiles = Mobiles.objects.all()[:24]
    laptops = Laptops.objects.all()[:24]
    print(Mobiles.objects.all().query)
    for mobile in mobiles:
        mobile.image_src = '../static/kompany/images/mobiles/' + str(mobile.product_id_id) + '-0.jpeg'
    for laptop in laptops:
        laptop.image_src = '../static/kompany/images/laptops/' + str(laptop.product_id_id) + '-0.jpeg'
    if request.user.is_authenticated():
        print(Cart.objects.annotate(product_count=Count('product_id')).filter(user=request.user).query)
        product_count = Cart.objects.annotate(product_count=Count('product_id')).filter(user=request.user)

        size = (len(product_count))
    cont_dict = {
        'categories': categories,
        'mobile_list': mobiles,
        'laptop_list': laptops,
        'size': size

    }
    return render(request, 'home_page.html', cont_dict)


def category_view(request, category, page_index=1):
    size = 0
    if request.user.is_authenticated():
        size = cart_count(request.user)
    products = []
    print(page_index)
    page_no = int(page_index)
    prev_link = ''
    next_link = ''
    if page_no == 1:
        prev_page = int(page_no)
    else:
        prev_page = int(page_no - 1)
    next_page = int(page_no + 1)
    start_index = int((page_no * 12) - 12)
    end_index = int(page_no * 12)
    if category == 'mobile':
        prev_link = '/home/mobile/' + str(prev_page)
        next_link = '/home/mobile/' + str(next_page)
        products = Mobiles.objects.all()[start_index:end_index]
        for product in products:
            if len(product.product_name) > 25:
                product.product_name = product.product_name[:25] + '...'
            product.image_src = '/static/kompany/images/mobiles/' + str(product.product_id_id) + '-0.jpeg'
    if category == 'laptop':
        prev_link = '/home/laptop/' + str(prev_page)
        next_link = '/home/laptop/' + str(next_page)
        products = Laptops.objects.all()[start_index:end_index]
        for product in products:
            if len(product.product_name) > 25:
                product.product_name = product.product_name[:25] + '...'
            product.image_src = '/static/kompany/images/laptops/' + str(product.product_id_id) + '-0.jpeg'
    page_list = {'prev': prev_link, 'next': next_link}
    if len(products) == 0:
        cont_dict = {
            'product_list': products,
            'page_list': page_list,
            'error_list': '  ',
            'size': size,
        }
    else:
        cont_dict = {
            'product_list': products,
            'page_list': page_list,
            'size': size,

        }
    return render(request, 'category-page.html', cont_dict)


def product_page(request, product_id):
    size = 0
    if request.user.is_authenticated:
        size = cart_count(request.user)
    category_type = str(Products.objects.get(product_id=product_id).category_type)
    products = []
    product_i = str(product_id)
    print(category_type + '<==')
    if category_type == 'laptop':
        products = Laptops.objects.get(product_id=product_id)

    if category_type == 'mobile':
        products = Mobiles.objects.get(product_id=product_id)

    num = int(Products.objects.get(product_id=product_id).image_count)

    image_list = []
    for i in range(0, num):
        image_list += ['/static/kompany/images/' + category_type + 's/' + str(product_id) + '-' + str(i) + '.jpeg']

    cont_dict = {
        'product_list': products,
        'image_list': image_list,
        'category_type': category_type,
        'product_i': product_i,
        'size': size,
    }
    return render(request, 'product-page.html', cont_dict)


def search(request):
    query = request.GET.get('q')
    if query is not None and query != '' and request.is_ajax():
        products = Products.objects.filter(product_name__contains=query)[:8]

        return render(request, 'search.html', {'products': products})

    return render(request, 'search.html')


def cart_count(user):
    c = connection.cursor()
    size = 0
    userid = int(User.objects.get(username=user).pk)
    try:
        c.callproc('cartcount', [userid, ])
        size = c.fetchone()[0]
        return size
        # for row in result_set:
        #     i = row[0]
        #     print(i)
    except ConnectionError:
        pass
    finally:
        c.close()
