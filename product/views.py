# Create your views here.
from django.shortcuts import render
from ad_item.models import *
from django.core.paginator import Paginator


def product_list(request):
    category_id = request.GET.get('category')
    categories = Category.objects.all()

    if category_id:
        items = Item.objects.filter(category_id=category_id)
    else:
        items = Item.objects.all()
    paginator = Paginator(items, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'product/products.html',
                  {'items': page_obj, 'categories': categories, 'selected_category': category_id})


from django.shortcuts import render, get_object_or_404
from .models import *
from datetime import datetime


def product_detail(request, id):
    item = get_object_or_404(Item, id=id)
    collateral_type = item.collateral_types.all()
    total_price = None
    days = None

    quantity = None
    error_message = None

    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        quantity = int(request.POST.get('quantity', 0))

        if start_date and end_date and quantity > 0:
            start_date = datetime.strptime(start_date, 'YYYY/MM/DD')
            end_date = datetime.strptime(end_date, 'YYYY/MM/DD')
            days = (end_date - start_date).days

            if days > 0:
                if quantity <= item.quantity_available:
                    total_price = days * item.price_per_day * quantity
                else:
                    error_message = "The requested quantity exceeds available stock."
            else:
                error_message = "End date must be after start date."
        else:
            error_message = "Please fill out all fields correctly."

    return render(request, 'product/detail_product.html', {
        'item': item,
        'days': days,
        'quantity': quantity,
        'total_price': total_price,
        'error_message': error_message,
        'collateral_type': collateral_type,
    })
