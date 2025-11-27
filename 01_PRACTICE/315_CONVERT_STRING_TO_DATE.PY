from datetime import datetime

date_str = "2025-11-27 14:30"
date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M")

print("Converted datetime:", date_obj)
