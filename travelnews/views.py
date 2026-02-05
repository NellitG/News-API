from django.http import JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET

@require_GET
def get_travel_news(request):
    url = "https://newsapi.org/v2/everything"
    params = {
        'q': 'travel',
        'language': 'en',
        'sortBy': 'publishedAt',
        'apiKey': '5c70a4b09c114d5387cfeb30c9af0da2',
    }
    try:
        response = requests.get(url, params=params)
        data = response.json()
        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@require_GET
def get_destinations(request):
    url = "https://newsapi.org/v2/everything"
    params = {
        'q': 'beautiful places to visit',
        'language': 'en',
        'sortBy': 'relevancy',
        'apiKey': '5c70a4b09c114d5387cfeb30c9af0da2',
    }
    try:
        response = requests.get(url, params=params)
        data = response.json()

        # Extract useful details for your frontend
        destinations = []
        for article in data.get("articles", []):
            destinations.append({
                "title": article.get("title"),
                "description": article.get("description"),
                "image": article.get("urlToImage"),
                "url": article.get("url"),
                "publishedAt": article.get("publishedAt"),
                "source": article.get("source", {}).get("name"),
            })

        return JsonResponse({"destinations": destinations}, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
