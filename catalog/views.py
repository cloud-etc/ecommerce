from django.shortcuts import render,  get_object_or_404
from .models import Product, Category
from django.views import generic

class ProductListView(generic.ListView):

	queryset = Product.objects.all()
	#model = Product
	template_name = 'catalogo/product_list.html'
	# variavel chamada no template para preencher o for
	context_object_name = 'products'

product_list = ProductListView.as_view()


class CategoryListView(generic.ListView):

	template_name = 'catalogo/category.html'
	# variavel chamada no template para preencher o for
	context_object_name = 'products'

	def get_queryset(self):
		return Product.objects.filter(category__slug=self.kwargs['slug'])

	def get_context_data(self, **kwargs):
		context = super(CategoryListView, self).get_context_data(**kwargs)
		context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
		return context

category = CategoryListView.as_view()

# def category(request, slug):
#     category = Category.objects.get(slug=slug)
#     context = {
#         'current_category': category,
#         'product_list': Product.objects.filter(category=category),
#     }
#     return render(request, 'catalog/category.html', context)


def product(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render(request, 'catalog/product.html', context)