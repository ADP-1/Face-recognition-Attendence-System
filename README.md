# Face Recognition Attendance System

![Project Banner](path/to/banner/image.png)

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Database Structure](#database-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## :wave: Introduction

The Face Recognition Attendance System is an advanced, automated solution designed to streamline the process of tracking attendance in educational institutions or workplaces. By leveraging state-of-the-art facial recognition technology, this system provides a contactless, efficient, and accurate method of recording attendance.

## :star: Features

- Real-time face detection and recognition using OpenCV and face_recognition library
- Automated attendance marking with timestamp recording
- Firebase integration for secure data storage and retrieval
- User-friendly graphical interface with custom background and mode displays
- Multi-threaded operations for improved performance
- Configurable attendance rules (e.g., minimum time between markings)
- Detailed logging and debugging information
- Support for multiple students with individual profiles

## :gear: Technologies Used

- Python 3.x
- OpenCV (cv2)
- face_recognition library
- Firebase Admin SDK
- NumPy
- cvzone
- Threading
- Pickle for data serialization

## :rocket: Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/face-recognition-attendance-system.git
   cd face-recognition-attendance-system
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up Firebase:
   - Create a Firebase project and download the `serviceAccountKey.json`
   - Place the `serviceAccountKey.json` in the project root directory
   - Update the Firebase configuration in the Python scripts with your project details

## :computer: Usage

1. Add student data to the Firebase database:
   ```
   python AddDatatoDatabase.py
   ```

2. Generate face encodings for registered students:
   ```
   python EncodeGenerator.py
   ```

3. Run the main attendance system:
   ```
   python main.py
   ```

4. The system will start the camera and begin recognizing faces. Attendance will be marked automatically for recognized students.

5. Press 'q' to quit the application.

## :wrench: Configuration

You can configure various aspects of the system by modifying the following files:

- `main.py`: Adjust frame processing frequency, attendance rules, and UI layout
- `EncodeGenerator.py`: Customize the encoding process for face recognition
- `AddDatatoDatabase.py`: Modify the structure of student data in the database

## :file_folder: Database Structure

The Firebase Realtime Database follows this structure:

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

No license till now 

## Acknowledgements

- [face_recognition library](https://github.com/ageitgey/face_recognition)
- [OpenCV](https://opencv.org/)
- [Firebase](https://firebase.google.com/)
- [cvzone](https://github.com/cvzone/cvzone)

## Last Updated
- [21/10/2024]
