import sys
from django.contrib.auth import authenticate, login
import json
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, Http404
from django.shortcuts import render, redirect
from random import randint

from kompany.views import cart_count
from kompany.models import Products
from user.forms import SignUpForm, LoginForm
from user.models import Cart, Orders, Addressbook


def signup(request):
    if request.user.is_authenticated():
        return redirect('/home/')
    else:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('/home/')
        else:
            form = SignUpForm()
        return render(request, 'signup.html', {'form': form})


def log_in(request):
    if request.user.is_authenticated():
        return redirect('/home/')
    else:
        form = LoginForm(request.POST or None)
        print(form)
        if request.POST and form.is_valid():
            user = form.login(request)
            if user:
                login(request, user)
                return HttpResponseRedirect("/")  # Redirect to a success page.
        print(form)
        return render(request, 'login.html', {'login_form': form})


def cart(request):
    if request.user.is_authenticated():
        size = 0
        size = cart_count(request.user)
        product_list = Cart.objects.filter(user=request.user).select_related()
        price = 0.0
        for product in product_list:
            price += (product.product.discounted_price * product.quantity)
        if len(product_list) > 0:
            cont_dict = {
                'product_list': product_list,
                'price': price,
                'size': size,
            }
        else:
            cont_dict = {
                'empty_cart': 'The cart is empty',
                'size': size,
            }

        return render(request, 'cart.html', cont_dict)
    else:
        raise Http404('Please Log in')


def remove_item_from_cart(request, product_id):
    if request.user.is_authenticated():
        query = Cart.objects.filter(user=request.user, product_id=product_id)
        print(query)
        query.delete()
        return redirect('../../cart')


def add_item(request):
    print(request.user.is_authenticated())
    print(request.is_ajax())
    if request.user.is_authenticated() and request.is_ajax() and request.GET:

        try:
            product_id = request.GET.get('q')
            print(product_id)
            if len(Cart.objects.filter(product_id=product_id, user=request.user)) > 0:
                item = Cart.objects.filter(product_id=product_id, user=request.user)
                for i in item:
                    i.quantity = int(i.quantity + 1)
            else:
                item = Cart()
                item.product = Products.objects.get(product_id=product_id)
                item.user = request.user
                item.quantity = 1
                item.save()
            size = cart_count(request.user)
            json_response = {'cart_count': size}
            # perform operations on the user name.
            print(json_response)
            return JsonResponse(json_response)
        except:
            e = sys.exc_info()
            print(e)
            return HttpResponse(e)
            # print('add_item \n' + str(len(Cart.objects.filter(product_id=product_id, user=request.user))))
            # if len(Cart.objects.filter(product_id=product_id, user=request.user)) > 0:
            #     item = Cart.objects.filter(product_id=product_id, user=request.user)
            #     for i in item:
            #         i.quantity = int(i.quantity + 1)
            # else:
            #     item = Cart()
            #     item.product = Products.objects.get(product_id=product_id)
            #     item.user = request.user
            #     item.quantity = 1
            #     item.save()
            # print(request.get_full_path())
            # return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        return redirect('user:signup')


def check_out(request):
    if request.user.is_authenticated():
        cart_items = Cart.objects.filter(user=request.user)
        price = 0
        order_no = random_with_n_digits(6)
        for product in cart_items:
            price += (product.product.discounted_price * product.quantity)
        print(len(Addressbook.objects.filter(user=request.user)))
        print('No of address')
        if len(Addressbook.objects.filter(user=request.user)) > 0:
            address = Addressbook.objects.get(user=request.user)
            print(address.locality)
            cont_dict = {
                'order_items': cart_items,
                'price': price,
                'address': address,
                'order_no': order_no,
            }
        else:
            cont_dict = {
                'order_items': cart_items,
                'price': price,
                'order_no': order_no,
            }
        return render(request, 'checkout.html', cont_dict)


def check_out_item(request, product_id):
    if request.user.is_authenticated():
        print('Product id in checkout' + str(product_id))
        if len(Cart.objects.filter(product_id=product_id, user=request.user)) > 0:
            item = Cart.objects.filter(product_id=product_id, user=request.user)
            for i in item:
                i.quantity = int(i.quantity + 1)
                i.save()
        else:
            item = Cart()
            item.product = Products.objects.get(product_id=product_id)
            item.user = request.user
            item.quantity = 1
            item.save()
        print('item saved to cart')
        return redirect('user:check_out')
    return redirect('user:signup')


def add_address(request):
    addr = Addressbook()
    print(request.body)
    print(request.POST.keys())
    addr.user = request.user
    addr.house_number = request.POST.get('house')
    addr.locality = request.POST.get('locality')
    addr.region = request.POST.get('region')
    addr.postcode = request.POST.get('postcode')
    addr.country = request.POST.get('country')
    addr.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def random_with_n_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)


def order_placed(request):
    cart_items = Cart.objects.filter(user=request.user)
    i = 0
    for item in cart_items:
        purchase_item = Orders()
        purchase_item.user = item.user
        purchase_item.quantity = item.quantity
        purchase_item.product = item.product
        print(str(i) + '==<<')
        i = i + 1
        purchase_item.save()
        item.delete()
    return render(request, 'order-placed.html')
