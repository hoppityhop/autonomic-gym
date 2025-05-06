import random
import time
import statistics
from collections import deque
from pandas import DataFrame
import matplotlib.pyplot as plt


class Human:
    def __init__(self, height, weight, age, one_rm):
        self.height = height
        self.weight = weight
        self.age = age
        self.one_rm = one_rm


class WeightMachine:
    def __init__(self, equipment_id, weight_lb, human, window_size=3):
        self.equipment_id = equipment_id
        self.status = "idle"
        self.human = human
        self.weight_lb = weight_lb
        self.window_size = window_size
        self.rom_window = deque(maxlen=window_size)
        self.speed_window = deque(maxlen=window_size)
        self.completed_reps = 0
        self.df = DataFrame(
            columns=["weight_lb", "completed_reps", "rep_speed_sec", "rep_consistency", "range_of_motion_percent",
                     "range_of_motion_stability"])
        self.data = {"weight_lb": weight_lb, "completed_reps": 0, "rep_speed_sec": 2.0, "rep_consistency": 0.1,
                     "range_of_motion_percent": 100, "range_of_motion_stability": 0.0}

    def calculate_stability_metrics(self):
        if len(self.rom_window) >= 2:
            self.data["range_of_motion_stability"] = statistics.stdev(self.rom_window)
        if len(self.speed_window) >= 2:
            self.data["rep_consistency"] = statistics.stdev(self.speed_window)

    def calculate_max_reps(self):
        percentage_of_1rm = self.weight_lb / self.human.one_rm
        if percentage_of_1rm >= 0.85:
            return random.randint(5, 7)  # Range for 85% and above
        elif percentage_of_1rm >= 0.70:
            return random.randint(12, 14)  # Range for 70% to 85%
        else:
            return random.randint(18, 22)  # Range for below 70%

    def generate_rep_data(self, elapsed_time, total_duration):
        fatigue_progress = (elapsed_time / total_duration) * 2
        base_rom = random.uniform(85, 100)
        rom_decrement = fatigue_progress * random.uniform(0.8, 2.0)
        current_rom = max(60, base_rom - rom_decrement)


        max_reps = self.calculate_max_reps()
        rep_speed_sec = random.uniform(1.5, 3.5) + fatigue_progress * random.uniform(0.1, 1.0)
        rep_speed_sec *= (1 + (self.human.age / 100))  # Older age increases rep speed
        rep_speed_sec *= (1 + (self.weight_lb / self.human.one_rm))  # Higher percentage of 1RM decreases rep speed

        # rep_speed_sec = random.uniform(1.5, 3.5) + fatigue_progress * random.uniform(0.1, 1.0)

        return current_rom, rep_speed_sec, max_reps

    def simulate_usage(self, duration_seconds=80):
        self.status = "active"
        elapsed_time = 0

        print(f"Starting simulation for {duration_seconds} seconds...")
        while elapsed_time < duration_seconds:
            current_rom, rep_speed_sec, max_reps = self.generate_rep_data(elapsed_time, duration_seconds)

            if self.completed_reps >= max_reps:
                print("Maximum repetitions reached. Ending simulation.")
                break

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

        # Code below uses actual clock time for simulation demonstration  # self.status = "active"  # start_time = time.time()  # elapsed_time = 0  #  # print(f"Starting simulation for {duration_seconds} seconds...")  #  # while elapsed_time < duration_seconds:  #     current_rom, rep_speed_sec = self.generate_rep_data(elapsed_time, duration_seconds)  #  #     self.rom_window.append(current_rom)  #     self.speed_window.append(rep_speed_sec)  #     self.calculate_stability_metrics()  #     self.completed_reps += 1  #  #     self.data.update({"completed_reps": self.completed_reps, "range_of_motion_percent": current_rom,  #                       "rep_speed_sec": rep_speed_sec, })  #  #     print(f"Time: {elapsed_time:.1f}s, Rep {self.data['completed_reps']}: "  #           f"ROM={current_rom:.2f}%, Speed={rep_speed_sec:.2f}s")  #     print(f"Current data: {self.data}\n")  #     self.record_metrics()  #  #     time.sleep(rep_speed_sec)  #     elapsed_time = time.time() - start_time  #  # print(f"Workout completed in {elapsed_time:.1f} seconds. Final data:", self.data)  # self.status = "idle"  # self.plot_metrics()

    def record_metrics(self):
        self.df = self.df._append(self.data, ignore_index=True)

    def plot_metrics(self):
        self.df.plot(x='completed_reps', y=['range_of_motion_percent', 'rep_speed_sec'], subplots=True, layout=(2, 1),
                     figsize=(10, 6))
        plt.show()


# Example Usage:
if __name__ == "__main__":
    person0 = Human(height=70, weight=180, age=30, one_rm=31.5)
    person1 = Human(70, 180, 25, 300)
    person2 = Human(65, 150, 30, 250)
    weight_machine0 = WeightMachine("W01", 25, person0, 5)
    weight_machine1 = WeightMachine("W02", 250, person1, 5)
    weight_machine2 = WeightMachine("W03", 222, person2, 5)

    weight_machine0.simulate_usage()
    weight_machine1.simulate_usage()
    weight_machine2.simulate_usage()
