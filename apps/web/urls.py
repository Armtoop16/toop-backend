# Core Django imports
from django.conf.urls import include, url

# Local apps imports
from .home.views import IndexView
from .accounts.views import ProfileView

urlpatterns = [
    # Homepage
    url(r'^$', IndexView.as_view(), name='home.index'),
    url(r'^accounts/profile/', ProfileView.as_view(), name='accounts.profile'),

    # Django AllAuth
    url(r'^accounts/', include('allauth.urls')),
]

