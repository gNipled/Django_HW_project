from django.contrib.auth.mixins import PermissionRequiredMixin
from django.forms import inlineformset_factory
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from catalog.forms import ProductForm, VersionForm, ModerProductForm
from catalog.models import Product, Category, Blog, Version


# def home(request):
#     product_list = Product.objects.all()
#     context = {
#         'object_list': product_list
#     }
#     return render(request, 'catalog/home.html', context)


class HomeListView(ListView):
    model = Product
    template_name = 'catalog/home.html'

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args, **kwargs)
        data['version'] = Version.objects.all,

        return data


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('InputName')
        email = request.POST.get('InputEmail')
        message = request.POST.get('InputMessage')
        print(f'{name} ({email}): {message}')
    return render(request, 'catalog/contacts.html')


# def product(request, pk):
#     context = {
#         'object': Product.objects.get(pk=pk)
#     }
#     return render(request, 'catalog/product.html', context)


class ProductDetailView(DetailView):
    model = Product
    form_class = ProductForm


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        self.object = form.save()
        self.object.created_by = self.request.user
        self.object.save()
        
        return super().form_valid(form)


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')
    permission_required = ('catalog:set_published', 'catalog:change_description', 'catalog:change_category')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.created_by !=self.request.user and not self.request.user.is_staff:
            raise Http404
        return self.object

    def get_form_class(self):
        if self.request.user.is_staff:
            return ModerProductForm
        return ProductForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        Versionformset = inlineformset_factory(Product, Version, form=VersionForm)
        if self.request.method == 'POST':
            formset = Versionformset(self.request.POST, instance=self.object)
        else:
            formset = Versionformset(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'catalog:delete_product'
    model = Product
    success_url = reverse_lazy('catalog:home')


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'preview', 'is_published')
    success_url = reverse_lazy('catalog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()

        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog
    
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'preview', 'is_published')
    # success_url = reverse_lazy('catalog:blog_post')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:blog_post', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog_list')
