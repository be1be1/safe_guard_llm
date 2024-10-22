import json
from collections import deque
from datetime import datetime, timedelta

class DataProcessor:
    def __init__(self, max_data_age=600):  # 默认保存10分钟的数据
        self.data_queue = deque()
        self.max_data_age = max_data_age

    def add_data(self, data):
        self.data_queue.append(json.loads(data))
        self.clean_old_data()

    def clean_old_data(self):
        current_time = datetime.now()
        while self.data_queue and (current_time - datetime.fromisoformat(self.data_queue[0]['timestamp'])).total_seconds() > self.max_data_age:
            self.data_queue.popleft()

    def get_processed_data(self):
        # 这里可以添加更复杂的数据处理逻辑
        return list(self.data_queue)

