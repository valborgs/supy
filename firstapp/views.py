from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Post, FileUpload
from .forms import PostForm, FileUploadForm
from .stockapi import findStocks
from .lhapi import findNotices



# Create your views here.

def index(request):
    return render(request, 'firstapp/index.html', {})



def post_list(request):
    # 페이지
    page = request.GET.get('page', '1')
    shownum = request.GET.get('shownum', '5')
    
    # 조회
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    
    # 페이징 처리
    paginator = Paginator(posts, shownum)  # 페이지당 10개씩 보여주기
    posts = paginator.get_page(page)
    return render(request, 'firstapp/post_list.html', {'posts': posts})

@login_required(login_url='/common/login/')
def post_detail(request, pk):
    post = get_object_or_404(Post,pk=pk) #해당 글이 없으면 404페이지를 보여줌
    #post = Post.objects.get(pk=pk)
    return render(request, 'firstapp/post_detail.html', {'post': post})

@login_required(login_url='/common/login/')
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'firstapp/post_edit.html', {'form': form})


@login_required(login_url='/common/login/')
def post_modify(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('post_detail', pk=post.id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.modified_date = timezone.now()  # 수정일시 저장
            post.save()
            return redirect('post_detail', pk=post.id)
    else:
        form = PostForm(instance=post)
    context = {'form': form, 'edit':True}
    messages.error(request, '수정권한이 없습니다')
    return render(request, 'firstapp/post_edit.html', context)


@login_required(login_url='/common/login/')
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('post_detail', pk=post.id)
    post.delete()
    return redirect('post_list')
    

def view_stock(request):
    s_data = findStocks(request.GET.get('sname'))
    return render(request, 'firstapp/view_stock.html', {'stocks': s_data})

def lh_notice(request):
    status = request.GET.get('PAN_SS')
    lh_data = findNotices(status)
    return render(request, 'firstapp/lh_notices.html', {'notices': lh_data, 'status':status})


'''
def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['imgfile'])
            return redirect('fileupload')
    else:
        form = FileUploadForm()
    return render(request, 'firstapp/fileupload.html', {'fileuploadForm': form})
'''


def fileupload(request):
    if request.method == 'POST':
        title = request.POST['title']
        memo = request.POST['memo']
        img = request.FILES["imgfile"]
        fileupload = FileUpload(
            title=title,
            memo=memo,
            imgfile=img,
        )
        fileupload.save()
        return redirect('firstapp:fileupload')
    else:
        fileuploadForm = FileUploadForm()
        return render(request, 'firstapp/fileupload.html', {'fileuploadForm': fileuploadForm})


