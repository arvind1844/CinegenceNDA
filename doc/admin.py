from django.contrib import admin



# Register your models here.
from doc.models import *

admin.site.register(Staff)
admin.site.register(Client)
admin.site.register(Visitor)
