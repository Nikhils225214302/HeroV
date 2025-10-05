import psutil
import time

def monitor_cpu(threshold=80):
    print("Starting to monitor CPU usage...")
    print("Press Ctrl+C to stop at any time.\n")
    
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            
            if cpu_usage > threshold:
                print(f"Alert! CPU usage is high: {cpu_usage}%")
            else:
                print(f"Current CPU usage: {cpu_usage}%")
            
            time.sleep(1)
    
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user. Exiting...")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    monitor_cpu(80)
