from django.shortcuts import render
from django.core.paginator import Paginator
from .recommender import handle_user_query, services_df, classify_domains_and_subcategories

def home(request):
    categories = services_df['Category'].unique()
    context = {
        'categories': categories
    }
    return render(request, 'home.html', context)

def search(request):
    query = request.GET.get('q', '')
    if query.startswith('problem:'):
        domains, subcategories = handle_user_query(query)
        context = {
            'query': query,
            'domains': domains,
            'subcategories': subcategories,
        }
        return render(request, 'results.html', context)
    else:
        results = handle_user_query(query)
        paginator = Paginator(results, 9)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'query': query,
            'page_obj': page_obj,
        }
        return render(request, 'results.html', context)

def classify(request):
    domains = []
    subcategories = {}
    if request.method == "POST":
        user_input = request.POST.get("problem_statement", "")
        domains, subcategories = classify_domains_and_subcategories(user_input)
    return render(request, 'classification/index.html', {
        'domains': domains,
        'subcategories': subcategories,
        'user_input': request.POST.get("problem_statement", "")
    })