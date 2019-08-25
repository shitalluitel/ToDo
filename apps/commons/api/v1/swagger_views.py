from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.schemas import SchemaGenerator
from rest_framework_swagger import renderers


class SwaggerSchemaView(APIView):
    permission_classes = [AllowAny]
    renderer_classes = [
        renderers.OpenAPIRenderer,
        renderers.SwaggerUIRenderer
    ]

    def get(self, request):
        generator = SchemaGenerator(title='ToDo', urlconf='apps.api.v1.urls', url="/api/v1/")
        schema = generator.get_schema(request=request)

        return Response(schema)
