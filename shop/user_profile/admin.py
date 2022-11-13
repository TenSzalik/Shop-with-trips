from django.contrib import admin
from .models import User

user_models = [
    User,
]

admin.site.register(user_models)
