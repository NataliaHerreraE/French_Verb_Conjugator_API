import jwt
import app_config as config
from datetime import datetime, timedelta

expiration = datetime.now() + timedelta(seconds = config.JWT_EXPIRATION)
print(expiration)

jwt_data = {'email': 'scott@email.com', 'id': '6607747c126904fd1007bdef', 'exp': expiration}
print(jwt_data)
#encoded_jwt = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")

encoded_jwt = jwt.encode(payload= jwt_data, key="secret", algorithm="HS256")

print(encoded_jwt)
