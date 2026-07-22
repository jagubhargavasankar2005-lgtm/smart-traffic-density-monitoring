# 🚦 Smart Traffic Density Monitoring and Adaptive Traffic Signal Control

An AI-powered traffic monitoring system that uses **YOLOv8** and **OpenCV** to detect vehicles, estimate traffic density, and dynamically optimize traffic signal timings. The system improves traffic flow by allocating green signal duration based on real-time vehicle density.

---

## 📌 Features

- 🚗 Real-time vehicle detection using YOLOv8
- 📹 Traffic density monitoring from video input
- 🔢 Automatic vehicle counting
- 📊 Dynamic traffic density estimation
- 🚦 Adaptive traffic signal timing
- ⚡ Intelligent traffic management using computer vision

---

## 🛠️ Tech Stack

- Python
- OpenCV
- YOLOv8
- NumPy
- Computer Vision

---

## 📂 Repository Structure

```text
smart-traffic-density-monitoring/
│── original.py
│── README.md
│── LICENSE
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/jagubhargavasankar2005-lgtm/smart-traffic-density-monitoring.git
```

Navigate to the project directory:

```bash
cd smart-traffic-density-monitoring
```

Install the required dependencies:

```bash
pip install ultralytics opencv-python numpy streamlit
```

---

## ▶️ Run the Project

```bash
streamlit run original.py
```

---

## 🚦 Project Workflow

1. Load traffic video input.
2. Detect vehicles using YOLOv8.
3. Count vehicles in each frame.
4. Estimate traffic density.
5. Adjust traffic signal timing dynamically.
6. Display traffic statistics in real time.

---

## 📈 Advantages

- Reduces traffic congestion
- Minimizes vehicle waiting time
- Improves road efficiency
- Supports smart city applications
- Automated traffic monitoring

---

## ⚠️ Limitations

- Performance depends on camera quality.
- Weather conditions can affect detection accuracy.
- Real-time processing benefits from GPU acceleration.

---

## 🚀 Future Enhancements

- Emergency vehicle priority detection
- Accident detection
- Multi-intersection traffic management
- AI-based traffic prediction
- Integration with Smart City and IoT infrastructure

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Bhargava Sankar Jagu**

- GitHub: https://github.com/jagubhargavasankar2005-lgtm
- LinkedIn: https://www.linkedin.com/in/bhargava-sankar-jagu

---

⭐ If you found this project useful, consider giving it a star on GitHub.
