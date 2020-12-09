from .views import Registered_Users_List

def Give_Registered_Users(req):
    return {'registered_users': Registered_Users_List}