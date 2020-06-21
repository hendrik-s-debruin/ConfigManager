ConfigManager
================================================================================

`ConfigManager` is a very simple script to manage dot files on Linux. It is a
thin wrapper around `git`. `ConfigManager` creates a new git repository for each
program's configuration that you would like to track.


Usage
--------------------------------------------------------------------------------

Tracking a new program's configuration:

	$ cfgmgr --new <alias>

The above will initialise a new git repository inside of `cfgmgr`'s
configuration location for the program identified by `alias`.

Cloning an already-existing configuration:

	$ cfgmgr --clone <alias> <repo>

The above will clone an already-tracked program's configuration from `repo` into
`cfgmgr`'s configuration location. The program can be referenced by `alias`.

To list all the programs that are being tracked:

	$ cfgmgr --list

Tracking of program configuration files is managed via `git`. To run a git
command on a program's configuration, simply call:

	$ cfgmgr <alias> <git command>

Here, `alias` identifies the command, and `git command` is the command you wish
to run.

Examples
--------------------------------------------------------------------------------

Consider tracking your `vim` configuration. You want to sync this configuration
among machines, but want slightly different configuration on your personal
machine from that on the machine at work.

Your home machine is already configured nicely, so we start the tracking there:

	$ cfgmgr --new vim
	$ cfgmgr vim add ~/.vimrc
	$ cfgmgr vim commit -m "initial commit"
	$ cfgmgr vim add origin https://github.com/hendrik-s-debruin/vim_dots.git
	$ cfgmgr vim push

Now, you clone this already-existing repository onto your work machine:

	$ cfgmgr --clone vim https://github.com/hendrik-s-debruin/vim_dots.git

Since your work pc needs a slightly different configuration, we create a new
branch for that pc:

	$ cfgmgr vim checkout -b work

Now, make any changes, add them and push them using commands of the form:

	$ cfgmgr vim <command>
