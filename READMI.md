**Blog website** 


**#configation of media file**

**#urls**

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
]

# ✅ Serve MEDIA files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#setting

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

**models(table)**

1.category model
2.blog model

**adminstuff**

 list_editable,
search_fields,list_display, prepopulated_fields