PyAppi
======

PyAppi - Semi-declarative REST APIs helpers library

Allows you declaratively define your API endpoint & parameters.

Supports:
 - Request parameters validation
 - Custom parameters checks
 - Custom parameters conversions
 - Different & custom response formatters
 - Different & custom response serializers
 - Bindings to popular python web frameworks (django, flask, etc.)

Example:

```
appi = Pyappi(adapter=django_adapter)

@appi.wrap
@appi.params({
    'name': {
        'required': True,
        'description': "User name",
        'check': (lambda x: len(x)>4, 'should be longer 4 chars')
    },
})
def say_hello(request, name, **kw):
    return {
        'message': "Hello, " + name,
    }

...

urlpatterns = patterns('', (r'', say_hello))
```
