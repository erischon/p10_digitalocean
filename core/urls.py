from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webapp.urls')),
    path('database/', include('database.urls')),
    path('users/', include('users.urls')),
    path('search/', include('search.urls')),
]

handler400 = 'webapp.views.error_404'
handler403 = 'webapp.views.error_404'
handler404 = 'webapp.views.error_404'

def handler500(request, *args, **argv):
    response = render_to_response('webapp/500.html', {}, context_instance=RequestContext(request))
    response.status_code = 500
    return response