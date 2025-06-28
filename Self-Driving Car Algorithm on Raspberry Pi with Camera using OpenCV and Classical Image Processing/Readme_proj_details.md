# Real-Time Image Analysis for Self-Driving Capabilities

A lightweight, rule-based self-driving simulation system built using **Python**, **OpenCV**, and a **Raspberry Pi 5**. This project showcases how classical computer vision techniques can be effectively used for lane detection, obstacle avoidance, and emergency stopping—without relying on machine learning models.

## Project Overview

This project implements a pseudo real-time self-driving algorithm that analyzes each video frame captured by a **Pi Camera** and determines the appropriate movement command: **go straight**, **turn left/right**, or **stop**. 

### Key Features

- **Lane Detection:**  
  Uses Canny Edge Detection and Hough Line Transform on the bottom region of the frame.

- **Obstacle Detection:**  
  Identifies lateral objects using contour analysis and clustering (K-means) on the middle region.

- **Emergency Stop Logic:**  
  Stops the car if an immediate obstacle is detected in the top-center region.

- **Real-Time Feedback:**  
  Processes video at ~25 FPS on Raspberry Pi 5.

---

## Technology Stack

- **Language:** Python 3  
- **Libraries:** OpenCV, NumPy, scikit-learn  
- **Hardware:** Raspberry Pi 5, Pi Camera  
- **Tools:** Arduino IDE (for potential expansion)

---

## System Design

The input frame is divided into three modular regions:

+------------------+
| Top Center (Stop) |
+------------------+
| Middle (Obstacle) |
+------------------+
| Bottom (Lane) |
+------------------+


Each region is analyzed separately for its role in guiding the car’s decision-making.

---

## Directional Logic

- **Both lane lines detected:** Follow the average slope to go straight.
- **One lane line:** Extrapolate and follow.
- **Obstacle on left/right:** Turn opposite.
- **Obstacle in top-center:** Initiate stop.

---

## Getting Started

### Prerequisites
- Raspberry Pi 5 with Pi Camera installed
- Python 3 environment
- Required libraries:
 -> Picamera2 + Opencv
