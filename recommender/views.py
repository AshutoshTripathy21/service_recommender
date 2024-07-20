from django.shortcuts import render
from django.core.paginator import Paginator
# Create your views here.
from .recommender import handle_user_query, services_df

def home(request):
    categories = services_df['Category'].unique()
    context = {
        'categories': categories
    }
    return render(request, 'home.html', context)

def search(request):
    query = request.GET.get('q', '')
    results = handle_user_query(query)
    paginator = Paginator(results, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'query': query,
        'page_obj': page_obj,
    }
    return render(request, 'results.html', context)
