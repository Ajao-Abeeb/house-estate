from django.shortcuts import render , get_object_or_404 
from .models import Blog, Comment 
 
# Create your views here.

def blog(request):
    blog = Blog.objects.all()
    data = {
        'blog':blog,
    }
    return render(request ,'blog/blog_grid.html', data)

def blog_single(request, id):
   blog_single = get_object_or_404(Blog , pk=id)

   global comments
   if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        comment = request.POST['comment']
        save_comment = Comment.objects.create(name=name,email=email,comment=comment, blog= blog_single )
        comments = save_comment.save()
    
   comments =  Comment.objects.filter(blog = blog_single)
   data = {
       'blog_single' : blog_single,
       'comments': comments
    
   }
    
       
           
   return render(request, 'blog/blog_single.html', data) 