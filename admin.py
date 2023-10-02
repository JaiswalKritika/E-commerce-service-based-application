from django.contrib import admin

from members.Category import *
from members.main_model import *
from members.models import *
# from members.login_models import *

# Register your models here.
admin.site.register(catego)
admin.site.register(SubCatego)
admin.site.register(Users)
admin.site.register(AddService)
admin.site.register(Profile)