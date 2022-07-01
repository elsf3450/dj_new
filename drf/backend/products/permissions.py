from rest_framework.permissions import BasePermission
class My_Permission(BasePermission):
    message = '你没有权限'
    def has_permission(self, request, view):
        # 注意request.user是认证后返回的对象
        print("request.user.user_type",request.user.user_type)
        if request.user.user_type == 1:  
            return True
        else:
            self.message = '你是%s用户，你没有权限' % request.user.get_user_type_display()
            return False

    def has_object_permission(self, request, view):
        # 注意request.user是认证后返回的对象
        print("request.user.user_type",request.user.user_type)
        if request.user.user_type == 1:  
            return True
        else:
            self.message = '你是%s用户，你没有权限' % request.user.get_user_type_display()
            return False