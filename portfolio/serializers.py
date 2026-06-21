from rest_framework import serializers
from .models import Project, Skill, Contact, HeroProfile, AboutSection, BlogPost


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class HeroProfileSerializer(serializers.ModelSerializer):
    effective_projects_completed = serializers.SerializerMethodField()

    class Meta:
        model = HeroProfile
        fields = '__all__'

    def get_effective_projects_completed(self, obj):
        # If user manually set a value greater than 0, use that
        # Otherwise auto-count from the actual Project table
        if obj.projects_completed and obj.projects_completed > 0:
            return obj.projects_completed
        return Project.objects.count()


class AboutSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutSection
        fields = '__all__'


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'
        
