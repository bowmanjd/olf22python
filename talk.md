# Python: the Multi-tool for System Management
__OLF Conference 2022, Jonathan Bowman__

## Introduction (2 minutes)

Welcome. I am Jonathan Bowman. I am a data engineer by day, a hobbyist developer all the time, and I have some experience in IT, in web development, teaching, and consulting. My computer history started in 1982 when my family got a Commodore 64 for Christmas. My parents only bought us two rather boring games, so we kids were left with blinking cursor and the BASIC programming language. That computer became a place to experiment, learn, customize, build, tear down, build again. It was an entire world to constantly explore.

Fast forward to 1999, finishing my Bachelor's degree so I could be a high school English teacher, and I heard about Linux. Discovering Linux and open source was like cresting a hill and seeing this infinite landscape stretched out. Like that old Commodore 64, it was a place to learn and build, but even more open. Where information was freely available, and the tools were attainable.

I became a middle and high school teacher, bringing with me that re-kindled interest in building digital things. And I quickly found that this vast open source landscape provided plenty of natural resources for helping others. I evolved into being an IT technician at the school where I worked. Thrived on offering others direction, pointing them to freely available tools. Configuring servers, desktops, web pages to support the adventures that my co-workers and students were on.

And continuing to develop and build on my own, building and tearing down my machines and homelab.

## The benefits of automation

I quickly learned that while building and configuring systems is certainly a lot of fun, there are a variety of tasks that are either:

- tedious
- hard to remember


This need for efficiency and/or repeatability is common, and many tools for automation that have arisen over the decades to fill these needs.

By "automation" I simply mean delegating some work to robots that you train. That doesn't necessarily mean a full "set it and forget it" automation. For instance, if you take the videos that your phone makes, and regularly convert these to a different format and resolution using ffmpeg, that is a task ripe for simple manually triggered automation. (Other examples)?

Two tools/classes of tools for system automation

- Bash
- Ansible

There are certainly more, but these are two common ones. Ansible and its similar counterparts, such as Chef, Puppet, and Saltstack, are for configuration management of a variety of systems, such as Linux servers. These tools use a domain-specific language that is easy to read, alter, and commit to version control. Bash scripts offer far more flexibility, but require a lot of sometimes hard-to-acquire knowledge about not only Bash, but the tools you will need to use along with Bash, such as grep, cut, tail, head, cat, sed, maybe even awk.

Both can automate tedious tasks. Ansible is by far more readable and shareable. A Bash script has less guardrails, and is useful for more than just configuration management.

I think Python occupies a middle place between these two. It can be used to do anything Ansible does (in fact, both Ansible and Saltstack are written in Python) and it can do anything Bash does, but unlike either of these, it is a general-purpose programming language with a multi-faceted ecosystem.

When your bash scripts:
- require a lot of complicated string, array, or data processing 
- require tools that are unavailable or inconsistent on the target machine (and Python is available)
- are becoming large, complicated, or difficult to read

When Ansible is:
- too heavy of a framework
- too slow
- requiring a lot of extra shell scripting to process outputs

Keep in mind, Python can work well with Bash, and with Ansible and other tools.

An [informative debate about the merits of Bash vs. Python on Stackoverflow](https://stackoverflow.com/questions/2424921/python-vs-bash-in-which-kind-of-tasks-each-one-outruns-the-other-performance-w)


## Why Python?

Many scripting languages exist that fill this space: Perl is the old standby, Ruby and even Javascript can be used. Lua is probably worth exploring!

If you find something that works as well as Python, excellent!

If you are weighing options, a couple quotes to consider:

- "The Python space is beautiful, and great, and big" -- Lorena Mesa, Engineer at GitHub, former chair of PSF
- "I came for the language, I stay for the community." - Brett Cannon, Dev lead on the Python extension for Visual Studio Code
- "batteries included" philosophy of Python. A robust standard library.

Cross-platform: when the scripts you write might end up being used by different operating systems, Python might be a good fit

## Getting started with Python

Automate the boring stuff

Django Girls tutorial

The python docs

Awesome python list?

## Lightning intro to Python (10 minutes)

- Download/install
- online, docker, or virtualenv
- The REPL
- Editors (vscode)
- Functions, arguments
- types
- dict
- loops
- conditions

## virtualenv

- `python -m venv .venv`
- `. .venv/bin/activate`

## Command execution

- subprocess.run()
- plumbum

## File system manipulation

- pathlib.Path()
- read_text
- write_text

## Processing command line arguments

- sys.argv
- argparse
- click
- typer
- plumbum

## JSON

- docker config

## CSV



## Web APIs





data from web APIs.
