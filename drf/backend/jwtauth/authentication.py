from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken,AuthenticationFailed
from django.utils.translation import gettext_lazy as _
from products.models import User




class MyJWTAuthentication(JWTAuthentication):
    def  get_user(self,validated_token):
        try:
            user_id=validated_token['user_id']
        except KeyError:
            raise InvalidToken(_("token contained"))
        try:
            user = User.objects.get(**{'id':user_id})
        except User.DoesNotExist:
            raise AuthenticationFailed(_('USER NOT FOUND'),code='user not found QQ')
        print("useruseruseruseruser",user)
        return user