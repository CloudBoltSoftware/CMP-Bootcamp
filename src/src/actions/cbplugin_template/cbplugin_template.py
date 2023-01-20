if __name__ == '__main__':
    import os
    import sys
    import django
    sys.path.extend(['/opt/cloudbolt', '/var/opt/cloudbolt/proserv'])
    os.environ["DJANGO_SETTINGS_MODULE"] = "settings"
    django.setup()



def run():
    from infrastructure.models import Server
    servers = Server.objects.filter(status="ACTIVE")
    for server in servers:
        print(server.id, server.hostname)


if __name__ == '__main__':
    run()

