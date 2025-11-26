# Build a User Configuration Manager

test_settings = {
    "theme": "light",
    "notification": "enabled",
    "volumn": "high"
}

def add_setting(settings, data):
    key = data[0].lower()
    value = data[1].lower()
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings.update(dict({(key, value)}))
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings, data):
    key = data[0].lower()
    value = data[1].lower()
    if key in settings:
        settings.update(dict({(key, value)}))
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, key):
    key = key.lower()
    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"

def view_settings(settings):
    if len(settings) == 0:
        return "No settings available."
    else:
        msg = "Current User Settings:\n"
        for key, value in settings.items():
            msg += f"{key.title()}: {value}\n"
    return msg

print(view_settings(test_settings))

print(add_setting(test_settings, ('THEME', 'dark')))
print(view_settings(test_settings))

print(update_setting(test_settings, ('THEME', 'dark')))
print(view_settings(test_settings))

print(delete_setting(test_settings, 'theme'))
print(view_settings(test_settings))
