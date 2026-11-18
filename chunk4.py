# Taking raw string input from user
user_name = input("Enter operator handle: ")

# Taking numeric input and casting it immediately to float
cpu_load = float(input("Enter current CPU load (%): "))

# Taking whole number input and casting to int
active_tasks = int(input("Enter total active tasks: "))

# Decision logic based on user input
if cpu_load >= 80.0:
    alert_level = "CRITICAL"
    action = "Throttle background tasks"
elif cpu_load >= 50.0:
    alert_level = "WARNING"
    action = "Monitor memory usage"
else:
    alert_level = "OPTIMAL"
    action = "System healthy"

# Clean formatted output
print("\n--- SYSTEM REPORT ---")
print(f"Operator: {user_name}")
print(f"CPU Load: {cpu_load}% | Tasks: {active_tasks}")
print(f"Status: [{alert_level}] -> Action: {action}")



