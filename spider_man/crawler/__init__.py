import os
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_root_path():
    root_path = os.path.dirname(os.path.abspath(__file__))
    return root_path