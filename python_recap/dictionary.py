active_users = {}
inactive_users = {}
users = {"particles": "active", "inkbaby": "inactive", "parti": "active"}

for user, status in users.items():  # Use .items() to iterate through key-value pairs.
    if status == 'inactive':
        inactive_users[user] = status
    else:
        active_users[user] = status
