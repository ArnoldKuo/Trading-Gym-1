from env import TradeEnv
import time
import random
import json
import logging


logger = logging.getLogger('gym-trading')

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

if __name__ == '__main__':
    env = TradeEnv(data_path='/data/money/source_minute.json')
    action = 0
    obs, reward, done, info = env.reset()
    while not done:
        action = random.sample([-1, 0, 1], 1)[0]
        obs, reward, done, info = env.step(action)
        env.render()
        if done:
            break
    time.sleep(1)
