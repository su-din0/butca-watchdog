# Watchdog script

This Python script is an „Intrusion Detection System“ (IDS) watchdog. It continuously monitors a log file for specific intrusion detection messages. When a detection message is found, a corresponding flag file is created.

## How it works

The script uses a list of detection messages to monitor the log file. Each detection is represented as a list with the following structure:

```python
[
    "Detection message",
    Detection status,
    "File name",
    "Flag"
]
```

The "Detection message" is the message that the script is looking for in the log file.
The Detection status is a boolean that indicates whether the detection has been found. It's initially set to ```False``` and is set to ```True``` when the detection message is found in the log file.
The "File name" is the name of the flag file that will be created when the detection message is found.
The "Flag" is the content that will be written to the flag file.


The script continuously reads the log file line by line. When a line contains a detection message and the detection status is ```False```, the script sets the detection status to ```True``` and calls the ```create_flag``` function to create the flag file.

The create_flag function creates a file with the specified file name in a specified directory. The flag is written to the file.

The script keeps track of the last line that was checked in the log file to avoid checking the same lines multiple times.

## Usage

The script is designed to run continuously in the background. It checks the log file every 5 seconds.

To start the script, simply run it with Python:
```python
python3 watchdog.py
```

## Customization

You can customize the script by modifying the ```detections```, ```log_file```, and ```flags_path``` variables at the top of the script.

```detections``` is the list of detections that the script will look for. You can add, remove, or modify detections as needed.
```log_file``` is the path to the log file that the script will monitor. You can change this to the path of your log file.
```flags_path``` is the directory where the flag files will be created. You can change this to your desired directory.
