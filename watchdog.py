import time

"""
Index 0 = Detection message
Index 1 = Detection Status
Index 2 = File Name
Index 3 = Flag
"""
detections = [
    [
        "Possible NMAP Scan Detected",
        False,
        "nmap",
        "FLAG(NMAP)",
    ],
    [
        "Possible ICMP Flood Detected",
        False,
        "icmp",
        "FLAG(ICMP_FLOOD)",
    ],
    [
        "Possible HTTP POST Flood Detected",
        False,
        "httppost",
        "FLAG(HTTP_POST_FLOOD)",
    ],
    [
        "Possible ReDoS Detected",
        False,
        "redos",
        "FLAG(ReDoS)",
    ],
    [
        "Possible Slowloris Detected",
        False,
        "slowloris",
        "FLAG(Slowloris)",
    ],
    [
        "Possible Ping of Death Detected",
        False,
        "pingofdeath",
        "FLAG(Ping_of_Death)",
    ]
]

log_file = "/var/log/suricata/fast.log"
flags_path = "/var/www/html/flags/"

last_checked_line = 0

def check_for_detections():
    global last_checked_line
    with open(log_file, "r") as file:
        lines = file.readlines()
        for i in range(last_checked_line, len(lines)):
            for detection in detections:
                if detection[0] in lines[i] and detection[1] == False:
                    detection[1] = True
                    create_flag(detection)
        last_checked_line = len(lines)

def create_flag(detection):
    with open(flags_path + detection[2] + ".txt", "w") as file:
        file.write(detection[3])
    
    print("Flag Created: " + detection[2] + ".txt")


def main():
    check_for_detections()
    

while True:
    main()
    time.sleep(5)