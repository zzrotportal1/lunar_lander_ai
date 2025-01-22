import gymnasium as gym
from stable_baselines3 import PPO
import os


models_dir = "models/PPO"

env = gym.make('LunarLander-v2',  render_mode="human")  # continuous: LunarLanderContinuous-v2

model_path = f"{models_dir}/900000.zip"
model = PPO.load(model_path, env=env)

episodes = 5


obs = env.reset()
while True:
    action, _states = model.predict(obs[0])
    obs = env.step(action)
    env.render()
