# Create your views here.
import uuid
from PasteText.models import *
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect,HttpResponse
import datetime

@csrf_exempt
def new_paste(request):
    if request.method == 'POST' :
        hash_id = handle_new_paste(request)
        url_to_redirect = "/"+hash_id+"/"
        return HttpResponseRedirect(url_to_redirect)
    else:
        return render_to_response('paste_home.html')

@csrf_exempt
def handle_new_paste(request):
    hash_id = get_unique_id()
    content = str(request.POST.get('user_text',""))
    current_time = datetime.datetime.now()
    title = str(request.POST.get('title'))
    if len(title) == 0:
        title = "Untitled"
    print current_time
    print hash_id
    print title
    print content

    contentData = Content(unique_hash_id = hash_id,content=content,pasted_time=current_time,paste_title=title)
    contentData.save()

    return hash_id

def show_paste(request,offset):
    query = Content.objects.filter(unique_hash_id = offset)
    print query[0].content
    data = None
    error_flag = False
    if len(query) == 0:
        error_flag = True
    else:
        data = query[0]
    if error_flag :
        print "Successful Query "+data.content
    return render_to_response("view_text.html",locals())

def get_unique_id():
    full_id = uuid.uuid1()
    x = str(full_id)
    return x[:8]

