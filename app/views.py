import redis
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from app.serializers import MouseSerializer

r = redis.StrictRedis(host='localhost', port=6379, db=0, charset="utf-8", decode_responses=True)


class MouseViewSet(GenericViewSet):
    serializer_class = MouseSerializer

    def create(self, request):
        sequence = int(r.get('sequence'))
        sequence += 1
        r.set('sequence', sequence)

        name = request.data.get('name')
        age = request.data.get('age')

        data = {
            'id': sequence,
            'name': name,
            'age': age,
        }
        mouse = self.get_serializer(data=data)
        mouse.is_valid()
        r.set('name:%s' % sequence, name)
        r.set('age:%s' % sequence, age)
        return Response(mouse.data)

    def retrieve(self, request, pk):
        name = r.get('name:%s' % pk)
        age = r.get('name:%s' % pk)
        mouse = self.get_serializer(data={'id': pk, 'name': name, 'age': age})
        mouse.is_valid()
        return Response(mouse.data)
