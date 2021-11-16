# poly_varo


1- Magic List in file MagicList.py
2 - issues with sanic-jwt see comments in sanic_jwt.py, even their demo not working, need to dig more, but limited in time

3 - file sanic_devices.py

for Testing : 

```
  curl -iv -H "Content-Type: application/json" -d '[
    {
        "name": "device",
        "strVal": "iPhone",
        "metadata": "not interrsting"
    },
    {
        "name": "isAuthorized",
        "boolVal": False,
        "lastSeen": "not interrsting"
    }
]' http://localhost:8000/devices
```

