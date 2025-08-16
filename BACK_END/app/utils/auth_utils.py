import jwt
import datetime
import config
from flask import request,jsonify
from functools import wraps


def create_token(name,role):
 try:
    payload={
        "user":name,
        "user_role":role,
        "exp":datetime.datetime.utcnow()+datetime.timedelta(hours=12)}

    token=jwt.encode(payload,config.key,algorithm="HS256")
    return token
 except Exception as e:
   return None

def token_req(f):
  @wraps(f)
  def decorated(*arg,**kwarg):
    token=None
    if "x-access-token" in request.headers():
      token=request.headers["x-access-token"]
    if not token:
      return jsonify({"mes":"missing token"}),401
    
    try:
      data=jwt.decode(token,config.key,algorithm="HS256")

      cur_user={
        "user_id":data["user_id"],
        "role":data["role"]
      }
    except jwt.ExpiredSignatureError:
      return jsonify({"mes":"TOKEN HAS EXPIRED"})
    except jwt.InvalidTokenError:
      return jsonify({"mes":"INVALID TOKEN"}),401
   
    return f(cur_user,*arg,**kwarg)
  return decorated