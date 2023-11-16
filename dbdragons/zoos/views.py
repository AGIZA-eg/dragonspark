from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.utils import timezone


class DragonAddedViewSet(viewsets.ModelViewSet):
    queryset = DragonAdded.objects.all()
    serializer_class = DragonAddedSerializer


class DragonRemovedViewSet(viewsets.ModelViewSet):
    queryset = DragonRemoved.objects.all()
    serializer_class = DragonRemovedSerializer


class DragonLocationUpdatedViewSet(viewsets.ModelViewSet):
    queryset = DragonLocationUpdated.objects.all()
    serializer_class = DragonLocationUpdatedSerializer


class DragonFedViewSet(viewsets.ModelViewSet):
    queryset = DragonFed.objects.all()
    serializer_class = DragonFedSerializer


class MaintenancePerformedViewSet(viewsets.ModelViewSet):
    queryset = MaintenancePerformed.objects.all()
    serializer_class = MaintenancePerformedSerializer


class StaffLoginView(APIView):

    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({"detail": "Login successful"}, status=status.HTTP_200_OK)
        else:
            return Response(
                {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )


class StaffLogoutView(APIView):
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            request.auth.delete()
            logout(request)
            return Response(
                {"detail": "Successfully logged out"}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"detail": "User is not authenticated"},
                status=status.HTTP_401_UNAUTHORIZED,
            )


class DragonScheduleView(APIView):
    def get(self, request, *args, **kwargs):
        dragons = DragonFed.objects.all()
        schedule_data = []

        for dragon in dragons:
            schedule_data.append(
                {
                    "dragon_name": dragon.name,
                    "species": dragon.species,
                    "last_meal_time": dragon.last_meal_time,
                    "is_safe_to_feed": self.is_safe_to_feed(dragon),
                }
            )

        return render(request, "dragon_schedule.html", {"dragons": schedule_data})

    def is_safe_to_feed(self, dragon):
        return (
            dragon.last_meal_time is None
            or (timezone.now() - dragon.last_meal_time).days >= 2
        )
