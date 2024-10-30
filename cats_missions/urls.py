from django.urls import path

from .views import (RetrieveCatsApiView, 
                    CreateCatApiView,
                    RetrieveUpdateDestroyCatAPIView,
                    CreateMissionApiView,
                    RetrieveMissionsApiView,
                    RetrieveUpdateDestroyMissionAPIView,
                    UpdateTargetApiView)

urlpatterns = [
    path('cats/', RetrieveCatsApiView.as_view(), name='get_cats'),
    path('cat/create/', CreateCatApiView.as_view(), name='create_cat'),
    path('cat/<int:pk>', RetrieveUpdateDestroyCatAPIView.as_view(), name='del_upd_cat'),
    path('mission/create/', CreateMissionApiView.as_view(), name='create_mission'),
    path('missions/', RetrieveMissionsApiView.as_view(), name='get_missions'),
    path('mission/<int:pk>', RetrieveUpdateDestroyMissionAPIView.as_view(), name='del_upd_mission'),
    path('target/<int:pk>', UpdateTargetApiView.as_view(), name='update_target')

]