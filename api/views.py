from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer


@api_view(['GET'])
def getName(request):
    dogs = [    {        "name": "Max",        "type": "Golden Retriever"    },    {        "name": "Buddy",        "type": "Beagle"    },    {        "name": "Charlie",        "type": "Labrador Retriever"    },    {        "name": "Rocky",        "type": "Bulldog"    },    {        "name": "Milo",        "type": "Dachshund"    },    {        "name": "Duke",        "type": "German Shepherd"    }]
    return Response(dogs)

@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getNote(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createNote(request):
    data = request.data
    note = Note.objects.create(
        body=data['body']
    )
    serializers = NoteSerializer(note, many=False)
    return Response(serializers.data)

@api_view(['PUT'])
def updateNote(request, pk):
    data = request.data
    note = Note.objects.get(id=pk)
    serializers = NoteSerializer(note, data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['DELETE'])
def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response("The Note was deleted")