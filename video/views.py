from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Video
from .serializers import VideoSerializer
from django.http import Http404


# Create your views here.
class ListaVideo(APIView):
    def get_object(self, pk):
	    try:
	    	return Video.objects.get(pk=pk)
	    except Video.DoesNotExist:
	    	raise Http404

    def get(self, request):#listar
    	videos = Video.objects.all()
    	video_json = VideoSerializer(videos, many=True)
    	return Response(video_json.data)

    def post(self, request):#crear
        video_json = VideoSerializer(data=request.data)
        if video_json.is_valid():
            video_json.save()
            return Response(video_json.data, status=201)
        return Response(video_json.errors, status=400)


class DetalleVideo(APIView):
	def get_object(self, pk):
	    try:
	    	return Video.objects.get(pk=pk)
	    except Video.DoesNotExist:
	    	raise Http404

	def get(self, request, pk):#listar por ID
	    video = self.get_object(pk)
	    video_json = VideoSerializer(video)
	    return Response(video_json.data)

	def put(self, request, pk):#modificar
	    video = self.get_object(pk)
	    video_json = VideoSerializer(video, data=request.data)
	    if video_json.is_valid():
	    	video_json.save()
	    	return Response(video_json.data)
	    return Response(video_json.errors, status=400)

	def delete(self, request, pk):#eliminar
		video = self.get_object(pk)
		video.delete()
		return Response(status=204)
