from django.shortcuts import render

# Create your views here.
def blog_view(request):
    return render(request, 'blog/blog-home.html')

def blog_single(request):
    context = {'title': 'bitcoin crashed again', 'content': 'bitxoin was flying but now grounded as always', 'author': 'MoAli'}
    return render(request, 'blog/blog-single.html', context)
