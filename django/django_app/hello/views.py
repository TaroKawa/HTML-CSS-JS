from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import HelloForm


class HelloView(TemplateView):
    def __init__(self):
        self.params = {
            "title": "Hello",
            "message": "your data",
            "form": HelloForm()
        }

    def get(self, request):
        return render(request, "hello/index.html", self.params)

    def post(self, request):
        msg = "name: " + request.POST["name"] + \
              "<br>mail:" + request.POST["mail"] + \
              "<br>age:" + request.POST["age"]
        self.params["message"] = msg
        self.params["form"] = HelloForm(request.POST)
        return render(request, "hello/index.html", self.params)


# def index(request, nickname, age):
def index(request):
    # if "msg" in request.GET:
    #     msg = request.GET['msg']
    #     result = 'you typed: "' + msg + '".'
    # else:
    #     result = "Ok"
    ##################################################
    # result = "your account: " + nickname + '"(' + str(age) + ').'
    # return HttpResponse(result)
    ##################################################
    params = {
        'title': "Hello/Index",
        'msg': "OKkkkkkk",
        'goto': '次のページへ',
    }
    return render(request, "hello/index.html", params)


def next(request):
    params = {
        'title': "Hello/Next",
        'msg': 'this is the next page',
        'goto': 'index'
    }
    return render(request, "hello/index.html", params)


def index2(request):
    params = {
        "title": "Hello",
        "message": "your data",
        "form": HelloForm(),
        "OK": "foo bar",
    }
    if (request.method == "POST"):
        params["message"] = "name: " + request.POST["name"] + \
                            "<br>mail:" + request.POST["mail"] + \
                            "<br>age:" + request.POST["age"]
        params["form"] = HelloForm(request.POST)
    return render(request, "hello/index.html", params)

    return render(request, "hello/index.html", params)


def form(request):
    msg = request.POST["msg"]
    params = {
        "title": "Hello/Form,",
        "msg": "こんにちは" + msg + "さん"
    }
    return render(request, "hello/index.html", params)
# Create your views here.
