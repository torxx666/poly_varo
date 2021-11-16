from sanic import Sanic
from sanic.response import json as s_json
from sanic.response import text
import json

app = Sanic("hello_example")

@app.route("/")
async def test(request):
  return json({"hello": "world"})

@app.route("/devices", methods=["POST",])
def create_user(request):
    # print(str(request.body))
    # print(json.loads(request.body))
    print((json.loads(request.body))[0])
    print((json.loads(request.body))[0]['name'])
    return s_json({'device': (json.loads(request.body))[0]['strVal'],
                     'isAuthorised': (json.loads(request.body))[1]['boolVal']} )



if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8000)


