from django.contrib import admin
from .models import categories
from .models import matelas
from .models import types
from .models import dimensions

admin.site.register(matelas)
admin.site.register(categories)
admin.site.register(types)
admin.site.register(dimensions)

