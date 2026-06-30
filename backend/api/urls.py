from api.views import ProcessMailAPIView, RebuildRAGAPIView
from django.urls import path


urlpatterns = [
    path("process-email", ProcessMailAPIView.as_view(), name="process-email"),
    path(
        "rebuild-rag/",
        RebuildRAGAPIView.as_view(),
        name="rebuild-rag"
    ),

]