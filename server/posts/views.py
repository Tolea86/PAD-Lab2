from rest_framework import mixins
from rest_framework.response import Response
from rest_framework_mongoengine.generics import GenericAPIView, get_object_or_404

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework_mongoengine import viewsets
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer

from posts.models import Post
from posts.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    '''
    Contains information about inputs/outputs of a single program
    that may be used in Universe workflows.
    '''
    lookup_field = 'id'
    serializer_class = PostSerializer
    renderer_classes = (JSONRenderer, XMLRenderer)
    parser_classes = (JSONParser, XMLParser)

    def get_queryset(self):
        return Post.objects.all()


class PostsPerUserViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin,
                          viewsets.GenericViewSet):
    renderer_classes = (JSONRenderer, XMLRenderer)

    def get_queryset(self):
        return Post.objects.all()

    def list(self, request, user_id=None):
        queryset = self.get_queryset()(author=user_id)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, id=None, user_id=None):
        queryset = self.get_queryset()(author=user_id)
        post = get_object_or_404(queryset, pk=id)
        serializer = PostSerializer(post)
        return Response(serializer.data)
