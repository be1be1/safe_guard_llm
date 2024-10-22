# Stadium Security System

## Overview

This project implements a comprehensive security decision-making system for a sports stadium using AI and real-time data analysis. The system collects data from various sources, processes it, and uses a large language model to make security-related decisions.

## Features

- Real-time video stream analysis for pedestrian and vehicle traffic
- Temperature and smoke sensor data collection
- Continuous data processing and aggregation
- AI-powered decision-making for security strategies
- Asynchronous data collection and processing

## Project Structure
stadium_security_system/

│

├── main.py

├── config.py

├── data_collectors/

│ ├── init.py

│ ├── camera_stream.py

│ ├── sensor_data.py

│ └── data_processor.py

├── prompt_engineering/

│ ├── init.py

│ └── prompt_generator.py

├── decision_making/

│ ├── init.py

│ └── llm_decision_maker.py

└── utils/

│ └── data_structures.py

├── config.py

└── main.py

# Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/stadium-security-system.git
   cd stadium-security-system
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure the system by editing `config.py` with your specific settings.

## Usage

Run the main script to start the security system:
python3 main.py


The system will begin collecting data from cameras and sensors, processing the information, and making security decisions at regular intervals.

## Configuration

Edit the `config.py` file to customize:

- Camera stream URLs and locations
- Sensor IDs and locations
- AI model API settings
- Data processing and decision-making intervals

## Components

- **Data Collectors**: Gather data from cameras and sensors
- **Data Processor**: Cleans and aggregates collected data
- **Prompt Generator**: Creates prompts for the AI model based on processed data
- **AI Decision Maker**: Interfaces with a large language model to make security decisions


## License

This project is licensed under the MIT License - see the LICENSE file for details.