import re

from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from m3.actions.exceptions import ApplicationLogicException
from objectpack.actions import ObjectPack
from objectpack.ui import ModelEditWindow

from .ui import UserAddWindow, PermissionAddWindow


class ContentTypePack(ObjectPack):
    model = ContentType
    add_to_desktop = add_to_menu = True
    can_delete = True
    add_window = edit_window = ModelEditWindow.fabricate(model)


class UserPack(ObjectPack):
    model = User
    add_to_desktop = add_to_menu = True
    can_delete = True
    add_window = edit_window = UserAddWindow

    # def save_row(self, obj, create_new, request, context):
    #     email_pattern = re.compile(r'[^@]+@[^@]+\.[^@]+')
    #     if not email_pattern.match(request.POST['email']):
    #         raise ApplicationLogicException(u'Неверный адрес электронной почты')
    #     super(UserPack, self).save_row(obj, create_new, request, context)


class GroupPack(ObjectPack):
    model = Group
    add_to_desktop = add_to_menu = True
    can_delete = True
    add_window = edit_window = ModelEditWindow.fabricate(model)


class PermissionPack(ObjectPack):
    model = Permission
    add_to_desktop = add_to_menu = True
    can_delete = True
    add_window = edit_window = PermissionAddWindow

