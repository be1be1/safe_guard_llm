import json

class PromptGenerator:
    def __init__(self):
        self.prompt_template = """
        根据以下体育场馆的安防数据，分析当前的安全状况并给出相应的安保策略：

        人流数据：
        {people_data}

        车流数据：
        {vehicle_data}

        温度数据：
        {temperature_data}

        烟雾数据：
        {smoke_data}

        请分析上述数据，判断当前场景是否安全，是否需要派遣安保人员，并给出具体的安保策略。
        """

    def generate_prompt(self, processed_data):
        people_data = []
        vehicle_data = []
        temperature_data = []
        smoke_data = []

        for item in processed_data:
            if 'camera_id' in item:
                if 'count' in item['data']:
                    people_data.append(f"位置 {item['location']} 的人流量为 {item['data']['count']}")
                elif 'plate' in item['data']:
                    vehicle_data.append(f"位置 {item['location']} 检测到车牌 {item['data']['plate']}")
            elif 'sensor_type' in item:
                if item['sensor_type'] == 'temperature':
                    temperature_data.append(f"位置 {item['location']} 的温度为 {item['data']['temperature']}°C")
                elif item['sensor_type'] == 'smoke':
                    smoke_data.append(f"位置 {item['location']} 的烟雾浓度为 {item['data']['smoke_level']}")

        prompt = self.prompt_template.format(
            people_data="\n".join(people_data),
            vehicle_data="\n".join(vehicle_data),
            temperature_data="\n".join(temperature_data),
            smoke_data="\n".join(smoke_data)
        )

        return prompt

