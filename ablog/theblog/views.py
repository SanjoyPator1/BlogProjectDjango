from functools import total_ordering
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.
# def home(request):
#     return render(request,'home.html', {})



def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    # print("user added to likedList")

    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
        # print("disliked now - LikeView")
    else:
        post.likes.add(request.user)
        liked = True
        # print("liked now - LikeView")

    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class ALLDocsView(ListView):
    model = Post
    template_name = 'all_docs.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ALLDocsView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(
            *args, **kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
            # print("liked now - ArticleDetailsView")

        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'


class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})


def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list': cat_menu_list})


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = EditForm
    #fields = ['title', 'title_tag', 'body']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

# summernote try
from django import forms
from django.shortcuts import render
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class SampleForm(forms.Form):
    desc1 = forms.CharField(
        label='iframe',
        widget=SummernoteWidget()
    )
    # desc2 = forms.CharField(
    #     label='inplace',
    #     widget=SummernoteInplaceWidget(),
    #     required=False
    # )
    desc3 = forms.CharField(
        label='normal field',
        widget=forms.Textarea,
    )

    def clean(self):
        data = super().clean()

        if 'summer' not in data.get('desc1', ''):
            self.add_error('desc1', 'You have to put ???summer??? in desc1')
            self.fields['desc1'].widget.attrs.update({'class': 'invalid'})
        # if 'note' not in data.get('desc2', ''):
        #     self.add_error('desc2', 'You have to put ???note??? in desc2')
        #     self.fields['desc2'].widget.attrs.update({'class': 'invalid'})


def index(request):
    passed = False
    form = SampleForm()

    if request.method == "POST":
        form = SampleForm(request.POST)
        if form.is_valid():
            passed = True
            form = SampleForm()

    return render(request, 'index.html', {
        'desc1': request.POST.get('desc1'),
        # 'desc2': request.POST.get('desc2'),
        'passed': passed,
        'form': form,
    })

