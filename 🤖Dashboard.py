import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import folium
from streamlit_folium import st_folium
from PIL import Image

st.set_page_config(page_title="🤖Dashboard", layout="wide")
st.title("🤖 Autonomous Robot Inspections")

st.image("main_image.png" , caption="Wheeled or legged ground robot with camera mounted", width=800)

st.markdown("""
Monitor live status, sensor alerts, location, and anomaly detections from autonomous inspection robots.
""")

# Define anomaly severity and icons
anomaly_severity = {
    "None": 0,
    "Leak": 1,
    "Corrosion": 1,
    "Overpressure": 2,
    "Overheat": 2
}
anomaly_color = {
    "None": "green",
    "Leak": "orange",
    "Corrosion": "orange",
    "Overpressure": "red",
    "Overheat": "red"
}
anomaly_icon = {
    "None": "✅",
    "Leak": "💧",
    "Corrosion": "⚠️",
    "Overpressure": "🔥",
    "Overheat": "🌡️"
}

# Display legend for anomaly severity
st.markdown("""
### ℹ️ Severity Legend
- 🔥 **Overpressure** – Critical (red)
- 🌡️ **Overheat** – Critical (red)
- 💧 **Leak** – Warning (orange)
- ⚠️ **Corrosion** – Warning (orange)
- ✅ **None** – Normal (green)
""")

# Static robot data
data = [
    {
        "Robot ID": "ROBOT-1",
        "Location": "Plant A",
        "Latitude": 37.7749,
        "Longitude": -122.4194,
        "Battery (%)": 78,
        "Temperature (°C)": 45.3,
        "Anomaly Detected": "None",
        "Last Sync": datetime.now() - timedelta(minutes=5),
        "Image": "https://via.placeholder.com/150"
    },
    {
        "Robot ID": "ROBOT-2",
        "Location": "Tank Yard",
        "Latitude": 34.0522,
        "Longitude": -118.2437,
        "Battery (%)": 64,
        "Temperature (°C)": 55.7,
        "Anomaly Detected": "Leak",
        "Last Sync": datetime.now() - timedelta(minutes=8),
        "Image": "https://placekitten.com/150/150"
    },
    {
        "Robot ID": "ROBOT-3",
        "Location": "Substation",
        "Latitude": 40.7128,
        "Longitude": -74.0060,
        "Battery (%)": 92,
        "Temperature (°C)": 37.8,
        "Anomaly Detected": "None",
        "Last Sync": datetime.now() - timedelta(minutes=2),
        "Image": "https://via.placeholder.com/150"
    },
    {
        "Robot ID": "ROBOT-4",
        "Location": "Offshore Rig",
        "Latitude": 29.7604,
        "Longitude": -95.3698,
        "Battery (%)": 50,
        "Temperature (°C)": 65.2,
        "Anomaly Detected": "Corrosion",
        "Last Sync": datetime.now() - timedelta(minutes=6),
        "Image": "https://placekitten.com/150/150"
    },
    {
        "Robot ID": "ROBOT-5",
        "Location": "Plant A",
        "Latitude": 37.7750,
        "Longitude": -122.4195,
        "Battery (%)": 85,
        "Temperature (°C)": 42.1,
        "Anomaly Detected": "Overpressure",
        "Last Sync": datetime.now() - timedelta(minutes=3),
        "Image": "https://via.placeholder.com/150"
    }
]

robot_df = pd.DataFrame(data)
st.dataframe(robot_df.drop(columns=["Latitude", "Longitude", "Image"]), use_container_width=True)

# Filter by anomaly
anomaly_filter = st.selectbox("Filter by Anomaly", ["All"] + sorted(robot_df["Anomaly Detected"].unique()))
filtered_df = robot_df if anomaly_filter == "All" else robot_df[robot_df["Anomaly Detected"] == anomaly_filter]
st.write(f"Filtered to {len(filtered_df)} robots")

# Summary
st.subheader("🔍 Summary Statistics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Robots", len(robot_df))
col2.metric("With Anomalies", sum(robot_df["Anomaly Detected"] != "None"))
col3.metric("Avg Battery %", f"{robot_df['Battery (%)'].mean():.1f}%")

# Map View
st.subheader("🌍 Robot Location Map")
m = folium.Map(location=[37.7749, -122.4194], zoom_start=4)
for _, row in filtered_df.iterrows():
    color = anomaly_color.get(row['Anomaly Detected'], "gray")
    popup_html = f"""
    <b>{row['Robot ID']}</b><br>
    Location: {row['Location']}<br>
    Temp: {row['Temperature (°C)']} °C<br>
    Battery: {row['Battery (%)']}%<br>
    Anomaly: {row['Anomaly Detected']}<br>
    <img src='{row['Image']}' width='100'>
    """
    folium.Marker(
        location=[row["Latitude"], row["Longitude"]],
        popup=popup_html,
        icon=folium.Icon(color=color)
    ).add_to(m)

st_folium(m, width=1000, height=500)

# Alert Section
st.subheader("🚨 Active Alerts")
alerts_df = robot_df[robot_df["Anomaly Detected"] != "None"]
if alerts_df.empty:
    st.success("No active anomalies detected.")
else:
    for _, alert in alerts_df.iterrows():
        color = anomaly_color.get(alert['Anomaly Detected'], "gray")
        alert_msg = f"{alert['Robot ID']} at {alert['Location']} reports: {alert['Anomaly Detected']} (Temp: {alert['Temperature (°C)']}°C)"
        if color == "red":
            st.error(alert_msg)
        elif color == "orange":
            st.warning(alert_msg)
        else:
            st.info(alert_msg)

# Robot video feeds (grid view sorted by severity)
st.subheader("🎥 Robot Camera Views (Inspection Feeds)")
video_url = "https://samplelib.com/lib/preview/mp4/sample-5s.mp4"
sorted_data = sorted(data, key=lambda x: anomaly_severity.get(x['Anomaly Detected'], 0), reverse=True)
cols = st.columns(5)
for i, (col, robot) in enumerate(zip(cols, sorted_data)):
    with col:
        st.markdown(f"**{robot['Robot ID']}**")
        st.video(video_url)
        icon = anomaly_icon.get(robot['Anomaly Detected'], "❔")
        color = anomaly_color.get(robot['Anomaly Detected'], "gray")
        st.markdown(f"<div style='background-color:{color}; padding:4px; border-radius:5px; color:white; text-align:center;'>"
                    f"{icon} Last synced: {robot['Last Sync'].strftime('%Y-%m-%d %H:%M:%S')}<br>Status: {robot['Anomaly Detected']}"
                    f"</div>", unsafe_allow_html=True)

