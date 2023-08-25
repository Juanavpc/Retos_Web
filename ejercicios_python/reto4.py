def vigilante(function):
    def verify(*args, **kwargs):
        view =str(function).split(" ")[1]
        user = args[0] if args else kwargs

        if user['session']:
            if view=='user_function' and user['role'] == 'user':
                function(user)
            elif view == 'admin_function' and user['role'] == 'admin':
                function(user)
            elif view == 'superuser_function' and user['role'] == 'super':
                function(user)
            else:
                print("No tienes permisos")
        else:
            loggin()
    return verify


    
def loggin():
    print("Entre al login")

@vigilante
def user_function(user):
    print(f"¡Bienvenido usuario {user['user']}!")

@vigilante
def admin_function(user):
    print(f"¡Bienvenido usuario {user['user']}!")

@vigilante
def superuser_function(user):
    print(f"¡Bienvenido usuario {user['user']}!")

users = [
    {
        "user": "user123",
        "role": "user",
        "session": False
    },
    {
        "user": "admin123",
        "role": "admin",
        "session": True
    },
    {
        "user": "superuser123",
        "role": "super",
        "session": False
    }
]

for user in users:
    user_function(user)
    admin_function(user)
    superuser_function(user)
