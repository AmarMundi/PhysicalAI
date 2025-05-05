import streamlit as st
import pandas as pd

st.set_page_config(page_title="🧠Physical AI", layout="wide")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("Robotics_Image.png", caption="Ground, Aerial, and Industrial Robots", width=300)

with col2:
    st.image("Robo_Block.png", caption="SmartTwin and Vision X Edge and Quality", width=300)

with col3:
    st.image("Pipeline.png" , caption="training steps", width=400)

st.title("🤖 Physical AI: Automonous Robot Inspections scenario comparison")

# Display image of different robot types with reduced size


# Define data for the table
data = {
    "Category": [
        "Mobility Platforms", "Sensors", "Processing Unit", "Vision AI Models", "Typical Use Cases",
        "Navigation/Tracking", "Power Source", "Communication", "Simulation Tools", "Challenges"
    ],
    "Ground Robots": [
        "Wheeled or legged: Boston Dynamics (Spot), Clearpath Robotics (Husky), Unitree Robotics",
        "LiDAR, Cameras, IMU, GPS: Velodyne, Ouster (LiDAR), Bosch, FLIR (thermal cameras)",
        "NVIDIA (Jetson series), Intel (NUC), Qualcomm",
        "OpenCV, YOLO by Ultralytics, Meta (DETR), Google (ViT), ByteTrack/DeepSORT open-source developers",
        "Inspection, surveillance, logistics, mining",
        "SLAM by SLAMTEC, Cartographer (Google), RTK-GPS by Septentrio",
        "Swappable Li-ion battery systems (Unitree, Boston Dynamics)",
        "Cisco (mesh), Cradlepoint, Sierra Wireless (4G/5G), Rajant (mesh)",
        "ROS Gazebo (Open Robotics), Webots (Cyberbotics)",
        "Terrain, obstacle avoidance, weather conditions, long runtime, SLAM drift"
    ],
    "Aerial Robots (Drones)": [
        "Multirotors, fixed-wing UAVs: DJI, Parrot, Skydio",
        "GPS, Barometer, IMU, Cameras, FLIR, Pixhawk, u-blox",
        "Jetson Nano, Raspberry Pi, Flight Controller",
        "YOLO, ViT, VLMs, CLIP, Optical Flow",
        "Infrastructure Inspection, surveying, search and rescue, agriculture",
        "GPS, Optical Flow, VIO (Visual Inertial Odometry)",
        "Battery (short duration) (limited time, usually <30 min flight)",
        "LoRa, 4G/5G, MAVLink Radio telemetry",
        "PX4 SITL, AirSim",
        "Wind, battery, regulations & regulatory limits"
    ],
    "Industrial Robots": [
        "Stationary robotic arms: Intuitive Surgical, KUKA, ABB",
        "Encoders, force sensors, vision cameras: Keyence, Cognex",
        "High-performance PCs or custom FPGA/ASIC systems: Industrial PCs, Siemens",
        "ViT, CLIP/BLIP (VLMs), semantic segmentation models",
        "Surgery, lab automation, assembly, precision manufacturing",
        "Encoders, vision-based tracking, Camera-guided manipulation",
        "Plugged-in or high-capacity power packs, Continuous power",
        "Ethernet, Profinet, Modbus, OPC UA (Industrial IoT protocols)",
        "MATLAB/Simulink, CoppeliaSim (V-REP)",
        "High Precision, repeatability, harsh environments, safety compliance, latency, sterilization requirements"
    ]
}

# Create dataframe and display
comparison_df = pd.DataFrame(data)
st.dataframe(comparison_df, use_container_width=True)
