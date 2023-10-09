from django.contrib import admin

# Register your models here.
from .models import Projects, Campaigns, Profile, Posts, Comments, BoardQuestions, Team, Notifications, Investments
# Register your models here.

admin.site.register(Projects)
admin.site.register(Campaigns)
admin.site.register(Profile)
admin.site.register(Posts)
admin.site.register(Comments)
admin.site.register(BoardQuestions)
admin.site.register(Team)
admin.site.register(Notifications)
admin.site.register(Investments)

