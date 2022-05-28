from django.urls import path
from . import views

urlpatterns = [
    path('', views.LandView.as_view(),name="home"),
    path('nuevo', views.AddView.as_view(),name="add"),
    path('consulta/<str:email>', views.DView.as_view(),name="detail"),
    path('actualizar/<int:pk>', views.Update_View.as_view(),name="update"),
    path('eliminar/<int:pk>', views.Delete_View.as_view(),name="delete"),
    path('api/<str:email>', views.consult,name="api_consult"),
    path('consulta_api/<str:email>', views.consult_view,name="detalle"),
] 