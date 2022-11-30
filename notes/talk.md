# Python: the Multi-tool for System Management
__OLF Conference 2022, Jonathan Bowman__

## Introduction (2 minutes)

(1st Slide). Welcome. I am Jonathan Bowman. I am a data engineer by day, a hobbyist developer all the time, and I have some experience in IT, in web development, teaching, and consulting.

(Slide). My computer history started in 1982 when my family got a Commodore 64 for Christmas. My parents only bought us two educational games, so we kids were left with blinking cursor and the BASIC programming language. Which was perfect! That computer became a place to experiment, learn, customize, build, tear down, build again. It was an entire world to constantly explore.

(Slide; Python REPL, hard refresh if needed). Decades later I found the Python REPL (Read Evaluate Print Loop or just the prompt) to be the same: approachable, powerful, available. A place to experiment, tear down, build again. (No production filesystems were harmed in the making of this presentation)

I did not go straight from the Commodore to Python. The path to get there involved the open source landscape.

(Slide). From the Commodore in the 80s, fast forward to 1999, finishing my Bachelor's degree so I could be a high school English teacher, and I heard about Linux. Discovering Linux and open source was like cresting a hill and seeing this infinite landscape stretched out (with key features highlighted). Information was freely available, and the tools were attainable.

(Slide. Holding hands). 

I became a middle and high school teacher, bringing with me that re-kindled interest in building digital things. Ever since then I have continued to develop and build on my own, building and tearing down my machines and homelab. But I quickly found that this vast open source landscape provided plenty of natural resources for _helping others_. I evolved into being an IT technician at the school where I worked. Thrived on responding to others' needs and questions, pointing them to freely available tools. Configuring servers, desktops, web pages to support the adventures that my co-workers and students were on.

I have a hunch that I am not the only one here with the underlying motivation to share and to help. But this noble adventure is not without its difficulties, right?

(Slide) This helping others is often hindered by tasks that are

- taking too much time
- hard to remember
- prone to human error


Thus the desire for automation! To improve efficiency, repeatability, and reliability.

All of these are quite desirable with Linux system administration, configuration, whether you are working with an Ubuntu laptop, an Open-WRT router, a datacenter with hundreds of RHEL VMs, or your Archlinux-based homelab. And, yes, even other platforms.

(Slide.) When considering system automation in the open source world, I immediately think of two classes of tools: represented well by bash and Ansible (and similar shells and tools)

Both Bash and Ansible can automate tedious tasks. Ansible is more readable and shareable. A Bash script has less guardrails, and is useful for more than just configuration management.

I think Python occupies a middle place between these two. It can be used to do anything Ansible does and it can do anything Bash does, but unlike either of these, it is a general-purpose programming language with a multi-faceted ecosystem.

__None of these are the right tool for _every_ job. There are always going to be tasks that are best with one or the other, or something else entirely.__

(Slide) Use Python when:

- Bash scripts are too large, complicated
- Processing complex string, array, or data
- Target machine lacks required commands
- Ansible is too heavy, slow, simple, or unavailable
- Cross-platform is desirable
- Already know or want to learn Python

Keep in mind: Python works well with Bash and with Ansible. This isn't an either/or choice. Also note an interesting discussion on Stackoverflow.

(Slide). Why Python?

Many scripting languages exist that fill this space: Perl is the old standby, Ruby and even Javascript can be used. Lua is probably worth exploring!

If you find something that works as well as Python, excellent!

(Slide). If you are weighing options, a couple quotes to consider:

- "The Python space is beautiful, and great, and big" -- Lorena Mesa, Engineer at GitHub, former chair of PSF
- (Slide). "I came for the language, I stay for the community." - Brett Cannon, Dev lead on the Python extension for Visual Studio Code
- (Slide). "batteries included" philosophy of Python. A robust standard library.


(Slide). Some suggestions for learning Python (all free):

(Slide). Automate the boring stuff

(Slide). Django Girls tutorial

(Slide). The python docs

(Slide). Awesome Python list

(Slide). help()

(Slide). help output

(Slide). Numerous ways of installing Python

(Slide). Don't be intimidated... But some intentionality is a good thing.

(Slide).

- If unsure, just download the distro for your machine
- If on Linux, there is likely a python3 package in your repository
- scoop.sh: a gentle on-ramp to open source software

(Slide). Linux package repos typically label python as python3, and python is launched as python3 although most distros have ways of making python launch python3, such as python-is-python3 (Ubuntu), pythonispython3 (Alpine), python-unversioned-command (Fedora) or shell config (.bashrc). Surely this need will go away the further we are from Python 2

(Slide). There are options for Python on the web.

(Slide). How to install packages: with pip. Singly or several at once..

(Slide). If you want to play around with installing python packages, a virtual environment is recommended.

Create a directory, then activate it. Easy to just delete the virtual env directory afterward and start fresh.

Docker could be used in place of this.

(Slide). Python editors. If in doubt, use what you already are familiar with, or just use VSCode

(Slide). Lightning intro to Python: see examples in the repo.

(Slide). Functions

(Slide). Use def and return.

(Slide). Default arguments can be assigned.

(Slide). Named arguments (also, f-strings). These are unrelated, but both shown here.

(Slide). Common types in Python: (step through)

(Slide). The dict. A hash type. Or a mapping. Or an associative array. Named values... Get a value by name.

(Slide). Various comparison operators, that work on a variety of types, not just numbers.

(Slide). Loops over am iterable (collection or range). (Review examples)

(Slide). Shell scripting libraries included in Python (summary)

(Slide). Data handling libraries included in Python (summary)

(Slide). Let's talk about subprocess

(Slide). subprocess.run can be used to do anything. Many options. Here it captures text output, tests for success. Note the list of arguments, the recommended way of passing commands. The first one is the command itself.

(Slide). Can run a shell command verbatim. But beware of untrusted user inputs (`; rm -rf /`)

(Slide). check_output shortcut (don't have to specify capture, nor pull stdout)

(Slide). check_call shortcut if output is not needed

(Slide). Summary slide. 

(Slide). SSH

(Slide). Paramiko example. A little involved, but not too bad. However, doesn't read SSH config very easily.

(Slide). Plumbum. This is a library I am getting to know. If you were serious about using Python for all your shell scripting needs, I think you want to get to know plumbum, too. Import executables from the PATH easily...

(Slide). Easy SSH. Just uses the OpenSSH binary under the hood, so everything just works.

(Slide). Other SSH options. If you are familiar with async/await syntax with Python or other languages, consider AsyncSSH.

Fabric is built on Paramiko with easier support for SSH config files.

But just using SSH is also an option, especially if Python is on the target machine

(Slide). File manipulation with pathlib.

- importing into global namespace
- the path object
- the convenient read_text function
- Note the `elif`
- breaking up a long string

(Slide). Loop through file line by line.

`with` creates a context in which you can do things with a temporarily opened entity, and trust that it will close when you are done.

If you run this, it should output a line with your distro name on it.

(Slide).

- Just an example of combining file operations with the shlex module
- shlex parses shell-like syntax safely
- such as a file that might be sourced by Bash, like /etc/os-release

(Slide). Writing text with pathlib is as easy as reading it. Here we write a message of the day.

(Slide).

(Slide). Let's write a program that takes arbitrary text as an argument, then writes it to the message of the day. But what if there are multiple arguments, or none, or if the user wants help.

(Slide). In case it is too tedious to write "python3" first.

(Slide). In the standard library, there is a nice argument parser called argparse. Try executing without an argument, or with motder.py -h (builtin help)

(Slide). While argparse is great, you may find some external libraries desirable for ease of use and even more features. And, yes, plumbum to the rescue again.

(Slide). For terminal output that is glamorous, you can try these libraries (rich has been around longer. textual the new hotness. Written by the same person)

(Slide). Python also has ability to handle temporary files. This is quite useful when editing a file in place.

(Slide). There is a broad and deep Python ecosystem around data manipulation. Here are a few helpers that are builtin.

(Slide). The JSON module can turn many Python objects, lists, or strings into JSON.

(Slide). And can deserialize JSON as well, converting it to Python objects. Here we load the config for the docker service.

(Slide).

(Slide). This is what a simple CSV file looks like.

(Slide). We can read that file row by row and then parse the fields in the row.

(Slide). There is also the ability to read each row as a dictionary, so you can always address the columns by the header (this assumes a header row, of course).

(Slide). Writing is similar to reading. Able to write line by line.

(Slide). Web requests

(Slide). There are really good third party http client libraries out there, but the one that is included with Python can work well, too. Be careful with user provided URLs, though! At least check if url startswith('http'). Also note that the response is returned as bytes, which you may which to decode as a string.

(Slide). 

(Slide). 

- jsonplaceholder __simulates__ a post

(Slide). Some external libraries you may wish to explore. requests is exceedinly popular http client, httpx is my favorite, BeautifulSoup or scrapy are excellent for actually parsing HTML if web scraping is your thing.

(Slide). Go point by point.

(Slide). Hold still while I throw a lot of links at you. Just in case something here is a path worth exploring for your needs.

Network engineers. Also note that nornir is more general purpose, similar to fabric, in that it is like Ansible, but you use the full strength of Python rather than a DSL.

(Slide). Various libraries to help you manage hypervisors.

(Slide). And Managing containers.

(Slide). Thank you. Questions? Opinions? Good arguments we can have with one another?



[boring]: https://automatetheboringstuff.com/
[libvirt]: https://www.libvirt.org/docs/libvirt-appdev-guide-python/en-US/html/
[shlex]: https://docs.python.org/3/library/shlex.html
[subprocess]: https://docs.python.org/3/library/subprocess.htm
