try:
    from src.settings import setting
except ImportError:
    import os
    from src.InspectionCenter import InspectionCenter
    import time
    InspectionCenter.settings()
    time.sleep(1)
    from src.settings import setting