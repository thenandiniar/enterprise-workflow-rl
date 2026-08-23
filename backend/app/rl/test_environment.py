from gymnasium.utils.env_checker import check_env

from backend.app.rl.environment import TicketWorkflowEnv


env = TicketWorkflowEnv()

check_env(env)

print("RL environment passed Gymnasium validation.")
