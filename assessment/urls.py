from django.urls import path, include
from rest_framework_swagger.views  import get_swagger_view
from authy.urls import auth_patterns

swagger_view = get_swagger_view(title='Idea Thinkers Assessment API')
urlpatterns = [
    path('', swagger_view),
    path('auth/', include(auth_patterns)),
]
