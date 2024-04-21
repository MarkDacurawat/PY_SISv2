# Student Information System (SIS)

## Overview

This project is a Student Information System (SIS) developed using Python and the Tkinter library for the graphical user interface. It serves as a tool for managing student records within an educational institution, providing functionalities such as user authentication, student registration, dashboard overview, and more.

## Requirements

- Python 3.x
- Tkinter
- Customtkinter
- SQLite3
- PIL (Python Imaging Library)

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/MarkDacurawat/PY_SISv2.git SISv2
   ```

2. Navigate to the project directory:

   ```bash
   cd SISv2
   ```

3. Install required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Download And Install SQLite3
   [Download SQLite Precompiled Binary](https://www.sqlite.org/2024/sqlite-tools-win-x64-3450300.zip)

## Usage

1. Run the main script to launch the application:

   ```bash
   python main.py
   ```

2. Upon launching the application, you will be presented with the user type selection page where you can choose between 'Student' and 'Admin' options.

3. Depending on the chosen user type, different functionalities will be available:

   - **Student**: Allows students to register their information.
   - **Admin**: Requires authentication and provides access to dashboard features such as adding new admins, adding students, finding students, and viewing statistics.

4. Follow the on-screen instructions to navigate through the application and utilize its features.

## Features

- **User Authentication**: Admins can log in securely using their username and password.
- **Student Registration**: Students can register with their personal information, including LRN, name, age, birthday, address, phone number, gender, year level, course, and semester.
- **Dashboard Overview**: Provides admins with statistics on the total number of students, admins, and students categorized by course.
- **Form Validation**: Validates user input for various fields such as LRN, name, age, birthday, address, phone number, etc.
- **Responsive GUI**: Designed with Tkinter to create a user-friendly and responsive graphical interface.

## Database Structure

The SQLite database used in this project consists of two tables:

### Students

- `id` INTEGER PRIMARY KEY
- `lrn` VARCHAR(10) UNIQUE
- `first_name` VARCHAR(50)
- `middle_name` VARCHAR(50)
- `last_name` VARCHAR(50)
- `age` INTEGER
- `birthday` VARCHAR(10)
- `address` VARCHAR(255)
- `phone_number` VARCHAR(15)
- `gender` TEXT CHECK (gender IN ('Male', 'Female', 'Other'))
- `year_level` INTEGER
- `course` VARCHAR(25)
- `semester` VARCHAR(10)

### Admin

- `id` INTEGER PRIMARY KEY
- `username` VARCHAR(50) UNIQUE
- `password` VARCHAR(255)

## Contributors

- Mark Dacurawat (@MarkDacurawat)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
