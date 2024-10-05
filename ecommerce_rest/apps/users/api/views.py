from rest_framework.views import APIView
from apps.users.models import User
from apps.users.api.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view 

@api_view(['GET','POST'])
def user_api_view(request):

    if request.method =='GET':
        #cuando es get hacemos lo siguiente : 
            #guardamos todos lo datos de User en users 
        users=User.objects.all()
            #usamos el serializados para serializar a json todos los valores de User y con el many le decimos que son varios objetos
        users_serializer=UserSerializer(users,many=True)
            # Se da la respuesta, lo cual es la parte de data
        return Response(users_serializer.data)
    
    elif request.method =='POST':
            #si hacemos esto deserializa y lo combierte en un objeto y compara si tiene los caracteres del modelo
        user_serializer= UserSerializer(data=request.data)
            #si es que la data que mando en el request contiene los mismos campos que tiene mi modelo user( ya que se convirtio en el objeto user)
        if user_serializer.is_valid():
            #guardamos los datos en el modelo (base de datos o orm de django)
            user_serializer.save()
            #se responde mostrandos los datos resientemente guardados 
            return Response(user_serializer.data)
            #si hay algun error en la respuesta, respondemos los errores que devuele el serializador
        return Response(user_serializer.errors)

#creamos una nueva funcion para mantener el orden 
@api_view(['GET','PUT','DELETE'])
def user_datail_view(request,pk=None):
    #verificamos si es get
    if request.method=='GET':
        #hacemos un filtro para que si no encuentra un user con ese id, no devuelva codigo, sino una cadena vacia 
        user=User.objects.filter(id=pk).first()
        #Le decimos que serialise el valor del usuario con la pk que llamamos 
        user_serializer=UserSerializer(user)
        #devolvemos los datos en formato json que saco el serializador con ese id 
        return Response(user_serializer.data)
    elif request.method=='PUT':
        #sacamos el objeto dependiendo del id 
        user=User.objects.filter(id=pk).first()
        #aqui vemos que es parecido a los otros dos metodos, pero cuando pasamos una data especifica y le decimos que la compare con otra
        #con los mismos campos, este va a actualizar los campos que no sean iguales
        user_serializer=UserSerializer(user,data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        return Response(user_serializer.errors)

    elif request.method=='DELETE':
        user=User.objects.filter(id=pk).first()
        user.delete()
        return Response('Eliminado')