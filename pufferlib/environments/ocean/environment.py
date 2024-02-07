import pufferlib.emulation

from .squared import Squared
from .bandit import Bandit
from .memory import Memory
from .password import Password
from .stochastic import Stochastic
from .multiagent import Multiagent
from .spaces import Spaces
from .performance import Performance


def env_creator(name='squared'):
    if name == 'squared':
        return make_squared
    elif name == 'bandit':
        return make_bandit
    elif name == 'memory':
        return make_memory
    elif name == 'password':
        return make_password
    elif name == 'stochastic':
        return make_stochastic
    elif name == 'multiagent':
        return make_multiagent
    elif name == 'spaces':
        return make_spaces
    elif name == 'performance':
        return make_performance
    else:
        raise ValueError('Invalid environment name')

def make_squared(distance_to_target=3, num_targets=1):
    '''Puffer Squared environment'''
    env = Squared(distance_to_target=distance_to_target, num_targets=num_targets)
    return pufferlib.emulation.GymnasiumPufferEnv(env=env)

def make_bandit(num_actions=10, reward_scale=1, reward_noise=1):
    env = Bandit(num_actions=num_actions, reward_scale=reward_scale,
        reward_noise=reward_noise)
    return pufferlib.emulation.GymnasiumPufferEnv(env=env)

def make_memory(mem_length=2, mem_delay=2):
    env = Memory(mem_length=mem_length, mem_delay=mem_delay)
    return pufferlib.emulation.GymnasiumPufferEnv(env=env)

def make_password(password_length=5):
    env = Password(password_length=password_length)
    return pufferlib.emulation.GymnasiumPufferEnv(env=env)

def make_performance(delay_mean=0, delay_std=0, bandwidth=1):
    env = Performance(delay_mean=delay_mean, delay_std=delay_std, bandwidth=bandwidth)
    return pufferlib.emulation.GymnasiumPufferEnv(env=env)

def make_stochastic(p=0.7, horizon=100):
    env = Stochastic(p=p, horizon=100)
    return pufferlib.emulation.GymnasiumPufferEnv(env=env)

def make_spaces():
    env = Spaces()
    return pufferlib.emulation.GymnasiumPufferEnv(env=env)

def make_multiagent():
    env = Multiagent()
    return pufferlib.emulation.PettingZooPufferEnv(env=env)
