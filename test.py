from drf.backend.cfehome.settings import SECRET_KEY

import jwt
# {
#   "token_type": "access",
#   "exp": 1657640000,
#   "jti": "24677f7731564a6c8ec7784502dd7221",
#   "user_id": 27
# }
# eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.ewogICJ0b2tlbl90eXBlIjogImFjY2VzcyIsCiAgImV4cCI6IDE2NTc2NDAwMDAsCiAgImp0aSI6ICIyNDY3N2Y3NzMxNTY0YTZjOGVjNzc4NDUwMmRkNzIyMSIsCiAgInVzZXJfaWQiOiAyNwp9.bjfbb4CujjqrW-WcF233pwo6iv-1O712_ziT2pIsBP4
# ewogICJ0b2tlbl90eXBlIjogImFjY2VzcyIsCiAgImV4cCI6IDE2NTc2NDAwMDAsCiAgImp0aSI6ICIyNDY3N2Y3NzMxNTY0YTZjOGVjNzc4NDUwMmRkNzIyMSIsCiAgInVzZXJfaWQiOiAyNwp9

token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.ewogICJ0b2tlbl90eXBlIjogImFjY2VzcyIsCiAgImV4cCI6IDE2NTc2NDAwMDAsCiAgImp0aSI6ICIyNDY3N2Y3NzMxNTY0YTZjOGVjNzc4NDUwMmRkNzIyMSIsCiAgInVzZXJfaWQiOiAyNwp9.bjfbb4CujjqrW-WcF233pwo6iv-1O712_ziT2pIsBP4'
# token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU3NjEzNDIzLCJqdGkiOiIyNDY3N2Y3NzMxNTY0YTZjOGVjNzc4NDUwMmRkNzIyMSIsInVzZXJfaWQiOjI3fQ.bjfbb4CujjqrW-WcF233pwo6iv-1O712_ziT2pIsBP4'

print(jwt.decode(str(token), SECRET_KEY, algorithms=['HS256']))