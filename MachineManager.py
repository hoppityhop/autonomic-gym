import random
import numpy as np
from WeightMachine import Human, WeightMachine

class EpsilonGreedyBandit:
    def __init__(self, epsilon=0.1):
        self.epsilon = epsilon
        self.actions = [-5, 0, 5]  # decrease by 5 lbs, maintain, increase by 5 lbs
        self.action_values = {action: [] for action in self.actions}

    def select_action(self, context):
        if random.random() < self.epsilon:
            action = random.choice(self.actions)
        else:
            average_rewards = {a: np.mean(self.action_values[a]) if self.action_values[a] else 0 for a in self.actions}
            action = max(average_rewards, key=average_rewards.get)

        return action

    def update_values(self, action, reward):
        self.action_values[action].append(reward)


class WorkoutManager:
    def __init__(self, human, ideal_hr=140, ideal_speed=2.0, ideal_stability=5.0):
        self.human = human
        self.bandit = EpsilonGreedyBandit()
        self.ideal_hr = ideal_hr
        self.ideal_speed = ideal_speed
        self.ideal_stability = ideal_stability

    def calculate_reward(self, heart_rate, rep_speed, stability):
        hr_diff = abs(self.ideal_hr - heart_rate)
        speed_diff = abs(self.ideal_speed - rep_speed)
        stability_diff = abs(self.ideal_stability - stability)

        # Negative reward for large deviations
        reward = - (hr_diff + speed_diff + stability_diff)
        return reward

    def recommend_weight_change(self, heart_rate, rep_speed, stability):
        context = [heart_rate, rep_speed, stability]
        action = self.bandit.select_action(context)
        return action

    def update_model(self, action, heart_rate, rep_speed, stability):
        reward = self.calculate_reward(heart_rate, rep_speed, stability)
        self.bandit.update_values(action, reward)
        return reward


# Example usage within simulation:
if __name__ == "__main__":
    human = Human(height=70, weight=180, age=30, one_rm=200)
    machine = WeightMachine(equipment_id="W01", weight_lb=150, human=human)
    manager = WorkoutManager(human)

    for _ in range(2000):  # Simulate 10 recommendations
        simulated_hr = random.randint(120, 160)
        simulated_speed = random.uniform(1.5, 3.0)
        simulated_stability = random.uniform(3, 10)

        action = manager.recommend_weight_change(simulated_hr, simulated_speed, simulated_stability)
        print(f"Recommended weight adjustment: {action} lbs")

        reward = manager.update_model(action, simulated_hr, simulated_speed, simulated_stability)
        print(f"Observed reward: {reward}\n")
