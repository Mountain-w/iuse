from django.db import models
from django.contrib.auth.models import User
from sources.models import Source
from utils.modelshelpers.enums import FileType
from sources.SourceServer import SourceServer
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    avatar = models.FileField(null=True)
    nickname = models.CharField(null=True, max_length=200)
    source_path = models.ForeignKey(Source, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} {self.nickname}"


def get_profile(user):
    if hasattr(user, '_cached_user_profile'):
        return getattr(user, '_cached_user_profile')
    if UserProfile.objects.filter(user=user).exists():
        profile = UserProfile.objects.get(user=user)
    else:
        profile = create_profile_and_dir(user)
    setattr(user, '_cached_user_profile', profile)
    return profile


def create_profile_and_dir(user):
    """
    创建用户时初始化用户文件夹
    """
    source_path = Source.objects.create(name=user.username, type=FileType.DIR, owner=user)
    return UserProfile.objects.create(user=user, source_path=source_path)


User.profile = property(get_profile)
