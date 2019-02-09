import os
from src.InspectionCenter import InspectionCenter
import time
if os.path.exists(r'src\settings\setting.py'):
    from src.settings import setting
else:
    InspectionCenter.settings()
    time.sleep(1)
    from src.settings import setting