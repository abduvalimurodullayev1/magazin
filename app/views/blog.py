from django.core.paginator import Paginator
from django.shortcuts import render
from app.models.other import Blog


def blog_list_view(request):
    sort_by_created = Blog.objects.order_by('-created_at').all()
    paginator = Paginator(sort_by_created, 3)
    page_number = request.GET.get('page')
    blogs = paginator.get_page(page_number)
    return render(request=request,
                  template_name='app/blog/blog-list.html',
                  context={"blogs":blogs})


def blog_details_view(request, blog_id):
    blog = Blog.objects.filter(id=blog_id).first()
    return render(request=request,
                  template_name='app/blog/blog-details.html',
                  context={"blog":blog})