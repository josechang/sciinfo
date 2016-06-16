from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
import xml.etree.ElementTree as ET
tree = ET.parse("/home/ichiehlin/djangoichieh/ichieh_venv/mysite/templates/paper.xml")


def welcome(request):
    if 'user_name' in request.GET:
        filte=request.GET['cata[]']
	keyword=request.GET['user_name']
        root = tree.getroot()
        showtitle=root[0].text
        showauthor=root[1].text
        showpublisher=root[2].text
        showdata=root[3].text
        showisbn=root[4].text
        showlink=root[5].text
        showabstract=root[6].text
        showimportantpart=root[7].text 
	return render_to_response('result.html',locals())
    else:
        return render_to_response('welcome.html',locals())
def result(request):
    return render_to_response('aaaa.html',locals())   


# Create your views here.
