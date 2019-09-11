import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.models import Review
from api.serializers import ReviewSerializer

@csrf_exempt
def review_detail(request, pk):
    try:
        review = Review.objects.get(id=pk)
    except Review.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        if request.user == review.created_by:
            return JsonResponse(serializer.data)
        else:
            JsonResponse({'error': 'No access'})
    elif request.method == 'PUT':
        body = json.loads(request.body)
        serializer = ReviewSerializer(instance=review, data=body)
        if serializer.is_valid():
            if request.user == review.created_by:
                serializer.save()
                return JsonResponse(serializer.data)
            else:
                JsonResponse({'error': 'No access'})
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        if request.user == review.created_by:
            review.delete()
            return JsonResponse({})
        else:
            JsonResponse({'error': 'No access'})
    return JsonResponse({'error': 'bad request'})

