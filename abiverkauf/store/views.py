from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order, OrderItem, Notification
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def product_list(request):
    products = Product.objects.filter(available__gt=0)
    return render(request, 'store/product_list.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})

@login_required
def create_order(request):
    if request.method == 'POST':
        items = []
        # for simplicity, expect fields: product_id, quantity
        product_id = request.POST.get('product_id')
        qty = int(request.POST.get('quantity', 1))
        is_delivery = request.POST.get('is_delivery') == 'on'
        room = request.POST.get('delivery_room')

        product = get_object_or_404(Product, pk=product_id)
        if qty > product.available:
            messages.error(request, 'Nicht genug verfügbar')
            return redirect('product_detail', pk=product_id)

        order = Order.objects.create(customer=request.user, is_delivery=is_delivery, delivery_room=room if is_delivery else '')
        OrderItem.objects.create(order=order, product=product, quantity=qty)
        product.available -= qty
        product.save()

        messages.success(request, f'Bestellung #{order.id} erfolgreich angelegt')
        return redirect('product_list')
    return redirect('product_list')

@login_required
def seller_dashboard(request):
    if not request.user.is_seller():
        messages.error(request, 'Nur Verkäufer zugelassen')
        return redirect('product_list')
    products = request.user.products.all()
    notifications = request.user.notifications.filter(read=False)
    return render(request, 'store/seller_dashboard.html', {'products': products, 'notifications': notifications})
