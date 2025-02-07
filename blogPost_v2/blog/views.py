from django.shortcuts import render, get_object_or_404
from .models import Article
from . forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def homeView(request):
    return render ( request, 'blog/home.html', {})



def article_list(request):
    articles = Article.objects.all()
    latest_articles = Article.objects.order_by('-created_at')[:3]
    paginator = Paginator(articles, 3)
    page_number = request.GET.get('page', 1)
   
    
    try:
        articles = paginator.page(page_number)
        nums ="a"*articles.paginator.num_pages
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return render(request, 'blog/article_list.html', {'articles': articles, 'latest_articles': latest_articles, 'nums':nums})

# def article_list(request):
#     articles = Article.objects.all()
#     latest_articles = Article.objects.order_by('-created_at')[:3]
#     return render(request, 'blog/article_list.html', {'articles': articles, 'latest_articles': latest_articles})

# class ArticleListView(ListView):
#     """
#     Alternative post list view
#     """
#     model = Article
#     context_object_name = 'articles',
#     paginate_by = 3
#     template_name = 'blog/article_list.html'


def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    related_articles = article.related_articles()
    latest_articles = article.latest_articles()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
    else:
        form = CommentForm()

    return render(request, 'blog/article_detail.html', {
        'article': article,
        'form': form,
        'related_articles': related_articles,
        'latest_articles': latest_articles
    })