import multiprocessing as mp

import gym
import torch
import time
from envs.subproc_vec_env import SubprocVecEnv
from episode import BatchEpisodes


def make_env(env_name):
    def _make_env():
        return gym.make(env_name)

    return _make_env


class BatchSampler(object):
    def __init__(self, env_name, batch_size, device, seed, num_workers=mp.cpu_count() - 1):
        self.env_name = env_name
        self.batch_size = batch_size
        self.num_workers = num_workers
        self.device = device

        self.queue = mp.Queue()
        self.envs = SubprocVecEnv([make_env(env_name) for _ in range(num_workers)], queue=self.queue)
        self.envs.seed(seed)
        self._env = gym.make(env_name)
        self._env.seed(seed)

    def sample(self, policy, params=None, gamma=0.95, batch_size=None):
        if batch_size is None:
            batch_size = self.batch_size
        episodes = BatchEpisodes(batch_size=batch_size, gamma=gamma, device=self.device)
        for i in range(batch_size):
            self.queue.put(i)
        for _ in range(self.num_workers):
            self.queue.put(None)
        observations, batch_ids = self.envs.reset()
        dones = [False]
        while (not all(dones)) or (not self.queue.empty()):
            with torch.no_grad():
                observations_tensor = torch.from_numpy(observations).to(device=self.device)
                actions_tensor = policy(observations_tensor, params=params).sample()
                actions = actions_tensor.cpu().numpy()

            time.sleep(0.0001)
            new_observations, rewards, dones, new_batch_ids, _ = self.envs.step(actions)
            episodes.append(observations, actions, rewards, batch_ids)
            observations, batch_ids = new_observations, new_batch_ids
        return episodes

    def reset_task(self, task):
        tasks = [task for _ in range(self.num_workers)]
        reset = self.envs.reset_task(tasks)
        return all(reset)

    def sample_tasks(self, num_tasks):
        tasks = self._env.unwrapped.sample_tasks(num_tasks)
        return tasks
