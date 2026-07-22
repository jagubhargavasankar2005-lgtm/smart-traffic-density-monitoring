import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO
import time

st.set_page_config(layout="wide")

st.markdown(
    "<h1 style='text-align:center;'>🚦 Smart Traffic Monitoring </h1>",
    unsafe_allow_html=True
)

# Load YOLO model
model = YOLO("yolov8n.pt")

# Video files
video_files = ["road1.mp4", "road2.mp4", "road3.mp4", "road4.mp4"]
caps = [cv2.VideoCapture(v) for v in video_files]

# Counters
vehicle_counts = [0, 0, 0, 0]
counted_ids = [set(), set(), set(), set()]

# Layout
cols = st.columns(2)
cols2 = st.columns(2)
analysis_col, alert_col = st.columns(2)

frame_slots = [
    cols[0].empty(), cols[1].empty(),
    cols2[0].empty(), cols2[1].empty()
]

analysis_placeholder = analysis_col.empty()
alert_placeholder = alert_col.empty()

start = st.button("▶ Start Monitoring")

# Vehicle classes
VEHICLE_CLASSES = [2, 3, 5, 7]

if start:
    while True:
        frames = []

        for i, cap in enumerate(caps):
            ret, frame = cap.read()

            if not ret:
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                ret, frame = cap.read()

            frame = cv2.resize(frame, (640, 360))

            results = model(frame)[0]

            line_y = 200
            cv2.line(frame, (0, line_y), (640, line_y), (0,0,255), 2)

            for box in results.boxes:
                cls = int(box.cls[0])

                if cls in VEHICLE_CLASSES:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    cx = (x1 + x2) // 2
                    cy = (y1 + y2) // 2

                    cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)
                    cv2.circle(frame, (cx,cy), 4, (0,0,255), -1)

                    # Unique ID using position
                    obj_id = (cx, cy)

                    if line_y - 5 < cy < line_y + 5:
                        if obj_id not in counted_ids[i]:
                            vehicle_counts[i] += 1
                            counted_ids[i].add(obj_id)

            frames.append(frame)

        total = sum(vehicle_counts)

        # Signal timing
        if total == 0:
            times = [30, 30, 30, 30]
        else:
            times = [int((v / total) * 120) for v in vehicle_counts]

        max_index = vehicle_counts.index(max(vehicle_counts))

        # Display frames
        for i in range(4):
            frame = frames[i]

            if i == max_index:
                signal = "🟢 GREEN"
                color = (0,255,0)
            else:
                signal = "🔴 RED"
                color = (0,0,255)

            cv2.putText(frame, f"Road {i+1}", (10,30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

            cv2.putText(frame, f"Vehicles: {vehicle_counts[i]}",
                        (10,300),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)

            cv2.putText(frame, f"Time: {times[i]} sec",
                        (10,330),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)

            cv2.putText(frame, f"{signal}",
                        (400,330),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

            frame_slots[i].image(frame, channels="BGR")

        # Analysis
        with analysis_placeholder.container():
            st.markdown("### 📊 Traffic Analysis")
            st.bar_chart(vehicle_counts)
            st.write(f"**Total Vehicles:** {total}")
            st.write(f"**High Traffic Road:** Road {max_index+1}")

        # Alert
        with alert_placeholder.container():
            st.markdown("### ⚠️ Traffic Alert")
            if max(vehicle_counts) > 20:
                st.error(f"🚨 Heavy Traffic on Road {max_index+1}")
            else:
                st.success("✅ Traffic Normal")

        time.sleep(0.5)
