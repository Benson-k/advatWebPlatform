
from advat.forms import PostForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from rest_framework import generics
from rest_framework import mixins
from .models import Post
from .serializers import AdvatSerializer






@login_required
def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES )
        if form.is_valid():
            sale = form.save(commit=False)
            sale.vendor = request.user
            sale.banner = request.FILES['banner']

            sale.save()

            posts = Post.objects.filter().order_by('-start_date')
            user = request.user.username

            return  archive(request,user)
    else:
        form = PostForm()
    variables = RequestContext(request, {
        'form': form})
    return render(request, 'advat/post.html', variables)

def archive(request,shop):
    posts = Post.objects.filter().order_by('-start_date')
    return  render(request,'advat/view.html', {'posts':posts})






class ApiList(mixins.ListModelMixin,
              mixins.CreateModelMixin,
              generics.GenericAPIView):

    queryset = Post.objects.all()
    serializer_class = AdvatSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CategoryList(generics.ListAPIView):
    serializer_class = AdvatSerializer
    def get_queryset(self):

        category = self.kwargs['category']
        return Post.objects.filter(category=category)


class LocationList(generics.ListAPIView):
    serializer_class = AdvatSerializer
    def get_queryset(self):

        location = self.kwargs['location']
        return Post.objects.filter(location=location).order_by(self, )

class LocationCategoryList(generics.ListAPIView):
    serializer_class = AdvatSerializer
    def get_queryset(self):

        location = self.kwargs['location']
        category = self.kwargs['category']
        return Post.objects.filter(location=location,category=category)
