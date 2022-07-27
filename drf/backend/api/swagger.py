from drf_yasg import openapi
from drf_yasg.inspectors import SwaggerAutoSchema
from drf_yasg.utils import swagger_auto_schema

class CustomAutoSchema(SwaggerAutoSchema):
    def get_tags(self, operation_keys=None):
        tags = self.overrides.get('tags', None) or getattr(self.view, 'my_tags', [])
        if not tags:
            tags = [operation_keys[0]]
        return tags

class CompanyAccountSwagger:
    rs = {'name': 'list', 'decorator': swagger_auto_schema(operation_summary='所有公司帳號',
                                                           operation_description='''
                                                            - id: 索引值
                                                            - permission: 權限
                                                                - vehicle: 汽機車進出入
                                                                - identity_management: 身份組管理
                                                                - kill_account: 刪除帳號
                                                                - give_permission: 賦予權限
                                                                - create_basic_data: 新增基本資料
                                                                - enter_application: 進場申請
                                                                - work_check: 檢查作業
                                                                - console_management: 後台管理 
                                                                - query_data: 查詢資料
                                                                - contractor: 使用廠商權限
                                                            - phone: 手機
                                                            - name: 名字
                                                            - email: 信箱
                                                            - job_number: 工號 
                                                           ''')}
    c = {'name': 'create', 'decorator': swagger_auto_schema(operation_summary='新增公司帳號',
                                                            operation_description='- ※ phone: 是唯一碼')}
    r = {'name': 'retrieve', 'decorator': swagger_auto_schema(operation_summary='單個公司帳號',
                                                              operation_description='- url id: 公司帳號的ID')}
    u = {'name': 'update', 'decorator': swagger_auto_schema(operation_summary='更新公司帳號資料',
                                                            operation_description='- url id: 公司帳號的ID')}
    d = {'name': 'destroy', 'decorator': swagger_auto_schema(operation_summary='刪除公司帳號',
                                                             operation_description='- url id: 公司帳號的ID')}