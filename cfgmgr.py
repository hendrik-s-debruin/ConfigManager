#!/usr/bin/env python

import sys
import os
import os.path

# script usage
usage = """Usage:
cfgmgr --new <name>
cfgmgr --list
cfgmgr --clone <alias> <repo>
cfgmger <name> <git command>"""

# Global variables for paths
home_dir = os.path.expanduser("~")
config_location = home_dir + "/.config/cfgmgr"
configuration_dirs = config_location + "/configs"

class ConfigLister:
	"""
	Lists the configurations that are tracked by cfgmgr
	"""
	def run(self):
		for el in os.listdir(configuration_dirs):
			if(os.path.isdir(configuration_dirs + "/" + el)):
				print(el)

class ConfigCreator:
	"""
	Creates a new configuration to be tracked and managed by cfgmgr
	"""
	def __init__(self, config_name):
		self.config_name = config_name
		self.config_location = configuration_dirs + "/" + config_name
		self.init_command = "git init --bare " + self.config_location

	def run(self):
		if(os.path.isdir(self.config_location)):
			raise RuntimeError("Configuration '" + self.config_name + "' already exists")
		os.system(self.init_command)

class ConfigCloner:
	def __init__(self, config_name, remote):
		self.config_name = config_name
		self.remote = remote
		self.config_path = configuration_dirs + "/" + self.config_name
		self.clone_command = "git clone --bare " + self.remote + " '" + self.config_path + "'"

	def run(self):
		if(os.path.isdir(self.config_path)):
			raise RuntimeError("Configuration '" + self.config_name + "' already exists")
		os.system(self.clone_command)

class ConfigUpdator:
	def __init__(self, config_name, git_command):
		self.config_name = config_name
		self.config_location = configuration_dirs + "/" + config_name
		self.git_command = "git --git-dir='" + self.config_location + "' --work-tree='" + home_dir + "' " + git_command

	def run(self):
		if(not os.path.isdir(self.config_location)):
			raise RuntimeError("Configuration '" + self.config_name + "' does not exist")
		os.system(self.git_command)

def parse_command():
	if(len(sys.argv) < 2):
		raise RuntimeError(usage)

	# ================================ Options =================================
	if sys.argv[1] == "--list":
		if len(sys.argv) != 2:
			raise RuntimeError(usage)
		else:
			return ConfigLister()

	if sys.argv[1] == "--new":
		if len(sys.argv) != 3:
			raise RuntimeError(usage)
		else:
			return ConfigCreator(sys.argv[2])

	if sys.argv[1] == "--clone":
		if len(sys.argv) != 4:
			raise RuntimeError(usage)
		else:
			return ConfigCloner(sys.argv[2], sys.argv[3])

	# Invalid option
	if sys.argv[1].startswith('-'):
		option = sys.argv[1]
		msg = "Unknown option: '" + option + "'"
		raise RuntimeError(msg + "\n" + usage)

	# ================================== Git ===================================
	if len(sys.argv) < 3:
		raise RuntimeError(usage)
	else:
		config_name = sys.argv[1]
		git_command = " ".join(sys.argv[2:])
		return ConfigUpdator(config_name, git_command)

def main():
	try:
		command = parse_command()
		command.run()
	except Exception as e:
		print(e)
		exit(1)

if __name__ == "__main__":
	main()
