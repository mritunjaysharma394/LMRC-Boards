from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import (Board,Topic,Post,Document)
from django.http import Http404
from django.contrib.auth.models import User
from .forms import (NewTopicForm,DocumentForm)
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def home(request):
    boards = Board.objects.all()
    return render(request,'home.html',{'boards':boards})
def board_topics(request,pk):
    try:
        board = get_object_or_404(Board,pk=pk)
        documents = Document.objects.all()

    except Board.DoesNotExist:
        raise Http404
    return render(request,'topics.html',{'board': board,'documents':documents})
def new_topic(request,pk):
    board = get_object_or_404(Board,pk=pk)
    user = User.objects.first()
    if request.method == 'POST':
        #form1 = NewTopicForm(request.POST)
        form = DocumentForm(request.POST,request.FILES)

        if  form.is_valid():
            #topic = form.save(commit=False)
            #topic.board = board
            #topic.starter = user
            #topic.save()
            form.save()
            #post = Post.objects.create(message = form1.cleaned_data.get('message'),topic=topic,created_by=user)
            return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
    else:
        #form1 = NewTopicForm()
        form = DocumentForm()
    return render(request, 'new_topic.html', {'board': board,'form':form})

def delete_document(request,pk):
    if request.method == "POST":
        document = Document.objects.get(pk=pk)
        document.delete()
    return redirect('board_topics')    






# Create your views here.
