ConfigManager
================================================================================

`ConfigManager` is a simple script to manage dot files on Linux. It is a
thin wrapper around `git`. `ConfigManager` creates a new git repository for each
program's configuration that you would like to track. Autocompletion is
available for the `zsh` shell.

Usage
--------------------------------------------------------------------------------

Tracking a new program's configuration:

	$ cfgmgr new <alias>

The above will initialise a new git repository inside of `cfgmgr`'s
configuration location for the program identified by `alias`.

Cloning an already-existing configuration:

	$ cfgmgr clone <alias> <repo>

The above will clone an already-tracked program's configuration from `repo` into
`cfgmgr`'s configuration location. The program can be referenced by `alias`.

To list all the programs that are being tracked:

	$ cfgmgr list

Tracking of program configuration files is managed via `git`. To run a git
command on a program's configuration, simply call:

	$ cfgmgr manage <alias> <git command>

Here, `alias` identifies the command, and `git command` is the command you wish
to run.

To run some git command on all of your tracked configurations, call:

	$ cfgmgr foreach <git command>

Examples
--------------------------------------------------------------------------------

Consider tracking your `vim` configuration. You want to sync this configuration
among machines, but want slightly different configuration on your personal
machine from that on the machine at work.

Your home machine is already configured nicely, so we start the tracking there:

	$ cfgmgr new vim
	$ cfgmgr manage vim add ~/.vimrc
	$ cfgmgr manage vim commit -m "initial commit"
	$ cfgmgr manage vim add origin https://github.com/hendrik-s-debruin/configuration_vim.git
	$ cfgmgr manage vim push

Now, you clone this already-existing repository onto your work machine:

	$ cfgmgr clone vim https://github.com/hendrik-s-debruin/configuration_vim.git

Since your work pc needs a slightly different configuration, we create a new
branch for that pc:

	$ cfgmgr manage vim checkout -b work

Now, make any changes, add them and push them:

	$ vim .vimrc
	$ cfgmgr manage vim add .vimrc
	$ cfgmgr manage vim commit -m "super cool changes"
	$ cfgmgr manage vim push

During the course of the day you are likely to make multiple changes to multiple
configuration repositories. When you get back home, you can sync all of them
again with the `foreach` command:

	$ cfgmgr foreach pull


Installation
================================================================================

A package exists for `ArchLinux`, but is not available on the `AUR`. To install
it, simply run from the root of the project:

	$ makepkg --install

For non-Arch or local installs, simply put `cfgmgr` somewhere in your `PATH`.
Optionally, for `zsh` tab completion, put `_cfgmgr` in your `fpath`.
