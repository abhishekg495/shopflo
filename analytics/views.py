# analytics/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from django.views.decorators.cache import cache_page
from asgiref.sync import async_to_sync
from .models import Post
from django_ratelimit.decorators import ratelimit
import json

@cache_page(60 * 15)  # Cache for 15 minutes (adjust as needed)
@ratelimit(key='ip', rate='1/s', block=True)  # Limits POST requests to 1 per second for a given IP
@csrf_exempt
@require_POST
def create_post(request):
    data = json.loads(request.body.decode('utf-8'))
    
    # Check if request contains appropriate fields
    if 'id' not in data or 'content' not in data:
        return JsonResponse({"error": "Invalid payload"}, status=400)
    
    post_id = data['id']
    content = data['content']
    
    try:
        # Check if a post exists with given ID
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post = Post(id=post_id, content=content)
        post.save()
        return JsonResponse({"message": "Post created successfully"}, status=201)
    
    return JsonResponse({"error": "A post already exists with the given id"}, status=400)


@cache_page(60 * 15)  # Cache for 15 minutes (adjust as needed)
@ratelimit(key='ip', rate='1/s', block=True) # Limits GET requests to 1 per second for a given IP
@require_GET
def get_analysis(request, post_id):
    try:
        # Retrieve the post from the database
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return JsonResponse({"error": "Post not found"}, status=404)

    content = post.content

    # Calculate the number of words and average word length
    words = content.split()
    num_words = len(words)
    avg_word_length = sum(len(word) for word in words) / num_words if num_words > 0 else 0
    
    return JsonResponse({"num_words": num_words, "avg_word_length": avg_word_length}, status=200)
