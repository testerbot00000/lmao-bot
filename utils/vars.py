import time
import json
import io

replace_ass_msg = "You appear to have misplaced your ass while laughing. Here is a replacement: :peach:"

deck = {}                   # TO BE WORKED ON: deck feature
# init = []                   # Guilds where settings have been initialized
guild_count = 0
dm_count = 0
start_time = time.time()    # Start time for lmao uptime command
last_use_time = time.time()
maintenance_time = "TBD"
no_command_invoked = False

settings = {}
def import_settings():
    with io.open("data/settings.json") as f:
        settings_data = json.load(f)
        for guild_id in settings_data.keys():
            settings[guild_id] = GuildSettings(guild_id)
def export_settings(guild_id):
    with io.open("data/settings.json") as f:
        settings_data = json.load(f)
        settings_data[guild_id] = {
            "cmd_prefix": get_prefix(guild_id),
            "replace_ass_chance": get_replace_ass_chance(guild_id),
            "react_chance": get_react_chance(guild_id)
        }
        new_settings_data = json.dumps(settings_data, indent=4)
        with io.open("data/settings.json", "w+", encoding="utf-8") as fo:
            fo.write(new_settings_data)
    with io.open("data/admins.json") as f:
        admins_data = json.load(f)
        admins_data[guild_id] = get_lmao_admin_list(guild_id)
        new_admins_data = json.dumps(admins_data, indent=4)
        with io.open("data/admins.json", "w+", encoding="utf-8") as fo:
            fo.write(new_admins_data)
    with io.open("data/customs.json") as f:
        customs_data = json.load(f)
        customs_data[guild_id] = get_custom_cmd_list(guild_id)
        new_customs_data = json.dumps(customs_data, indent=4)
        with io.open("data/customs.json", "w+", encoding="utf-8") as fo:
            fo.write(new_customs_data)
def update_settings(guild_id, guild_settings):
    settings[guild_id] = guild_settings

def set_no_command_invoked(invoked):
    global no_command_invoked
    custom_invoked = invoked
def get_no_command_invoked():
    return no_command_invoked

# Represents a given guild's settings
class GuildSettings:

    def __init__(self, guild_id):
        self.var = 0
        self.guild_id = str(guild_id)

        # Prefix for lmao-bot commands; default is "lmao"
        self.prefix = "lmao"
        self.init_prefix()
        # Dictionary for storing lmao admins
        self.lmao_admin_list = "[]"
        self.init_lmao_admin_list()
        # Dictionary for storing custom commands.
        self.custom_cmd_list = "{}"
        self.init_custom_cmd_list()
        # Chance of ass replacement
        self.replace_ass_chance = 100
        self.init_replace_ass_chance()
        # Chance of ass reaction
        self.react_chance = 100
        self.init_react_chance()

    def get_guild_id(self):
        return self.guild_id

    def init_prefix(self):
        with io.open("data/settings.json") as f:
            settings_data = json.load(f)
            try:
                self.prefix = settings_data[self.guild_id]["cmd_prefix"].strip()
            except (KeyError, NameError) as e:
                self.prefix = "lmao"
        return self.prefix
    def set_prefix(self, prefix):
        self.prefix = prefix
        return self.prefix
    def get_prefix(self):
        return self.prefix

    def init_replace_ass_chance(self):
        with io.open("data/settings.json") as f:
            settings_data = json.load(f)
            try:
                self.replace_ass_chance = settings_data[self.guild_id]["replace_ass_chance"]
            except (KeyError, NameError) as e:
                self.replace_ass_chance = 100
        return self.replace_ass_chance
    def set_replace_ass_chance(self, replace_ass_chance):
        self.replace_ass_chance = replace_ass_chance
        return self.replace_ass_chance
    def get_replace_ass_chance(self):
        return self.replace_ass_chance

    def init_react_chance(self):
        with io.open("data/settings.json") as f:
            settings_data = json.load(f)
            try:
                self.react_chance = settings_data[self.guild_id]["react_chance"]
            except (KeyError, NameError) as e:
                self.react_chance = 100
        return self.react_chance
    def set_react_chance(self, react_chance):
        self.react_chance = react_chance
        return self.react_chance
    def get_react_chance(self):
        return self.react_chance

    def init_lmao_admin_list(self):
        with io.open("data/admins.json") as f:
            admins_data = json.load(f)
            try:
                self.lmao_admin_list = admins_data[self.guild_id]
            except KeyError:
                self.lmao_admin_list = []
    def add_lmao_admin(self, member_id):
        self.lmao_admin_list.append(str(member_id))
        return self.lmao_admin_list
    def remove_lmao_admin(self, member_id):
        self.lmao_admin_list = [admin for admin in lmao_admin_list[self.guild_id] if admin != str(member_id)]
        return self.lmao_admin_list
    def set_lmao_admin_list(self, lmao_admin_list):
        self.lmao_admin_list = lmao_admin_list
        return self.lmao_admin_list
    def get_lmao_admin_list(self):
        return self.lmao_admin_list

    def init_custom_cmd_list(self):
        with io.open("data/customs.json") as f:
            full_custom_cmd_list = json.load(f)
            try:
                self.custom_cmd_list = full_custom_cmd_list[self.guild_id]
            except KeyError:
                self.custom_cmd_list = {}
    def add_custom_cmd(self, key, value):
        self.custom_cmd_list[key] = str(value)
        return self.custom_cmd_list
    def delete_custom_cmd(self, key):
        self.custom_cmd_list.pop(key, None)
        return self.custom_cmd_list
    def set_custom_cmd_list(self, custom_cmd_list):
        self.custom_cmd_list = custom_cmd_list
        return self.custom_cmd_list
    def get_custom_cmd_list(self):
        return self.custom_cmd_list

def set_start_time(time):
    global start_time
    start_time = time
    return start_time
def get_start_time():
    return start_time

def set_last_use_time(time):
    global last_use_time
    last_use_time = time
    return last_use_time
def get_last_use_time():
    return last_use_time

def set_maintenance_time(time):
    global set_maintenance_time
    maintenance_time = time
    return maintenance_time
def get_maintenance_time():
    return maintenance_time

def increment_guild_count():
    global guild_count
    guild_count += 1
    return guild_count
def reset_guild_count():
    global guild_count
    guild_count = 0
    return guild_count
def get_guild_count():
    return guild_count

def increment_dm_count():
    global dm_count
    dm_count += 1
    return dm_count
def reset_dm_count():
    global dm_count
    dm_count = 0
    return dm_count
def get_dm_count():
    return dm_count

# def add_to_init(guild_id):
#     global init
#     init.append(guild_id)
#     return init
# def get_init():
#     return init
# def is_in_init(guild_id):
#     return guild_id in init

def set_prefix(guild_id, prefix):
    settings[str(guild_id)].set_prefix(prefix)
    return settings[str(guild_id)].get_prefix()
def get_prefix(guild_id):
    try:
        return settings[str(guild_id)].get_prefix()
    except KeyError:
        try:
            return settings[str(guild_id)].init_prefix()
        except KeyError:
            settings[str(guild_id)] = GuildSettings(guild_id)
            return settings[str(guild_id)].get_prefix()

def set_replace_ass_chance(guild_id, replace_ass_chance):
    settings[str(guild_id)].set_replace_ass_chance(replace_ass_chance)
    return settings[str(guild_id)].get_replace_ass_chance()
def get_replace_ass_chance(guild_id):
    try:
        return settings[str(guild_id)].get_replace_ass_chance()
    except KeyError:
        try:
            return settings[str(guild_id)].init_replace_ass_chance()
        except KeyError:
            settings[str(guild_id)] = GuildSettings(guild_id)
            return settings[str(guild_id)].get_replace_ass_chance()

def set_react_chance(guild_id, react_chance):
    settings[str(guild_id)].set_react_chance(react_chance)
    return settings[str(guild_id)].get_react_chance()
def get_react_chance(guild_id):
    try:
        return settings[str(guild_id)].get_react_chance()
    except KeyError:
        try:
            return settings[str(guild_id)].init_react_chance()
        except KeyError:
            settings[str(guild_id)] = GuildSettings(guild_id)
            return settings[str(guild_id)].get_react_chance()

def set_lmao_admin_list(guild_id, lmao_admin_list):
    settings[str(guild_id)].set_lmao_admin_list(lmao_admin_list)
    return settings[str(guild_id)].get_lmao_admin_list()
def get_lmao_admin_list(guild_id):
    try:
        return settings[str(guild_id)].get_lmao_admin_list()
    except KeyError:
        try:
            return settings[str(guild_id)].init_lmao_admin_list()
        except KeyError:
            settings[str(guild_id)] = GuildSettings(guild_id)
            return settings[str(guild_id)].get_lmao_admin_list()
def add_lmao_admin(guild_id, member_id):
    settings[str(guild_id)].add_lmao_admin(member_id)
    return settings[str(guild_id)].get_lmao_admin_list()
def remove_lmao_admin(guild_id, member_id):
    settings[str(guild_id)].remove_lmao_admin(member_id)
    return settings[str(guild_id)].get_lmao_admin_list()

def set_custom_cmd_list(guild_id, custom_cmd_list):
    settings[str(guild_id)].set_custom_cmd_list(custom_cmd_list)
    return settings[str(guild_id)].get_custom_cmd_list()
def get_custom_cmd_list(guild_id):
    try:
        return settings[str(guild_id)].get_custom_cmd_list()
    except KeyError:
        try:
            return settings[str(guild_id)].init_custom_cmd_list()
        except KeyError:
            settings[str(guild_id)] = GuildSettings(guild_id)
            return settings[str(guild_id)].get_custom_cmd_list()
def add_custom_cmd(guild_id, key, value):
    settings[str(guild_id)].add_custom_cmd(key, value)
    return settings[str(guild_id)].get_custom_cmd_list()
def delete_custom_cmd(guild_id, key):
    settings[str(guild_id)].delete_custom_cmd(key)
    return settings[str(guild_id)].get_custom_cmd_list()