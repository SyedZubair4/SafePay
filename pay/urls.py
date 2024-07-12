from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.land, name='landingPage'),
    path('redirectToLogin',views.redirectToLogin,name='redirectToLogin'),
    path('Register',views.Register,name="register"),
    path('redirectToHome',views.redirectToHome,name='redirectToHome'),
    path('Login',views.Login,name='UserLogin'),
    path('redirectToEwallet',views.redirectToEwallet,name='redirectToEwallet'),
    path('redirectToTrackOne',views.redirectToTrackOne,name='redirectToTrackOne'),
    path('redirectToTrackTwo',views.redirectToTrackTwo,name='redirectToTrackTwo'),
    path('redirectToEwalletViaLogin',views.redirectToEwalletViaLogin,name='redirectToEwalletViaLogin'),
    path('backToHome',views.backToHome,name='backToHome'),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
