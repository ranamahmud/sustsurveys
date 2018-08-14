from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
urlpatterns = [
    # Examples:
    # url(r'^$', 'sustsurveys.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
# Home page 
# Landing page area
     url(r'^$', TemplateView.as_view(template_name='visitor/landing-index.html'), name='landing_index'),
    url(r'^about$', TemplateView.as_view(template_name='visitor/landing-about.html'), name='landing_about'),
    url(r'^terms/$', TemplateView.as_view(template_name='visitor/terms.html'), name='website_terms'),
    url(r'^contact$', TemplateView.as_view(template_name='visitor/contact.html'), name='website_contact'),


    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^pulpo/', include('pulpo_forms.urls'), name='base'),

]
