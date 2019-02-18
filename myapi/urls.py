from django.urls import path, include
from .views import LanguageView, ParadigmView, ProgrammerView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('languages', LanguageView)
router.register('paradigms', ParadigmView)
router.register('programmers', ProgrammerView)


urlpatterns = [
    path('', include(router.urls))
]
