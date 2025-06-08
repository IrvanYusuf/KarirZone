import time
import os


def upload_to_timestamp(path, instance, filename):
    ext = filename.split('.')[-1]
    timestamp = int(time.time())
    filename = f"{timestamp}.{ext}"
    return os.path.join(path, filename)
