from django.shortcuts import render
from blog.models import Articles

def create_article(request):
    new_article = Articles.objects.create(
        title = 'Bajo el Bitcoin', 
        description = 'Esta bajisimo, desesperen o salgan a comprar mas', 
        author = 'Jose Ignacio Tessio'
        )
    context = {
        'new_article':new_article
    }
    return render(request, 'articles/new_article.html', context=context)