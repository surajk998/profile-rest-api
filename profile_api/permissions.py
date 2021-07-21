from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
  '''Allows user to edit their own profile'''

  def has_object_permission(self, request, view, obj):
    '''check user is trying to edit their own profile'''

    if request.method in permissions.SAFE_METHODS:
      return True

    return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
  ''' allows users to update their own status'''
  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True
    return obj.user_profile.id == request.user.id