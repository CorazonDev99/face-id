from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserProfile
from .serializers import UserProfileSerializer, RecognizeSerializer
import face_recognition
import numpy as np

class UploadPhoto(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            photo = request.FILES['photo']
            user_id = request.data['user_id']

            # Load the image and get the face encoding
            image = face_recognition.load_image_file(photo)
            encodings = face_recognition.face_encodings(image)
            if encodings:
                encoding = encodings[0]
                UserProfile.objects.create(
                    user_id=user_id,
                    photo=photo,
                    encoding=encoding.tobytes()
                )
                return Response({'status': 'photo uploaded'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'No face found in the image'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RecognizePhoto(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RecognizeSerializer(data=request.data)
        if serializer.is_valid():
            image = face_recognition.load_image_file(request.FILES['image'])
            encodings = face_recognition.face_encodings(image)
            if encodings:
                encoding = encodings[0]
                users = UserProfile.objects.all()
                for user in users:
                    known_encoding = np.frombuffer(user.encoding, dtype=np.float64)
                    matches = face_recognition.compare_faces([known_encoding], encoding)
                    if matches[0]:
                        return Response({'user_id': user.user_id}, status=status.HTTP_200_OK)
                return Response({'error': 'No matching user found'}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'error': 'No face found in the image'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
