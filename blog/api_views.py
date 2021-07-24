from django.shortcuts import get_object_or_404,get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PostSerializers
from .models import Post

@api_view(['GET'])
def post_list_api(request):
    all_posts=get_list_or_404(Post)
    data = PostSerializers(all_posts,many=True).data
    return Response({'data':data})

@api_view(['GET'])
def post_detail_api(request,id):
    post=get_object_or_404(Post,id=id)
    data = PostSerializers(post).data
    return Response({'data':data})