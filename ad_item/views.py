from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ItemForm
from .models import ProductImage, Collateral


@login_required
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            # ذخیره محصول بدون ثبت نهایی
            product = form.save(commit=False)

            # افزودن اطلاعات کاربر و موقعیت مکانی
            product.owner = request.user
            product.latitude = request.POST.get('latitude')
            product.longitude = request.POST.get('longitude')

            # ذخیره محصول
            product.save()
            form.save_m2m()  # ذخیره روابط ManyToMany

            # ذخیره تصاویر
            images = request.FILES.getlist('images')
            for image in images:
                ProductImage.objects.create(product=product, image=image)

            return redirect('home:home')
    else:
        form = ItemForm()

    # ارسال اطلاعات وثیقه‌ها برای استفاده در قالب
    collaterals = Collateral.objects.all()
    return render(
        request,
        'add_item/add_item.html',
        {'form': form, 'collaterals': collaterals}
    )
