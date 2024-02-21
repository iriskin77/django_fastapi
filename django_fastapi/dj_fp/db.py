from .models import ClientInfo, Client, Endpoint, EndpointStates
from django.db.models import Q, Value
from .schemas import Schema


def aggregate(item: Schema):
    #print(item.input_start)
    milliseconds = int(item.input_start.timestamp() * 1000)
    #print(milliseconds)
    res = EndpointStates.objects.filter(Q(endpoint=139) & Q(state_start__gt=milliseconds)).order_by('-state_start')
    query = [obj for obj in res if obj.id % 3 == 0]
    #print(query)
    cl_id = query[2].client_id
    print(cl_id)
    cl = Client.objects.all()
    print(cl)
    #print(client_info)
    #d = {'filtered_count': len(query)}
    #print(res)
    return res


def get_data():
    return EndpointStates.objects.all()
