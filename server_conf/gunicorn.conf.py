import multiprocessing


bind = '10.10.115.30:8000'
workers = multiprocessing.cpu_count() * 2 + 1