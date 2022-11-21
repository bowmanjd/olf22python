Python: the Multi-tool for System Management <!-- .element: class="r-fit-text" -->

![Python Swiss-army knife](assets/python-tool-o.svg) <!-- .element: class="hero" -->

Notes:

- Welcome
- I am Jonathan Bowman, software engineer from Central Pennsylvania
- The presentation is going to move fast
- Highly recommended to have the slides open, and a terminal or Python REPL

---

Learn, customize, tear down, build <!-- .element: class="r-fit-text" -->

[![Commodore 64](assets/c64.gif) <!-- .element: class="hero" -->][c64] 

[c64]: https://en.wikipedia.org/wiki/Commodore_64

Notes:

- My digital history began with the Commodore 64
- That  1 Mhz computer became a place to experiment, learn, customize, build, tear down, build again.
- I went from Commodore BASIC 2.0...

---

<!-- .slide: data-background-image="assets/pyrepl.gif"  -->

Notes:

To Python! (Decades later)

I found Python:

- Approachable
- Powerful
- Available
- The REPL is a bit like the Commodore: a place to experiment, build, tear down, build again

No production filesystems were harmed in the making of this slide deck

---

<!-- .slide: data-background-image="assets/oldrag.jpg" -->

![Tux the Linux penguin](assets/tux.svg) <!-- .element: class="hero fragment fade-up" -->

Notes:
- My path wasn't so much a progression with Python as the goal, but a journey through open source and Linux, and encountering opportunities to help others
- I found Linux and open source to be an open and inviting landscape
- (With some recommended sites to see) Tux
- Quickly learned that in open source there were many opportunities to help others.
- The landscape offering freely available tools.
- I could offer my assistance in configuring and using these tools. Such as Linux servers, web application frameworks

---

<!-- .slide: data-background-image="assets/holding-hands.svg" data-background-size="85%" -->

Notes:
- I have a hunch that I am not the only one here with the underlying motivation to share and to help
- But this noble adventure is not without its difficulties, right?

---

Hindered by tasks that are

- taking too much time
- hard to remember
- prone to human error

Notes:

I quickly found that helping others was often hindered...

Thus the desire for automation! To improve:
- Efficiency
- Repeatability
- Reliability

All of these are quite desirable with Linux system administration, configuration, whether you are working with an Ubuntu laptop, an Open-WRT router, a datacenter with hundreds of RHEL VMs, or your Archlinux-based homelab.

(Automation is also helpful and feasible on the BSDs, Mac, and, yes, even Windows.)

---

Different tools for system automation

- Bash <span class="fragment" data-fragment-index="2">(or ash/dash, zsh, fish, Elvish, xonsh, Nushell...)</span>
- Python <!-- .element: class="fragment fade-left" data-fragment-index="3" style="color: #0c9"-->
- Ansible <span class="fragment" data-fragment-index="1">(or Salt, Chef, Puppet...)</span>

Notes:

- When considering system automation in the open source world, I immediately think of two classes of tools: bash and Ansible (and similar shells and tools)
- Both Bash and Ansible can automate tedious tasks. Ansible is more readable and shareable. A Bash script has less guardrails, and is useful for more than just configuration management.
- I think Python occupies a middle place between these two. It can be used to do anything Ansible does and it can do anything Bash does, but unlike either of these, it is a general-purpose programming language with a multi-faceted ecosystem.
- None of these are the right tool for __every__ job. There are always going to be tasks that are best with one or the other, or something else entirely

---

Use Python when:

- Bash scripts are too large, complicated
- There are Complex string, array, or data processing needed
- the target machine lacks the required commands
- Ansible is too heavy, slow, simple, or unavailable
- cross-platform is desirable
- you already know or want to learn Python

[An informative debate about the merits of Bash vs. Python on Stackoverflow](https://stackoverflow.com/questions/2424921/python-vs-bash-in-which-kind-of-tasks-each-one-outruns-the-other-performance-w)

Notes:

(Walk through points)

Keep in mind: Python works well with Bash and with Ansible. This isn't an either/or choice

---

Why Python (and not other general-purpose languages)?

It isn't a competition; collect them all! <!-- .element class="fragment fade-in" -->

---

"The Python space is beautiful, and great, and big"

Lorena Mesa, Engineer at GitHub, former chair of Python Software Foundation <!-- .element class="fragment fade-in" -->

Notes:

From Github's README project. Lorena in turn quotes Brett Cannon.

---

"I came for the language, I stay for the community."

Brett Cannon, Dev lead on the Python extension for Visual Studio Code <!-- .element class="fragment fade-in" -->

---

"batteries included"

![Battery](assets/battery.svg) <!-- .element: class="hero" -->

Notes:

The standard library is huge. Lots of built-in functionality.

---

Getting started with Python

Lots of good documentation. Here are a few options...

Notes:

Move quickly through the following slides.

---

[![Automate the Boring Stuff](assets/AutomatetheBoringStuff_cover.png) <!-- .element: class="hero" -->][boring]

[boring]: https://automatetheboringstuff.com/

---

[![Django Girls](assets/djangogirls.png) <!-- .element: class="hero" -->][djangogirls]

[djangogirls]: https://tutorial.djangogirls.org/en/

---

[![Python](assets/python-logo.svg)][pythondocs]

[pythondocs]: https://docs.python.org/3/

---

[![Awesome Python cap](assets/cap.svg) <!-- .element style="height: 10vh" -->][awesomepython] <br>
[Awesome Python][awesomepython]</br>
List

[awesomepython]: https://awesome-python.com/

---

![Python help command](assets/pyhelp1.gif) <!-- .element: class="hero" -->

---

<!-- .slide: data-background-image="assets/pyhelp.gif"  -->

---

Installing Python

---

<!-- .slide: data-background-image="https://imgs.xkcd.com/comics/python_environment.png" data-background-size="contain"  -->

Notes:

- Python installation and management can be confusing, but it doesn't need to be

---

- [python.org/downloads/][downloads]
- Linux: 
	* Debian/Ubuntu: `apt install python3`
	* Fedora: `dnf install python3`
- Docker: `docker run -it python:alpine`
- Phones: Termux (Android) or Pythonista (iOS)
- Mac: see [downloads] or `brew install python`
- Windows: see [downloads] or Store or scoop/chocolatey/winget

[downloads]: https://www.python.org/downloads/

Notes:

- If unsure, just download the distro for your machine
- If on Linux, there is likely a python3 package in your repository
- scoop.sh: a gentle on-ramp to open source software

---

Making `python` launch `python3`?

- python-is-python3 (Ubuntu/Debian)
- pythonispython3 (Alpine)
- python-unversioned-command (Fedora)
- `alias python=python3`

Notes:

- Linux package repos typically label python as python3, and python is launched as `python3` although most distros have ways of making `python` launch python3, such as python-is-python3 (Ubuntu), pythonispython3 (Alpine), python-unversioned-command (Fedora) or shell config (.bashrc)
- Surely this need will go away the further we are from Python 2

---

Python REPL on the web:

- [pythonanywhere.com](https://www.pythonanywhere.com/)
- [python.org/shell](https://www.python.org/shell/)
- [github.com/codespaces](https://github.com/codespaces/)
- [repl.it/languages/python3](https://replit.com/new/python3)
- [paiza.cloud](https://paiza.cloud/)
- [c9.io](https://aws.amazon.com/cloud9/)

Notes:

- walk through points
- No particular order

---

Installing packages

```terminal
> pip install requests
> pip install plumbum httpx sqlalchemy
```

Browse at [pypi.org](https://pypi.org)

---

Virtual environments

```terminal
> python3 -m venv virtual_directory_name
> python3 -m venv .venv
> . .venv/bin/activate
```

Notes:

- if you want to play around with installing python packages, a virtual environment is recommended
- easy to just delete the virtual env directory afterward and start fresh
- Docker also works fine for this

---

Python editors

- [VSCode](https://code.visualstudio.com/)
- [PyCharm](https://www.jetbrains.com/pycharm/)
- Vim/Neovim, Emacs, Sublime Text, Helix, Zed...
- For beginners: [Thonny](https://thonny.org/), [Mu](https://codewith.mu/)

Notes:

- More than likely, the editor of your choice has good Python support; you may need to install a plugin/extension

---

Lightning intro to writing Python

[github.com/bowmanjd/olf22python](https://github.com/bowmanjd/olf22python)

![Github repo QR code](assets/github_qr.svg) <!-- .element: class="hero" -->

---

Functions and their arguments

---

```python [1-5|1-2|5|1-5]
def greet(greeting):
    return greeting + ", World!"


greet("Hello")
```

---

Default arguments

```python [1-5|1|5|1-5]
def greet(greeting="Hello"):
    return greeting + ", World!"


greet()
```

---

Named arguments and f-strings

```python [1-7|2|6-7|1-7]
def greet(greeting="Hello", audience="World"):
    return f"{greeting}, {audience}!"


greet()
greet("Salutations", "Galaxy")
greet(audience="Galaxy")
```

---

Some types

```python [1-9|1|2|3|4|5|6|7|8|9|1-9]
a_number = 12
another_number = 7.1
a_string = "Some text"
another_string = "Some more text"
a_range = range(10)
some_bytes = b"\x00\x01\x02\x03Hi"
a_list = ["Some text", 14, another_number, "你好", 1]
a_lonely_number = a_list[4]
a_boolean = True
```

---

The dict

```python [1-5|5|3|1-5]
a_dict = {"a_key": "a_value",
          "first_name": "Sheila",
          "pi": 3.14159}

archimedes_constant = a_dict["pi"]
```

---

Comparisons and conditions

```python
def compare(a, b):
    if a == b:
        print("equality")
    if not a == b:
        print("inequality")
    if a != b:
        print("also inequality")
    if a > b:
        print("greater than")
    else:
        print("less than or equal")
    if a <= b:
        print("also less than or equal")
```

---

Loops

```python [1-13|3-4|6-7|9-10|12-13|1|1-13]
import os

for variable in os.environ.keys():
	print(variable)

for path in os.getenv("PATH").split(":"):
	print(path)

for num in range(10):
	print(num)

for _ in range(10):
	print("Doing this thing 10 times.")
```

---

Shell scripting in the standard library

- [`subprocess`](https://docs.python.org/3/library/subprocess.html) for command execution
- [`pathlib`](https://docs.python.org/3/library/pathlib.html) for filesystem reading/manipulation
- [`shutil`](https://docs.python.org/3/library/shutil.html) for copying/deleting directories
- [`shlex`](https://docs.python.org/3/library/shlex.html) for parsing arguments
- [`re`](https://docs.python.org/3/library/re.html) for regular expressions
- [`fnmatch`](https://docs.python.org/3/library/fnmatch.html) for shell-like file matching
- [`argparse`](https://docs.python.org/3/library/argparse.html) for parsing command-line arguments
- [`os`](https://docs.python.org/3/library/os.html) 
- [`sys`](https://docs.python.org/3/library/sys.html)

---

Data wrangling in the standard library

- [`csv`](https://docs.python.org/3/library/csv.html)
- [`json`](https://docs.python.org/3/library/json.html)
- [`xml.etree.ElementTree`](https://docs.python.org/3/library/xml.etree.elementtree.html) (consider [defusedxml](https://github.com/tiran/defusedxml))
- [`sqlite`](https://docs.python.org/3/library/sqlite.html)
- [`urllib.request`](https://docs.python.org/3/library/urllib.request.html) for HTTP calls

Notes:

- mention XML bombs

---

The heart of shell scripting in Python:

command execution with `subprocess`

---

`subprocess.run()` with text output capture

```python
import subprocess

result = subprocess.run(["ip", "addr"],
                        capture_output=True,
                        text=True)

if result.returncode == 0 and result.stdout:
	print(result.stdout)
```

---

The same, but with shell mode (be careful)

```python
import subprocess

result = subprocess.run("ip addr",
                        capture_output=True,
                        shell=True,
                        text=True)

if result.returncode == 0 and result.stdout:
  print(result.stdout)
```

---

A shortcut with `subprocess.check_output`

```python
import subprocess

output = subprocess.check_output(["ip", "addr"],
                                 text=True)

print(output)

```

---

A shortcut with `subprocess.check_call` if output capture is not needed

```python
import subprocess

subprocess.check_call(["ip","addr"])
```

---

- `subprocess.run` for anything and everything
- `subprocess.check_output` for convenience, capturing output
- `subprocess.check_call` if execution is all that is needed
- `shell=True` parameter will pass the whole command as string to `sh`, and expand variables (security alert); otherwise pass the command as a `["list", "of", "command", "and", "parameters"]`

Notes:

- summary slide

---

SSH

with [Paramiko](https://www.paramiko.org/) 

---

```python
import paramiko

client = paramiko.SSHClient()
client.load_system_host_keys()
client.connect("server", username="user")

stdin, stdout, stderr = client.exec_command('ls /')
root_directories = stdout.read()

sftp = client.open_sftp()
with sftp.file("/etc/os-release") as f:
  for line in f:
    print(line)
```

---

Have you tried [plumbum](https://plumbum.readthedocs.io)?

```python
from plumbum.cmd import ip

ip('addr')
```

And *so* much more...

---

Such as SSH:

```python
from plumbum import SshMachine

server = SshMachine("server", user="admin")
server["uname"](['-a'])
```

---

Other SSH options

- [AsyncSSH](https://asyncssh.readthedocs.io/)
- [fabric](https://www.fabfile.org/)
- `ssh server python3 < script.py`

Notes:

- AsyncSSH is quite versatile and modern, but requires a willingness to use async/await
- If python is on the target machine, then run python script over ssh

---

File reading, writing, and manipulation with

`pathlib`

---

```python [1-11|1|3|4|9|10-11|1-11]
from pathlib import Path

filepath = Path("/etc/os-release")
os_info = filepath.read_text()
if "Fedora" in os_info:
	print("I still remember Redhat 5.1")
elif "Alpine" in os_info:
  print("Compiled with love and musl")
elif "archlinux" in os_info:
  print("A wiki and the AUR; it "
	      "doesn't get better than this!")
```

Notes:
- importing into global namespace
- the path object
- the convenient read_text function
- Note the `elif`
- breaking up a long string

---

Reading line by line

```python [1-7|4-7|5|1-7]
from pathlib import Path

filepath = Path("/etc/os-release")
with filepath.open() as f:
  for line in f:
    if line.startswith("PRETTY_NAME"):
      print(line.strip())
```

---

```python
import pathlib
import shlex

os_release_file = pathlib.Path("/etc/os-release")
os_release = os_release_file.read_text()
lexer = shlex.shlex(os_release, posix=True)
lexer.whitespace_split = True
os_info = dict(i.split('=') for i in lexer if "=" in i)
print(os_info["PRETTY_NAME"])
```

Notes:

- Just an example of combining file operations with the shlex module
- shlex parses shell-like syntax safely
- such as a file that might be sourced by Bash, like /etc/os-release

---

Writing text to a file

```python
from pathlib import Path

filepath = Path("/etc/motd")
weather = "There will be temperatures today with a chance of weather."
filepath.write_text(weather)
```

---

Processing command-line arguments

---

Easy but inflexible with `sys.argv`

Save the following to something like `motder.py`

```python
import sys
from pathlib import Path

def motder(text):
  filepath = Path("/etc/motd")
  filepath.write_text(text)

if __name__ == "__main__":
	motder(sys.argv[1])
```

Execute with:

```terminal
> sudo python3 motder.py "Good morning it is Friday!"
```

---

Add a shebang and make it executable

```python [1-10|1|1-10]
#!/usr/bin/env python3
import sys
from pathlib import Path

def motder(text):
  filepath = Path("/etc/motd")
  filepath.write_text(text)

if __name__ == "__main__":
	motder(sys.argv[1])
```

```terminal
> chmod a+x motder.py
> sudo ./motder.py "Good morning it is a lazy Friday!"
```

---

A more flexible way: `argparse`

```python
#!/usr/bin/env python3
import argparse
from pathlib import Path

def motder(text):
  filepath = Path("/etc/motd")
  filepath.write_text(text)

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("message", help="The message of the day")
  args = parser.parse_args()
	motder(args.message)
```

Note:
- builtin help
- Try executing without an argument, or with `motder.py -h`

---

Some excellent third-party CLI libraries

- [`click`](https://palletsprojects.com/p/click/)
- [`typer`](https://typer.tiangolo.com/)
- [`fire`](https://google.github.io/python-fire/)
- [`plumbum`](https://plumbum.readthedocs.io/en/latest/cli.html#command-line-interface-cli)

---

Create truly glamorous TUIs

- [`rich`](https://rich.readthedocs.io/)
- [`textual`](https://textual.textualize.io/)

---

Temporary files

```python
import pathlib
import shutil
import subprocess
import tempfile

tempdir = pathlib.Path(tempfile.mkdtemp())
temp_motd = tempdir / "motd"
temp_motd.write_text("Welcome, user!")
motd = pathlib.Path("/etc/motd")
subprocess.check_call(["sudo", "cp", temp_motd, motd])
shutil.rmtree(tempdir, ignore_errors=True)
```

---

Data

---

Writing JSON

```python[1-5|1|3|4|1-5]
import json

data = {"name": "OLF conference", "age": 20}
json_data = json.dumps(data, indent=4)
print(json_data)
```

Notes:
- line 3 is not JSON, even though it looks like it!
- indent is entirely optional

---

Reading JSON

```python[1-6|6|1-6]
import json
from pathlib import Path

filepath = Path("/etc/docker/daemon.conf")
filetext = filepath.read_text()
dockerd_conf = json.loads(filetext)
```

---

Reading CSV

---

`sample.csv`

```text
Name,Age
Michael Palin,79
John Cleese,83
OLF Conference,20
```

---

```python
import csv
from pathlib import Path

inpath = Path("sample.csv")

with inpath.open(newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader) # Skip the header
    for row in reader:
        name = row[0]
        age = row[1]
        print(f"{name} is {age} years old.")
```

---

```python
import csv
from pathlib import Path

inpath = Path("sample.csv")

with inpath.open(newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        name = row["Name"]
        age = row["Age"]
        print(f"{name} is {age} years old.")
```

Notes:
- using dict reader allows dynamically assigned columns

---

Writing CSV

```python
import csv
from pathlib import Path

outpath = Path("output.csv")

with outpath.open("w", newline="", encoding="utf-8-sig") as outfile:
  writer = csv.writer(outfile)
  new_row = {"First": "Jane", "Last": "Smith"}
  writer.writerow(["Name","Age"])
  writer.writerow(["John Cleese",83])
```

---

Web requests

---

GET some data

```python
from urllib.request import urlopen

# Avoid unsanitized user inputs, because:
# url = "file:///etc/passwd"
url = "https://wttr.in/Columbus,OH?A1nF"
with urlopen(url) as response:
  print(response.read().decode())
```

Notes:
- Be careful with user provided URLs!
- At least check if url startswith('http')

---

POST some JSON

---

```python [1-15|10|12|15|1-15]
import json
from urllib.request import Request, urlopen

url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "userid": "1001",
    "title": "POSTing JSON for Fun and Profit",
    "body": "JSON in the request body! Don't forget the content type.",
}
postdata = json.dumps(data).encode()
headers = {"Content-Type": "application/json; charset=UTF-8"}
httprequest = Request(url, method="POST", data=postdata, headers=headers)

with urlopen(httprequest) as response:
    print(response.read().decode())
```

Notes:

- jsonplaceholder __simulates__ a post
- when the Request object has data parameter specified, POST is set automatically
- note that this uses binary data, so need to decode() (utf-8 is default)

---

Third-party libraries for Web

- [`requests`](https://requests.readthedocs.io/)
- [`httpx`](https://www.python-httpx.org/)
- [`BeautifulSoup`](https://beautiful-soup-4.readthedocs.io/)
- [`scrapy`](https://scrapy.org/)

---

Other data avenues to explore

- built-in [`sqlite`](https://docs.python.org/3/library/sqlite.html)
- [`xml.etree.ElementTree`](https://docs.python.org/3/library/xml.etree.elementtree.html) or [defusedxml](https://github.com/tiran/defusedxml) or [`lxml`](https://lxml.de/)
- [`SQLAlchemy`](https://www.sqlalchemy.org/)
- [`pandas`](https://pandas.pydata.org/)
- [`numpy`](https://numpy.org/)

---

For network engineers

- [Netmiko](https://pynet.twb-tech.com/blog/automation/netmiko.html): switch management
- [Napalm](https://napalm.readthedocs.io/): network automation
- [Nornir](https://nornir.readthedocs.io/): automate everything 
- [Free Python Network Automation Course](https://pynet.twb-tech.com/) from Twin Bridges Technology

Notes:

- nornir is for more than just network devices; works great for servers, for instance

---

For virtualization

- [proxmoxer](https://proxmoxer.github.io/docs/)
- [libvirt]
- [AWS SDK for Python](https://aws.amazon.com/sdk-for-python/)
- [Azure SDKs for Python](https://azure.github.io/azure-sdk-for-python/index.html)
- [Google Cloud Client Libraries](https://cloud.google.com/python/docs/reference/)
- [vSphere Automation SDK](https://github.com/vmware/vsphere-automation-sdk-python)
- [VMware ESXi/vSphere API Python Bindings](https://github.com/vmware/pyvmomi)
- For Hyper-V: [pywinrm](https://github.com/diyan/pywinrm) WinRM client
- For Hyper-V: [pypsrp](https://github.com/jborean93/pypsrp) PowerShell Remoting

[libvirt]: https://www.libvirt.org/docs/libvirt-appdev-guide-python/en-US/html/

Notes:

- For the most part, your cloud provider or hypervisor likely has a Python SDK!

---

For container management

- [docker](https://docker-py.readthedocs.io/)
- [podman](https://github.com/containers/podman-py) (if using socket)
- [kubernetes](https://github.com/kubernetes-client/python)

Notes:

- podman package is for using the API through the podman socket

---

Thank you <!-- .element: class="r-fit-text" -->
