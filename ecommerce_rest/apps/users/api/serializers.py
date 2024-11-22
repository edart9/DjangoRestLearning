from rest_framework import serializers
from apps.users.models import User

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model= User
        fields = '__all__'

    def create(self,validated_data):
        user=User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    # estos metodos update y create se sobreescriben ya que asi podemos hacer que se encripten las contrasenas
    def update(self,instance,validated_data):
        updated_user=super().update(instance,validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user

#creamos un serializador para listar, esto es para mantener un orden 
class UserListSerializer(serializers.ModelSerializer):
    # to_representation es la funcion que usa django para poder hacer la visualizacion de los campos que esten en la instacia(objeto)
    # aqui nosotros podriamos especificar que campos de la instancia queremos mostrar al hacer el listado de los objetos guardados 
    #si no sobreescribimos esta funcion, siempre va a mostrar todos los valores de fields
    def to_representation(self,instance):
        return {
            #aqui estamos especificando que campos del objeto queremos mostrar, esto no afectara a los otros casos (put, create, delete)
            #porque esta funcion solo es para el get, este se trabaja como diccionario solo cuando se devuelve asi
            #buena practica seria siempre ver que devuelve en instance para ver como trabajar la data
            #aqui podemos cambiar como devuelve en un get los campos, cambiando las claves sin tener que cambiar el modelo 
            'id':instance['id'],
            'username':instance['username'],
            'email':instance['email'],
            'password':instance['password'],
        }


# #aqui podemos ver como funciona un ModelSerializer de DRF por detras, aqui haciendo las validaciones y el guardado de los datos respectivos
# #estas validaciones tambien podemos hacerlas en el model serializer pero de una manera mas personalizada, las basicas ya estarian cubiertas
# class TestUserSerializer(serializers.Serializer):
#     name= serializers.CharField(max_length=200)
#     email= serializers.EmailField()                  

#     def validate_name(self,value):
#         if 'developer' in value:
#             raise serializers.ValidationError("El nombre no es correcto")
#         print (self.context)
#         return value 
    
#     #aqui lo que hacemos con el if es que si el email esta vacio va a agregar ese mensaje a errors
#     #errors es un array que se crea para guardar los errores del serializador
#     def validate_email(self,value):
#         if value is "":
#             raise serializers.ValidationError("Este campo no puede ir vacio")
#         #Hacemos la validacion del email en el campo email para que cuando haya un error salga de que compo proviene el error 
#         #En base a esto nosostros usamos self para poder usar variables que son del contexto del serializador y no especificas del campo 
#         #como es en este caso self.context['name']
#         #como self.context['name'] es el nombre que estamos validando, y este no es el mismo que se valido arriba, debemos hacer
#         # # nuevamente la validacion, ya que este campo no fue verificado 
#         # if self.validate_name(self.context['name']) in value:
#         #     raise serializers.ValidationError("No puede contener el nombre el email")
#         else:
#             return value

#     def validate (self,data):
#         return data #esta es la informacion ya validada
    
#     #al momento de pasar las pruebas de validacion (is_valid?), se usa un .save de esta data, al hacer uso de esto se corre lo siguiente 
#     # que es eso de create, que usara la data validada, esta es la forma en la que hace el create el modelserializer 
#     def create(self,validated_data):
#         print(validated_data)
#         #aqui es donde tenemos que devolver una clase, no contamos con una clase (una clase es por ejemplo los modelos del crm de django)
#         # por ejempolo cuando usamos model serializer, DRF te pide un modelo, y vos tenes que seleccionar el modelo al cual queres cargar
#         # los datos, esto porque necesitas retornar una clase en create. Ya con esto sabemos entonces que tenemos que retornar la clase (modelo user)
#         # donde queramos guardar la informacion, en este caso es informacion del modelo USER

#         #Metodo POST
#         return User.objects.create(**validated_data)#al pasar con ** hacemos que pase de un diccionario a valores ordenados para el modelo
#         # al usar esto guardamos en la BD, y cuando vos poner en el model serializer model=User, lo que hace es self.model.objects.create

#     #Metodo PUT
#     #este funciona cuando se llama a .save cuando es un put, ya que actualizara los datos, no los guardara como nuevos 
#     def update(self,instance,validated_data):
#         instance.name=validated_data.get('name',instance.name)
#         instance.email=validated_data.get('email',instance.email)
#         instance.save()
#         return instance
