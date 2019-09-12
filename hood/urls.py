from django.conf.urls import url,include
from . import views
from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
    url(r'^$',views.hood,name='hood'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^new_profile/$',views.new_profile,name = 'new_profile'),
    url(r'^edit/profile/$',views.profile_edit,name = 'edit_profile'),

]