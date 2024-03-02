import time

detections = [
    {
        "message": "Possible ICMP Flood Detected",
        "lastDetection": None,
        "isDetected": False,
        "fileName": "icmp",
        "flag": "FLAG(ICMP_FLOOD)",
    },
    {
        "message": "Possible HTTP POST Flood Detected",
        "lastDetection": None,
        "isDetected": False,
        "fileName": "httppost",
        "flag": "FLAG(HTTP_POST_FLOOD)",
    },
    {
        "message": "Possible ReDoS Detected",
        "lastDetection": None,
        "isDetected": False,
        "fileName": "redos",
        "flag": "FLAG(ReDoS)",
    },
    {
        "message": "Possible Slowloris Detected",
        "lastDetection": None,
        "isDetected": False,
        "fileName": "slowloris",
        "flag": "FLAG(Slowloris)",
    },
    {
        "message": "Possible SYN Flood Detected",
        "lastDetection": None,
        "isDetected": False,
        "fileName": "synflood",
        "flag": "FLAG(SYNflood)",
    }
]

log_file = "/var/log/suricata/fast.log"
flags_path = "/var/www/htmlflags/"
last_checked_line = 0

def check_for_detections():
    global last_checked_line
    with open(log_file, "r") as file:
        lines = file.readlines()
        for i in range(last_checked_line, len(lines)):
            for j, detection in enumerate(detections):
                if (
                    detection["message"] in lines[i] and 
                    (j == 0 or detections[j - 1]["isDetected"]) and 
                    (detection["lastDetection"] is None or (time.time() - detection["lastDetection"]) > 30)
                ):
                    detection["lastDetection"] = time.time()
                    detection["isDetected"] = True
                    create_flag(detection)
        last_checked_line = len(lines)

def create_flag(detection):
    with open(flags_path + detection["fileName"] + ".txt", "w") as file:
        file.write(detection["flag"])
    print("Flag Created: " + detection["fileName"] + ".txt")

def main():
    try:
        while True:
            check_for_detections()
            time.sleep(5)
    except KeyboardInterrupt:
        print("[*] Stopping Scenario Manager [*]")

if __name__ == "__main__":
    print("[*] Starting Scenario Manager [*]")
    main()

