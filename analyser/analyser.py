import serial

def parse_log(log):
    try:
        return dict(item.split(':') for item in log.strip().split(','))
    except:
        return None


def diagnose(data):
    if not data:
        return "Invalid log format"

    state = data.get("STATE", "UNKNOWN")

    if state == "TEMP_HIGH":
        return "Overheating → Check environment"

    elif state == "NOISE_ALERT":
        return "Noise spike → Possible disturbance"

    elif state == "TILT_ALERT":
        return "Instability → Check placement"

    elif state == "NORMAL":
        return "System stable"

    return "Unknown state"


# 🔴 CHANGE THIS PORT
ser = serial.Serial('COM4', 9600)  

print("Listening to real-time data...\n")

while True:
    try:
        log = ser.readline().decode().strip()
        if log:
            data = parse_log(log)
            result = diagnose(data)
            print(f"{log} => {result}")
    except Exception as e:
        print("Error:", e)