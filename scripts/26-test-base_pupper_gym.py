import time

import gym
import stanford_quad  # need this unused import to get our custom environments
import numpy as np

env = gym.make("PupperBaseDebug-v0")

state = env.reset()
done = False
while not done:
    action = env.action_space.sample()
    obs, rew, done, misc = env.step(action)
    print(
        f"action: {np.around(action,2)}, " f"obs: {np.around(obs,2)}, " f"rew: {np.around(rew,2)}, " f"done: {done}"
    )