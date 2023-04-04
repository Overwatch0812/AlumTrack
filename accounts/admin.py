from django.contrib import admin
# from .models import Custom_User
# from django.contrib.auth.models import User
# from django.contrib.auth.admin import UserAdmin
# Register your models here.
# admin.site.register(User)


from django.contrib import admin
from .models import CustomUser

# Register your models here.
# admin.site.unregister(CustomUser)
admin.site.register(CustomUser)


# class CustomUserInLine(admin.StackedInline):
#     model=Custom_User
#     can_delete=False
#     verbose_name_plural='Custom_Users'

# class Custom_UserAdmin(UserAdmin):
#     inlines=(CustomUserInLine, )

# # admin.site.unregister(User)
# admin.site.register(User,Custom_UserAdmin)