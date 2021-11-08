from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm

urlpatterns = [
    path('', views.ProductView.as_view(), name="home"),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),


    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html', 
    authentication_form=LoginForm), name='login'),
    path('registration/', views.CustomerRegistrationView.
    as_view(), name="customerregistration"),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html',
    form_class=MyPasswordChangeForm),name='passwordchange'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path('checkout/', views.checkout, name='checkout'),
    path('asiandishes/', views.asiandishes, name='asiandishes'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
