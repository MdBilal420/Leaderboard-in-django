from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from Scorecard.views import profile_upload, get_points


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', profile_upload, name="profile_upload"),
    path('leads/', get_points, name="leaderboard"),

]
