class AlertManager:
    def __init__(self, threshold):
        self.threshold = threshold
        self.consecutive_count = 0

    def check_alert(self, temp):
        if temp > self.threshold:
            self.consecutive_count += 1
            if self.consecutive_count >= 2:
                print(f"ALERT! Temperature exceeded {self.threshold}°C for two consecutive updates.")
        else:
            self.consecutive_count = 0
