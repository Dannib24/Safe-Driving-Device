import tkinter as tk
from datetime import datetime

class SafeDrivingDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Safe Driving Device Dashboard")
        self.root.configure(bg="#111827")
        self.root.geometry("1024x600")

        self.scenarios = [
            {
                "event": "NORMAL DRIVING",
                "risk": "LOW",
                "speed": "35 mph",
                "distance": "180 cm",
                "deceleration": "1.2 m/s²",
                "gps": "41.6105, -87.7210",
                "message": "Normal driving behavior detected.",
                "color": "#22c55e"
            },
            {
                "event": "HARD BRAKING",
                "risk": "MEDIUM",
                "speed": "28 mph",
                "distance": "115 cm",
                "deceleration": "3.6 m/s²",
                "gps": "41.6112, -87.7218",
                "message": "Hard braking event detected.",
                "color": "#f59e0b"
            },
            {
                "event": "EMERGENCY BRAKING",
                "risk": "HIGH",
                "speed": "15 mph",
                "distance": "45 cm",
                "deceleration": "6.1 m/s²",
                "gps": "41.6120, -87.7226",
                "message": "Emergency braking condition detected.",
                "color": "#ef4444"
            },
            {
                "event": "RECKLESS BRAKING",
                "risk": "HIGH",
                "speed": "12 mph",
                "distance": "85 cm",
                "deceleration": "4.3 m/s²",
                "gps": "41.6131, -87.7235",
                "message": "Repeated aggressive braking pattern detected.",
                "color": "#a855f7"
            }
        ]

        self.index = 0

        self.title_label = tk.Label(
            root,
            text="SAFE DRIVING DEVICE",
            font=("Arial", 34, "bold"),
            fg="white",
            bg="#111827"
        )
        self.title_label.pack(pady=20)

        self.event_label = tk.Label(
            root,
            text="",
            font=("Arial", 38, "bold"),
            fg="white",
            bg="#111827"
        )
        self.event_label.pack(pady=10)

        self.info_label = tk.Label(
            root,
            text="",
            font=("Arial", 22),
            fg="white",
            bg="#111827",
            justify="left"
        )
        self.info_label.pack(pady=20)

        self.message_label = tk.Label(
            root,
            text="",
            font=("Arial", 22, "bold"),
            fg="white",
            bg="#111827",
            wraplength=900
        )
        self.message_label.pack(pady=15)

        self.footer_label = tk.Label(
            root,
            text="",
            font=("Arial", 16),
            fg="#d1d5db",
            bg="#111827"
        )
        self.footer_label.pack(side="bottom", pady=20)

        self.root.bind("<Escape>", lambda event: self.root.destroy())

        self.update_dashboard()

    def update_dashboard(self):
        data = self.scenarios[self.index]

        self.event_label.config(
            text=data["event"],
            fg=data["color"]
        )

        self.info_label.config(
            text=(
                f"Risk Level: {data['risk']}\n"
                f"Speed: {data['speed']}\n"
                f"Obstacle Distance: {data['distance']}\n"
                f"Deceleration: {data['deceleration']}\n"
                f"GPS: {data['gps']}"
            )
        )

        self.message_label.config(
            text=data["message"],
            fg=data["color"]
        )

        self.footer_label.config(
            text=f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}   |   CSV Logging: Active"
        )

        self.index = (self.index + 1) % len(self.scenarios)
        self.root.after(4000, self.update_dashboard)


if __name__ == "__main__":
    root = tk.Tk()
    app = SafeDrivingDashboard(root)
    root.mainloop()