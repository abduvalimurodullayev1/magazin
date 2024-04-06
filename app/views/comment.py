from django.shortcuts import redirect
from app.models.other import Product, Comment
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required(login_url='login')
def new_comment(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        Comment.objects.create(
            user=request.user,
            product=product,
            text=request.POST['text']
        )
        messages.info(request, 'Successfully Sended!')
        return redirect('shop-details', product_id)
    return HttpResponse("add comment")


@login_required(login_url='login')
def delete_comment(request, product_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.user:
        comment.delete()
        messages.info(request, 'Successfully Deleted!')
        return redirect('shop-details', product_id)
    return redirect('shop-details', product_id)