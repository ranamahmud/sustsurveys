from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'sustsurveys.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
# Home page 
# Landing page area
    url(r'^$', TemplateView.as_view(template_name='visitor/landing-index.html'), name='landing_index'),
    


    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^pulpo/', include('pulpo_forms.urls'), name='base'),

]
