from backend.app.rl.environment import TicketWorkflowEnv


env = TicketWorkflowEnv()

state, info = env.reset()

print("State:", state)
print("Selected ticket ID:", env.current_ticket.id)
print("Category:", env.current_ticket.category)
print("Customer tier:", env.current_ticket.customer_tier)
print("Urgency:", env.current_ticket.urgency)
print("Expected escalation:", env.current_ticket.expected_escalation)

action = env.action_space.sample()

next_state, reward, terminated, truncated, info = env.step(action)

print("Selected action:", action)
print("Expected action:", info["expected_action"])
print("Reward:", reward)
print("Episode terminated:", terminated)