from django.contrib import admin
from .models import Feedback
# Register your models here.


admin.site.site_header = "HIDDEN EYE"
admin.site.site_title = "HIDDEN EYE ADMIN PANEL"
admin.site.index_title = "Manage HIDDEN EYE"


class Feedback_Admin(admin.ModelAdmin):
    list_display = ('name', 'email', 'comment')


admin.site.register(Feedback, Feedback_Admin)
