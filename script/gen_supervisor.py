

template = '''
[program:programname]
command =/home/username/projectname/bin/python /home/username/projectname/bin/gunicorn -w 4 -k gevent -b 127.0.0.1:7998 runserver:app
directory = /home/username/projectname/pillar/


'''