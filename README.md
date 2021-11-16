# poly_varo




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
        "boolVal": "False",
        "lastSeen": "not interrsting"
    }
]' http://localhost:8000/devices
```

