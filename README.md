# Pomodoro-GUI-Application
The Pomodoro Technique is a time management method developed by Francesco Cirillo in the late 1980s. It encourages people to work with the time they have, rather than against it. The technique uses a timer to break work into intervals, traditionally 25 minutes in length, separated by short breaks. This method enhances focus and productivity, reducing mental fatigue.

## Overview

This program utilizes the Python module Tkinter to create a user-friendly graphical interface. The Pomodoro GUI Application is designed to help users manage their time effectively by following the Pomodoro Technique.

### Key Components
* Tkinter: The core library for building the GUI.
* Window: The main application window that hosts all components.
* Label: Displays the current timer status and prompts to the user.
* Button: Interactive elements to start and reset the timer.

### Features
* 25-Minute Work Sessions: The application prompts you to work for 25 minutes.
* 5-Minute Short Breaks: After each work session, enjoy a 5-minute break to recharge.
* 20-Minute Long Break: After completing four work sessions, you can take a longer break.
* Start Button: Click the "Start" button to begin your work session countdown.
* Automatic Transition: The timer automatically transitions from work sessions to breaks.
* Reset Button: You can reset the timer at any time to start over.

## How to Use

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yingliu1206/Pomodoro-GUI-Application.git
   cd Pomodoro-GUI-Application

2. **Running the Application**:
   ```bash
   python main.py

### Interface
<img width="542" alt="Screenshot 2024-10-02 at 10 03 53 PM" src="https://github.com/user-attachments/assets/44c8ca89-4605-4ba0-a64d-1bb28d1ab10b">

## Instructions
* Start the Timer: Click the "Start" button to begin your 25-minute work session.
* Work: Focus on your task for the entire 25 minutes.
* Short Break: After the session ends, take a 5-minute break. The timer will automatically start for the break.
* Repeat: After completing four work sessions, the application will prompt for a longer break.
* Reset: If you need to pause or restart, simply click the "Reset" button.

## Acknowledgments
- [100 Days of Code: The Complete Python Pro Bootcamp - Udemy](https://www.udemy.com/course/100-days-of-code) for the inspiration and guidance.
