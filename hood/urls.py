from django.conf.urls import url,include
from . import views
from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
    url(r'^$',views.hood,name='hood'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^new_profile/$',views.new_profile,name = 'new_profile'),
    url(r'^edit/profile/$',views.profile_edit,name = 'edit_profile'),
    url(r'^hoods', views.all_hoods, name='hoods'),
    url(r'^createHood/$', views.createHood, name='createHood'),
    url(r'^join/(\d+)', views.join, name='joinHood'),
    url(r'^business/view',views.display_business,name = 'viewbiz'),
    url(r'^business/',views.create_business,name = 'business'),
    url(r'^new/post$', views.new_post, name='newpost'),
    url(r'^comment/(?P<post_id>\d+)', views.comment, name='comment'),






]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)