from django.shortcuts import render, redirect
from django.http import HttpResponse
from page01.models import *

# Create your views here.
def index(request) :
    return render(request, 'page01/index.html')

def play(request) :
    return render(request, 'page01/play.html')

count = 0
name = '김현조'
age = 20 
def play2(request) :
    global name, count, age
    count = count + 1   
    if age > 19 :
        status = '성인'
    else:
        status = '청소년'
    diary = ['오늘은 날씨가 맑았다. - 4월 3일', '미세먼지가 너무 심하다. (4월 2일)', '비가 온다. 4월 1일에 작성']
    return render(request, 'page01/play2.html',{'name': name, 'cnt': count, 'age': status, 'diary': diary })

event_count = 0
def event(request) :
    global event_count
    event_count += 1
    WINNING_NUM = 7
    win = '꽝...'
    if event_count == WINNING_NUM: 
        win = '당첨!'
    return render(request, 'page01/event.html', {'name': name, 'age': age, 'event_cnt': event_count, 'win': win })

def fail(request):
    message = '비정상적인 접근입니다.'
    return render(request, 'page01/fail.html',{'fail_msg': message })

def warn(request):
    message = '다시 확인해주세요.'
    return render(request, 'page01/warn.html',{'warn_msg': message })

def help(request):
    message = '무엇을 도와드릴까요?'
    return render(request, 'page01/help.html',{'help_msg': message })
    
def newsfeed(request):
    articles = Article.object.all()
    return render(request, 'page01/newsfeed.html',{'articles':articles})

def detail_feed(request, pk):
    article = Article.object.get(pk=pk)

    if request.method == 'POST':
        Comment.object.create(
            article = article,
            author = request.POST['nickname'],
            text = request.POST['reply'],
            password = request.POST['password'],

        )
        return redirect(f'/feed/{ article.pk }')
    return render(request, 'page01/detail_feed.html', {'article': article})

def pages(request):
    page_list = Page.object.all()
    return render(request, 'page01/page_list.html', {'pages': page_list} )

def new_feed(request):
    if request.method == 'POST':
        if request.POST['author'] != '' and request.POST['title'] != '' and request.POST['content'] != '' and request.POST['password'] != '':
            new_article = Article.object.create(
                author = request.POST['author'],
                title = request.POST['title'],
                text = request.POST['content'] + '- 추신: 감사합니다.',
                password = request.POST['password'],
            )
            return redirect(f'/feed/{ new_article.pk }')
    return render(request, 'page01/new_feed.html')

def edit_feed(request, pk):
    article = Article.object.get(pk=pk)
    if request.method == 'POST':
        if request.POST['entering_pw'] == article.password:
            article.author = request.POST['author']
            article.title = request.POST['title']
            article.text = request.POST['content']
            article.save()
            return redirect(f'/feed/{ article.pk }')
        else:
            return redirect('/fail')  # 비밀번호 오류 페이지 이동하기
    return render(request, 'page01/edit.html', {'article':article})

def delete_feed(request, pk):
    article = Article.object.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('/')
    else:
        return redirect('/fail')  # 비밀번호 오류 페이지 이동하기
    return render(request, 'page01/delete.html', {'article': article})

def new_page(request):
    category_list = ['IT', 'Food', 'Sports', 'Entertainment', 'Etc']
    return render(request, 'page01/new_page.html',{'category_list': category_list})

def edit_page(request, pk):
    page =  Page.object.get(pk=pk)
    if request.method == 'POST':
        page.master = request.POST['master']
        page.name = request.POST['title']
        page.text = request.POST['content']
        page.save()
        return redirect('/pages')
    return render(request, 'page01/edit_page.html', {'page':page})

def delete_page(request, pk):
    page = Page.object.get(pk=pk)
    if request.method == 'POST':
        page.delete()
        return redirect('/pages')
    return render(request, 'page01/delete_page.html', {'page': page})

def delete_comment(request, comment_pk):
    comment = Comment.object.get(pk=comment_pk)
    if request.method == 'POST':
        comment.delete()
        return redirect('/')
    return render(request, 'page01/delete_comment.html', {'comment': comment})