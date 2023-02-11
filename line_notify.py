# curl -o linenotify.py https://raw.githubusercontent.com/victorgau/khpy_linenotify_intro/main/py/linenotify.py
from linenotify import Notify

#測試token
token = "t4IYSHDjxVgVK1hTi3gA54Z7y6PqMtcYQAS8RQUqkKd"
Notify(token, "貼圖", 1, 3)