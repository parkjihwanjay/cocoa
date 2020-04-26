from django.shortcuts import render
from .forms import PostForm
from .models import Post
from django.shortcuts import redirect
# Create your views here.
def post_home(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_home.html', {'posts' : posts})

def post_detail(request, post_pk):
    post = Post.objects.get(pk = post_pk)
    return render(request, 'blog/post_detail.html', {'post' : post})
    
def post_list(request):
    return render(request, 'blog/post_list.html', {})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            # return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def count(request):
    return render(request, 'wordCount/count.html')

def result(request):
    print('리퀘스트는 : ', request)
    text=request.POST['text']
    splitted_text=text.split()
    word_len = len(splitted_text)
    list_word=[]
    result={}
    
    for i in splitted_text:
        result[i] =splitted_text.count(i)
    
    
    return render(request, 'wordCount/result.html',{
        'word_len':word_len,
        'text':text,
        'result':result,
    })