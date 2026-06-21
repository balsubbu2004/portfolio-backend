from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from .models import Project, Skill, Contact, HeroProfile, AboutSection, BlogPost
from rest_framework.generics import RetrieveAPIView
from .serializers import (
    ProjectSerializer, SkillSerializer, ContactSerializer,
    HeroProfileSerializer, AboutSectionSerializer, BlogPostSerializer
)

class ProjectListView(ListAPIView):
    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer

class SkillListView(ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class ContactCreateView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class HeroProfileView(ListAPIView):
    queryset = HeroProfile.objects.all()
    serializer_class = HeroProfileSerializer

class AboutSectionView(ListAPIView):
    queryset = AboutSection.objects.all()
    serializer_class = AboutSectionSerializer

class BlogPostListView(ListAPIView):
    queryset = BlogPost.objects.all().order_by('-created_at')
    serializer_class = BlogPostSerializer
    
class ProjectDetailView(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ContactCreateView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Send email notification
        name = serializer.validated_data.get('name')
        email = serializer.validated_data.get('email')
        message = serializer.validated_data.get('message')

        try:
            send_mail(
                subject=f'Portfolio Contact — message from {name}',
                message=f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=False,
            )
        except Exception as e:
            print(f'Email sending failed: {e}')

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)