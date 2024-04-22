**Log Analysis and Monitoring Script:**

This README provides an overview of the Log Analysis and Monitoring Script,including usage instructions,script details and author attribution. For further details on the script's implementation and usage, please refer to the provided Python script file.

**Objective:**
The objective of this script is to automate the analysis and monitoring of log files using Python scripting. By continuously monitoring specified log files for new entries, it provides real-time tracking and analysis functionalities.

**Script Overview:**
The provided Python script is designed to monitor a specified log file for new entries in real-time. It continuously checks for new lines appended to the log file and displays them on the console. Additionally, it logs the new entries to a separate log file named "log_monitor_Script.log".

**PreRequistes:**
1.Ensure you have Python installed on your system.

**Execution:**
1.Copy the provided script into a Python file (e.g., Log-Analysis_Script.py).
2.Run the script using the command (cd path/to/directory 
  python Log-Analysis_Script.py)
3.The script will continuously log messages at different levels and can be terminated using Ctrl+C.

**Script Details:**

• Logging Configuration:
The script configures the logging module to log messages to the file "log_monitor_Script.log" at the INFO level. The log messages include the timestamp, log level, and message content.

• Log Message Formats:
Defines message formats for different log levels: INFO, DEBUG, and ERROR.

• Signal Handler:
Defines a signal handler function signal_handler to handle the Ctrl+C signal (SIGINT). When Ctrl+C is pressed, the script gracefully exits and logs a message indicating that the monitoring process has been interrupted.

• Monitoring Function:
Implements a function monitor_log(log_file) to monitor the specified log file for new entries. Displays each new log entry on the console and logs it to the log file.
Handles the case where the specified log file is not found, logging an error message and printing an error to the console.

• Main Function:
Defines the main function main() which serves as the entry point of the script.
Prints a message indicating the start of log file monitoring and logs the same message.
Executes a continuous loop to log messages at random log levels with a short interval between each log.

• Script Execution:
The script checks if it is being executed as the main program (__name__ == "__main__").
If so, it invokes the main() function to start monitoring the log file.

• Exception Handling:
Handles keyboard interrupt (Ctrl+C) to gracefully exit the script.

**Author:**
Dharshini Sridharan
