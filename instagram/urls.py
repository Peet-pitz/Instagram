from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.instagram,name='post'),
    url(r'^no_profile/$',views.welcome,name = 'welcome'),
    url(r'^image/(\d+)',views.image,name ='image'),
    url(r'^new/image$', views.new_image, name='new-image'),
    url(r'^profile/',views.profile,name = 'insta-Profile'),
    url(r'^edit-profile/',views.edit_profile,name = 'edit-profile'),
    url(r'^comment-photo/',views.comment_photo,name = 'comment-photo'),
    # url(r'^comment/(?P<image_id>\d+)', views.comment, name='comment'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^search_profile/(\d+)',views.search_profile,name = 'search_profile'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)