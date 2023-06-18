from unicodedata import category
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse


from .models import *
from .forms  import *
from django.core.paginator import PageNotAnInteger,EmptyPage,Paginator


# Create your views here.

def home(request):
    blogs = Blog.objects.order_by('-posted_date')
    context = {
        "blogs":blogs
    }
    
    return render(request,'home.html',context)


def video(request):
    queryset = Blog.objects.order_by('-posted_date')
    # tags = Tag.objects.order_by('-created._date')
    page = request.GET.get('page',1)
    paginator = Paginator(queryset,4)
    
    try:
        blogs = paginator.page(page)
    except EmptyPage:
        blogs = paginator.page(1)
    except PageNotAnInteger:
        blogs = paginator.page(1)
        return redirect('video')
        
        
    context = {
        "blogs":blogs,
        # "tags":tags,
        "paginator":paginator
    }
    
    return render(request,'video.html',context)



def category_blog(request, slug):
    category = get_object_or_404(Category, slug = slug)
    blogs = category.category_blogs.all()
    # tags = Tag.objects.order_by('-created_date')[:5]
    context = {
        'blogs': blogs
        # 'tags':ta.gs
        }
    return render(request,'category_video.html',context)


@login_required(login_url='/')
def blog_details(request, slug):
    form = TextForm()
    
    blog = get_object_or_404(Blog, slug = slug)
    category = Category.objects.get(id = blog.category.id)
    related_blogs = category.category_blogs.all()
    # tags = Tag.objects.order_by('-created_date')[:5]
    liked_by = request.user in blog.likes.all()
    
    if request.method == "POST":
        form = TextForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                user = request.user,
                blog = blog,
                text = form.cleaned_data.get('text')
            )
            
            return redirect('blogdetails',slug = slug)
    
    context = {
        'blog':blog,
        'related_blogs': related_blogs,
        # 'tags':tags,
        'form':form,
        'liked_by':liked_by
        
    }
    return render(request,'video_details.html',context)

@login_required(login_url='/')
def add_reply(request, blog_id,comment_id):
    blog = get_object_or_404(Blog, id = blog_id)
    
    if request.method == "POST": 
        form = TextForm(request.POST)
        if form.is_valid():            
            reply = get_object_or_404(Comment, id = comment_id)
            Reply.objects.create(
                user = request.user,
                reply = reply,
                text = form.cleaned_data.get('text')
            )
    return redirect('blogdetails',slug = blog.slug)



def scoreboard(request):
    return render(request,'scoreboard.html')

