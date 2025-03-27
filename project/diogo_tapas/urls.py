"""
URL configuration for diogo_tapas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from reservas.views import HomeView, CreateReservationView, UpdateReservationView, CancelReservationView
from django.urls import path, include
from django.views import ReservationListView, HomeView, SignUpView, logout_view


urlpatterns = [
    path("admin/", admin.site.urls),
] 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('reservations/', ReservationListView.as_view(), name='reservation-list'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', logout_view, name='logout'),
]

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('reservation/', CreateReservationView.as_view(), name='book'),
    path('edit/<int:pk>/', UpdateReservationView.as_view(), name='edit'),
    path('cancel/<int:pk>/', CancelReservationView.as_view(), name='cancel'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('reservas.urls')),
]