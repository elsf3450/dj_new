from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken,AuthenticationFailed
from django.utils.translation import gettext_lazy as _
from products.models import User
from cfehome.settings import SECRET_KEY
import jwt


class MyJWTAuthentication(JWTAuthentication):
    def  get_user(self,validated_token):
        # jwt.decode(str(validated_token), SECRET_KEY, algorithms=['HS256'])
        try:
            user_id=validated_token['user_id']
            print("validated_token00",validated_token['user_id'])

        except KeyError:
            raise InvalidToken(_("token contained"))
        try:
            user = User.objects.get(**{'id':user_id})
        except User.DoesNotExist:
            raise AuthenticationFailed(_('USER NOT FOUND'),code='user not found QQ')
        print("useruseruseruseruser",user)
        return user