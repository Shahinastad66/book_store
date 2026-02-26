from django.contrib import admin
from user.models import User



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return self.model.all_objects.get_queryset()
    


