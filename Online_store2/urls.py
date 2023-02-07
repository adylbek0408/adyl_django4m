from django.contrib import admin
from django.urls import path
from products.views import ProductsView, ProductDetailView, CategoryView, CreateProduct, MainView
from Online_store2.settings import MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
from users.views import LoginView, RegisterView, LogoutView  # logout_view, login_view, register_view,

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view()),
    path('products/', ProductsView.as_view()),
    path('products/<int:id>/', ProductDetailView.as_view()),
    path('category/', CategoryView.as_view()),
    path('products/create/', CreateProduct.as_view()),

    # users
    path('users/login/', LoginView.as_view()),
    path('users/register/', RegisterView.as_view()),
    path('users/logout/', LogoutView.as_view()),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
