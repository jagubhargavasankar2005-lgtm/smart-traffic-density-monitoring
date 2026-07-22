# 🚦 Smart Traffic Density Monitoring and Adaptive Traffic Signal Control

An AI-powered traffic monitoring system that uses **YOLOv8** and **OpenCV** to detect vehicles, estimate traffic density, and dynamically optimize traffic signal timings. The project aims to reduce traffic congestion by allocating green signal duration based on real-time vehicle density.

---

## 📌 Features

- 🚗 Real-time vehicle detection using YOLOv8
- 📹 Traffic monitoring from video streams
- 🔢 Automatic vehicle counting
- 📊 Traffic density estimation
- 🚦 Adaptive traffic signal timing based on vehicle density
- ⚡ Computer vision-based intelligent traffic management

---

## 🛠️ Tech Stack

- **Python**
- **OpenCV**
- **YOLOv8**
- **NumPy**
- **Computer Vision**

---

## 📂 Project Structure

```text
smart-traffic-density-monitoring/
│── original.py
│── yolov8n.pt
│── road1.mp4
│── road2.mp4
│── road3.mp4
│── road4.mp4
│── README.md
│── LICENSE
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/jagubhargavasankar2005-lgtm/smart-traffic-density-monitoring.git
```

```bash
cd smart-traffic-density-monitoring
```

### Install dependencies

```bash
pip install ultralytics opencv-python numpy
```

---

## ▶️ Run the Project

```bash
python original.py
```

---

## 🚦 Workflow

1. Load traffic video.
2. Detect vehicles using YOLOv8.
3. Count detected vehicles.
4. Estimate traffic density.
5. Allocate signal timing dynamically.
6. Display processed traffic information.

---

## 📈 Advantages

- Reduces traffic congestion
- Minimizes waiting time
- Improves traffic flow
- Supports smart city initiatives
- Fully automated traffic monitoring

---

## ⚠️ Limitations

- Performance depends on camera quality.
- Weather conditions may affect detection accuracy.
- Requires GPU for faster inference.

---

## 🚀 Future Enhancements

- Emergency vehicle priority detection
- Accident detection
- Multi-intersection traffic control
- Traffic prediction using AI
- Integration with IoT and Smart City infrastructure

---

## 📸 Demo

> Add screenshots or GIFs of your project here.

Example:

```
images/output1.png
images/output2.png
```

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Bhargava Sankar Jagu**

- GitHub: https://github.com/jagubhargavasankar2005-lgtm
- LinkedIn: https://www.linkedin.com/in/bhargava-sankar-jagu

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.
