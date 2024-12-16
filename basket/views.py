from django.shortcuts import render, redirect, get_object_or_404
from .models import BasketModel
from .forms import BasketForm

# create basket
def create_basket_view(request):
    if request.method == 'POST':
        form = BasketForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('basketList')
    else:
        form = BasketForm()
    return render(request, template_name='basket/create_basket.html', context={'form' : form})

# update basket
def update_basket_view(request, id):
    basket_id = get_object_or_404(BasketModel, id=id)
    if request.method == 'POST':
        form = BasketForm(request.POST, instance=basket_id)
        if form.is_valid():
            form.save()
            return redirect('basketList')
    else:
        form = BasketForm(instance=basket_id)
    return render(request, template_name='basket/basket_update.html',
                  context={
                      'basket_id': basket_id,
                      'form': form
                  }
                  )

# delete basket
def delete_basket_view(request, id):
    basket_id = get_object_or_404(BasketModel, id=id)
    basket_id.delete()
    return redirect('basketList')

# read basket
def basket_list_view(request):
    if request.method == 'GET':
        basket_list = BasketModel.objects.all().order_by('-id')
        context = {
            'basket_list': basket_list
        }
        return render(request, template_name='basket/basket_list.html', context=context)

# detail read basket
def basket_detail_view(request, id):
    if request.method == 'GET':
        basket_id = get_object_or_404(BasketModel, id=id)
        context = {'basket_id': basket_id}
        return render(request, template_name='basket/basket_detail.html', context=context)