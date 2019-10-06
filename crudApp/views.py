from django.shortcuts import render,get_object_or_404,redirect
from Cbvpractice import settings
from .models import Post, Product
from .forms import PostForm, ProductForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    # print(settings.BASE_DIR)
    # print(settings.TEMPLATES['DIR'])
    post = Post.objects.all()
    return render(request,'home.html',{'posts':post})
class Home(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
class Home(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request,'create_post.html',{'form':form})
class Create_post(CreateView):
    model = Post
    template_name = 'create_post.html'
    form_class = PostForm
    success_url = reverse_lazy('home')
class Create_post(CreateView):
    model = Product
    template_name = 'create_post.html'
    form_class = ProductForm
    success_url = reverse_lazy('home')

def edit_post(request,post_pk):
    post = get_object_or_404(Post, id = post_pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance = post)
        if form.is_valid():
            form.save()
            # return render(request,'home.html',{'posts':Post.objects.all()})
            return redirect('home')
    else:
        form = PostForm(instance=post)
    return render(request,'create_post.html',{'form':form})
class Edit_post(UpdateView):
    model = Post
    template_name = 'create_post.html'
    form_class = PostForm
    success_url = reverse_lazy('home')
class Edit_post(UpdateView):
    model = Product
    template_name = 'create_post.html'
    form_class = ProductForm
    success_url = reverse_lazy('home')

def delete_post(request,post_pk):
    post = get_object_or_404(Post, id = post_pk)
    post.delete()
    return redirect('home')
class Delete_post(DeleteView):
    model = Post
    success_url = reverse_lazy('home')
    template_name = 'delete_post.html'
    def post(self, request, *args, **kwargs):
        if "cancle" in request.POST:
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super(Delete_post, self).post(request, *args, **kwargs)
    def get_success_url(self):
        return reverse_lazy('home')
class Delete_post(DeleteView):
    model = Product
    success_url = reverse_lazy('home')
    template_name = 'delete_post.html'
    def post(self, request, *args, **kwargs):
        if "cancle" in request.POST:
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super(Delete_post, self).post(request, *args, **kwargs)
    def get_success_url(self):
        return reverse_lazy('home')

def detail_post(request,post_pk):
    post = get_object_or_404(Post, id = post_pk)
    return render(request,'detail_post.html',{'post':post})
class Detail_post(DetailView):
    model = Post
    template_name = 'detail_post.html'
class Detail_post(DetailView):
    model = Product
    template_name = 'detail_product.html'


