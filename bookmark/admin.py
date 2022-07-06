from atexit import register
from django.contrib import admin
from .models import Bookmark

## admin 페이지에 Bookmark 모델을 등록 ##
admin.site.register(Bookmark) 