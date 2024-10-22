import asyncio
import time
from config import (
    PEOPLE_CAMERA_STREAMS, VEHICLE_CAMERA_STREAMS,
    TEMPERATURE_SENSORS, SMOKE_SENSORS,
    DATA_PROCESSING_INTERVAL, DECISION_MAKING_INTERVAL
)
from data_collectors.camera_stream import CameraStream
from data_collectors.sensor_data import SensorData
from data_collectors.data_processor import DataProcessor
from prompt_engineering.prompt_generator import PromptGenerator
from decision_making.llm_decision_maker import AIDecisionMaker

async def collect_camera_data(camera_stream, data_processor):
    while True:
        data = camera_stream.process_frame()
        if data:
            data_processor.add_data(data)
        await asyncio.sleep(1)  # 每秒处理一帧

async def collect_sensor_data(sensor, data_processor):
    while True:
        data = sensor.read_data()
        data_processor.add_data(data)
        await asyncio.sleep(5)  # 每5秒读取一次传感器数据

async def process_data_and_make_decisions(data_processor, prompt_generator, ai_decision_maker):
    while True:
        await asyncio.sleep(DECISION_MAKING_INTERVAL)
        processed_data = data_processor.get_processed_data()
        prompt = prompt_generator.generate_prompt(processed_data)
        decision = ai_decision_maker.make_decision(prompt)
        print(f"AI决策结果：\n{decision}")

async def main():
    data_processor = DataProcessor()
    prompt_generator = PromptGenerator()
    ai_decision_maker = AIDecisionMaker()

    tasks = []

    # 启动摄像头数据收集任务
    for camera_config in PEOPLE_CAMERA_STREAMS + VEHICLE_CAMERA_STREAMS:
        stream_type = "people" if camera_config in PEOPLE_CAMERA_STREAMS else "vehicle"
        camera_stream = CameraStream(camera_config['url'], camera_config['id'], camera_config['location'], stream_type)
        tasks.append(asyncio.create_task(collect_camera_data(camera_stream, data_processor)))

    # 启动传感器数据收集任务
    for sensor_config in TEMPERATURE_SENSORS + SMOKE_SENSORS:
        sensor_type = "temperature" if sensor_config in TEMPERATURE_SENSORS else "smoke"
        sensor = SensorData(sensor_config['id'], sensor_config['location'], sensor_type)
        tasks.append(asyncio.create_task(collect_sensor_data(sensor, data_processor)))

    # 启动数据处理和决策任务
    tasks.append(asyncio.create_task(process_data_and_make_decisions(data_processor, prompt_generator, ai_decision_maker)))

    # 等待所有任务完成
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())

