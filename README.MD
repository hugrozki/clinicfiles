## Clinic Record Example

Stack: Python 3.7.1 / PostgreSQL

### Instalation


1. Install dependences
```
pip install -r requirements
```

2. Create local settings file (example: clinicfiles/settings_local.py) and set database conection data
```
from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

3. Apply migrations.

4. Load initial data in database
```
python manage.py loaddata accounts.json --settings=clinicfiles.settings_local
```

5. Run server
```
python manage.py runserver --settings=clinicfiles.settings_local
```

### Service

Access to record enpoint
```
http://localhost:8000/demo/v1/accounts/{id}/record
```

If {id} is equal to values 2, 3 or 4 get the next json response

```
{
    "codigo": 200,
    "mensaje": "Petición completada",
    "payload": {
        "no_expediente": 205,
        "fecha_ultima_consulta": "12/05/18",
        "tipo_sangre": "O+",
        "alergias": [
            {
                "nombre": "Rinitivis",
                "fecha_alta": "03/09/10",
                "medicamento": "ospirin 100mg"
            }
        ]
    }
}
```

A 404 Not Found status error is return if {id} is not equal to designed values also the above json response

```
{
    "codigo": 400,
    "mensaje": "El id de usuario no existe"
}
```