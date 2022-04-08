import multiprocessing


bind = '10.10.115.30:8000'
workers = multiprocessing.cpu_count() * 2 + 1



### Debugging

reload = True # default: False
reload_engine = 'inotify' # ('auto', 'poll', 'inotify')
reload_extra_files=['templates/message.html',] # (e.g., templates, configurations, specifications, etc.)

# check_config = True # default: False
# print_config = True # default: False




### Logging

accesslog = 'log/gunicorn.log' # command line: --access-logfile FILE
disable_redirect_access_to_syslog = True # default: False, command line: --disable-redirect-access-to-syslog 
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"' # command line: --access-logformat STRING
    #default: '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
            # h - remote address
            # l - '-'
            # u - user name
            # t - date of the request
            # r - status line (e.g GET/HTTP/1.1)
            # m - request method
            # U - url path without query string 
            # q - query string
            # H - protocol
            # s - status
            # B - response length
            # b - response length or '-' (CLF format)
            # f - referer
            # a - user agent
            # T - request time in seconds
            # M - request time in milliseconds
            # D - request time in microseconds
            # L - request time in decimal seconds
            # p - process ID
            # {header}i - request header
            # {header}o - response header
            # {variable}e - environment variable

errorlog = 'log/gunicorn.log' # default: '-', command-line: --error-logfile FILE or --log-file FILE
loglevel = 'info' # ('info', 'debug', 'warning', 'error', 'critical') command-line: --log-level LEVEL
capture_output = True # default: False, command-lind: --capture-output
logger_class = 'gunicorn.glogging.Logger' # default: 'gunicorn.glogging.Logger', command-line: --logger-class STRING
logconfig = None # default: None, command-line: --log-config FILE
syslog = False # default: False, command: --log-syslog




###   Process Naming

proc_name = 'cryptowithpy' # default: None, command: -n STRING or --name STRING
default_proc_name = 'cryptowithpy' # default: 'gunicorn'



###   Security

limit_request_line = 4094 # default: 4094, command: --limit-request-line INT
limit_request_fields = 50 # default: 100, command: --limit-request-fields INT (can’t be larger than 32768.)
limit_request_field_size = 8000 # default: 8190, command: --limit-request-field_size INT (Setting it to 0 will allow unlimited header field sizes)





