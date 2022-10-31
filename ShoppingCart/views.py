from django.views.generic import View, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductAddForm
from .models import Producto
from django.urls import reverse_lazy
# Create your views here.
class ProductListView(View):
    def get(self, request, *args, **kwargs):
        products = Producto.objects.all()
        context = {
            'productos':products
        }
        return render(request, 'product_list.html', context)
class ProductCreateView(View):
    def get(self, request, *args, **kwargs):
        form=ProductAddForm()
        context = {
            'form':form
        }
        return render(request, 'product_create.html', context)
    def post(self, request, *args, **kwargs):
        if request.method=='POST':
            form = ProductAddForm(request.POST)
            if form.is_valid():
                nombre=form.cleaned_data.get('nombre')
                categoria=form.cleaned_data.get('categoria')
                precio=form.cleaned_data.get('precio')

                p, created = Producto.objects.get_or_create(nombre=nombre, categoria=categoria, precio=precio)
                p.save()
                return redirect('store:product_list')
        context = {}
        return render(request, 'product_create.html', context)
class ProductDetailView(View):
    def get(self, request, pk,*args, **kwargs):
        product = get_object_or_404(Producto, pk = pk)
        context ={'producto':product}
        return render(request,'product_detail.html',context)
class ProductUpdateView(UpdateView):
    model=Producto
    fields=['nombre','categoria','precio']
    template_name='product_update.html'
    def get_success_url(self):
        #pk = self.kwargs['pk'] , kwargs={'pk':pk}
        return reverse_lazy('store:product_list')
class ProductDeleteView(DeleteView):
    model=Producto
    template_name= 'product_delete.html'
    success_url = reverse_lazy('store:product_list')