import logging
import time
import signal
import sys

# Configure logging
logging.basicConfig(filename='log_monitor_Script.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

# Function to handle Ctrl+C
def signal_handler(sig, frame):
    print('\nMonitoring interrupted. Exiting.')
    logging.info('Monitoring interrupted. Exiting.')
    sys.exit(0)

# Register the signal handler for Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

# Function to monitor log file for new entries
def monitor_log(log_file):
    try:
        with open(log_file, 'r') as file:
            # Move to the end of the file
            file.seek(0, 2)
            while True:
                # Read new lines continuously
                line = file.readline()
                if line:
                    print(line.strip())  # Display the new log entry
                    logging.info(line.strip())  # Log the entry
                else:
                    time.sleep(0.1)
    except FileNotFoundError:
        print(f"Error: Log file '{log_file}' not found.")
        logging.error(f"Log file '{log_file}' not found.")

# Main function
def main():
    # Specify the log file to monitor
    log_file = "User.log"

    print(f"Monitoring log file '{log_file}'...")
    logging.info(f"Monitoring log file '{log_file}'...")
    monitor_log(log_file)

if __name__ == "__main__":
    main()
