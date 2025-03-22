import random
import time
import statistics
from collections import deque
from pandas import DataFrame
import matplotlib.pyplot as plt


class WeightMachine:
    def __init__(self, equipment_id, window_size=3):
        self.equipment_id = equipment_id
        self.status = "idle"
        self.window_size = window_size
        self.rom_window = deque(maxlen=window_size)
        self.speed_window = deque(maxlen=window_size)
        self.completed_reps = 0
        self.df = DataFrame( columns=["weight_lb", "completed_reps", "rep_speed_sec", "rep_consistency",
                          "range_of_motion_percent", "range_of_motion_stability"])
        self.data = {"weight_lb": 50, "completed_reps": 0, "rep_speed_sec": 2.0, "rep_consistency": 0.1,
                     "range_of_motion_percent": 100, "range_of_motion_stability": 0.0}

    def calculate_stability_metrics(self):
        if len(self.rom_window) >= 2:
            self.data["range_of_motion_stability"] = statistics.stdev(self.rom_window)
        if len(self.speed_window) >= 2:
            self.data["rep_consistency"] = statistics.stdev(self.speed_window)

    def generate_rep_data(self, elapsed_time, total_duration):
        fatigue_progress = (elapsed_time / total_duration) * 2
        base_rom = random.uniform(85, 100)
        rom_decrement = fatigue_progress * random.uniform(0.8, 2.0)
        current_rom = max(60, base_rom - rom_decrement)
        rep_speed_sec = random.uniform(1.5, 3.5) + fatigue_progress * random.uniform(0.1, 1.0)

        return current_rom, rep_speed_sec

    def simulate_usage(self, duration_seconds=80):
        self.status = "active"
        elapsed_time = 0

        print(f"Starting simulation for {duration_seconds} seconds...")
        while elapsed_time < duration_seconds:
            current_rom, rep_speed_sec = self.generate_rep_data(elapsed_time, duration_seconds)

            self.rom_window.append(current_rom)
            self.speed_window.append(rep_speed_sec)
            self.calculate_stability_metrics()
            self.completed_reps += 1

            self.data.update({"completed_reps": self.completed_reps, "range_of_motion_percent": current_rom,
                              "rep_speed_sec": rep_speed_sec, })

            print(f"Time: {elapsed_time:.1f}s, Rep {self.data['completed_reps']}: "
                  f"ROM={current_rom:.2f}%, Speed={rep_speed_sec:.2f}s")
            print(f"Current data: {self.data}\n")
            self.record_metrics()

            elapsed_time += rep_speed_sec  # Increment elapsed time by the duration of the current rep

        print(f"Workout completed in {elapsed_time:.1f} seconds. Final data:", self.data)
        self.status = "idle"
        self.plot_metrics()






        # Code below uses actual clock time for simulation demonstration
        # self.status = "active"
        # start_time = time.time()
        # elapsed_time = 0
        #
        # print(f"Starting simulation for {duration_seconds} seconds...")
        #
        # while elapsed_time < duration_seconds:
        #     current_rom, rep_speed_sec = self.generate_rep_data(elapsed_time, duration_seconds)
        #
        #     self.rom_window.append(current_rom)
        #     self.speed_window.append(rep_speed_sec)
        #     self.calculate_stability_metrics()
        #     self.completed_reps += 1
        #
        #     self.data.update({"completed_reps": self.completed_reps, "range_of_motion_percent": current_rom,
        #                       "rep_speed_sec": rep_speed_sec, })
        #
        #     print(f"Time: {elapsed_time:.1f}s, Rep {self.data['completed_reps']}: "
        #           f"ROM={current_rom:.2f}%, Speed={rep_speed_sec:.2f}s")
        #     print(f"Current data: {self.data}\n")
        #     self.record_metrics()
        #
        #     time.sleep(rep_speed_sec)
        #     elapsed_time = time.time() - start_time
        #
        # print(f"Workout completed in {elapsed_time:.1f} seconds. Final data:", self.data)
        # self.status = "idle"
        # self.plot_metrics()

    def record_metrics(self):
        self.df = self.df._append(self.data, ignore_index=True)

    def plot_metrics(self):
        self.df.plot(x='completed_reps', y=['range_of_motion_percent', 'rep_speed_sec'], subplots=True, layout=(2, 1), figsize=(10, 6))
        plt.show()


# Example Usage:
if __name__ == "__main__":
    weight_machine = WeightMachine("W01", 5)
    weight_machine.simulate_usage()