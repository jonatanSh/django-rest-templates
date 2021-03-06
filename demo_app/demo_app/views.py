from easy_rest.views import RestApiView
from easy_rest.mixins import ModelUnpacker, FunctionUnPackerMixin, DecorativeKeysMixin, HelpMixin, FormPostMixin
from django.views.generic import CreateView, UpdateView, TemplateView
from django.contrib.auth.models import User
from easy_rest.test_framework.recorder.post_record_mixins import PostRecordTestGenerator
from easy_rest.mixins import TemplateContextFetcherMixin, JavascriptContextMixin
from datetime import datetime
from random import randint


class ApiTest(ModelUnpacker, FunctionUnPackerMixin, DecorativeKeysMixin, HelpMixin, RestApiView):
    get_data = {"purpose": "this is a demo for the easy rest framework",
                "usage": {'echo': {"description": "echos back any information use echo",
                                   "usage": '{"action":"echo","data":"any-data"}'}},
                'get_username': {"description": "returns the username of the requested user",
                                 "usage": '{"action":"get_username", "with-model": {"field":"auth.User", "query":{'
                                          '"pk":1}}}'}
                }

    def __init__(self, *args, **kwargs):
        super(ApiTest, self).__init__(*args, **kwargs)

    @staticmethod
    def echo():
        return {"echo": "t"}

    def calculate(self, data):
        return {"result": eval(data)}

    @staticmethod
    def get_username(user):
        return {"username": user.username}


class RestUpdate(FormPostMixin, UpdateView):
    template_name = "demo_app/base.html"
    fields = ['first_name', 'last_name']
    model = User
    success_message = 'details updated successfully'

    def get_object(self, queryset=None):
        return User.objects.get(pk=1)


class RestCreate(FormPostMixin, CreateView):
    fields = ['username', 'password']
    template_name = "demo_app/base.html"
    model = User
    success_message = 'created user successfully'


class WelcomePage(JavascriptContextMixin, TemplateView):
    template_name = 'demo_app/home.html'

    def get_context_data(self, **kwargs):
        ctx = super(WelcomePage, self).get_context_data(**kwargs)
        ctx['data'] = "This is javascript context mixin"
        return ctx


class ActiveTemplate(TemplateContextFetcherMixin, TemplateView):
    template_name = 'demo_app/live_ctx.html'

    def get_context_data(self, **kwargs):
        return {"time": str(datetime.now()), "random_int": randint(0, 100)}


class Error(TemplateView):
    template_name = "demo_app/error.html"
