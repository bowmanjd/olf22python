Python: the Multi-tool for System Management <!-- .element: class="r-fit-text" -->

![Python Swiss-army knife](/assets/python-tool-o.svg) <!-- .element: class="r-stretch" style="height: 50vh" -->

Notes:

- Welcome
- Introduce myself

---

Learn, customize, tear down, build

[![Commodore 64](/assets/c64.gif)<!-- .element: style="height: 40vh" -->][c64] 

[c64]: https://en.wikipedia.org/wiki/Commodore_64

Notes:

- My digital history began with the Commodore 64
- That  1 Mhz computer became a place to experiment, learn, customize, build, tear down, build again.
- From Commodore BASIC 2.0...

---

<!-- .slide: data-background-image="/assets/pyrepl.gif"  -->

Notes:

- To Python!
- Approachable
- Powerful
- Available
- The REPL: a place to experiment, build, tear down, build again
- No production filesystems were harmed in the making of this slide deck

---

<!-- .slide: data-background-image="/assets/oldrag.jpg" -->

![Tux the Linux penguin](/assets/tux.svg) <!-- .element: class="fragment fade-up" -->

Notes:
- The path isn't so much a progression with Python as the goal, but a journey through open source and Linux, and encountering opportunities to help others
- Story of encountering Linux and open source -- an open and inviting landscape
- (With some recommended sites to see)
- Quickly learned that in open source there were many opportunities to help others, offering freely available tools, and my assistance in configuring and using these tools. Such as Linux servers, web application frameworks

---

<!-- .slide: data-background-image="/assets/holding-hands.svg" data-background-size="85%" -->

Notes:
- I have a hunch that I am not the only one here with the underlying motivation to share and to help
- But this noble adventure is not without its difficulties, right?

---

Hindered by tasks that are

- taking too much time
- hard to remember
- prone to human error

Notes:

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

- Both Bash and Ansible can automate tedious tasks. Ansible is more readable and shareable. A Bash script has less guardrails, and is useful for more than just configuration management.
- I think Python occupies a middle place between these two. It can be used to do anything Ansible does and it can do anything Bash does, but unlike either of these, it is a general-purpose programming language with a multi-faceted ecosystem.
- None of these are the right tool for __every__ job. There are always going to be tasks that are best with one or the other, or something else entirely

---

Use Python when:
- Bash scripts are too large, complicated
- Complex string, array, or data processing is needed
- the target machine lacks the required commands
- Ansible is too heavy, slow, simple, or unavailable
- cross-platform is desirable

[An informative debate about the merits of Bash vs. Python on Stackoverflow](https://stackoverflow.com/questions/2424921/python-vs-bash-in-which-kind-of-tasks-each-one-outruns-the-other-performance-w)

Notes:

Keep in mind: Python works well with Bash and with Ansible. This isn't an either/or choice

---

Why Python (and not other general-purpose languages)?

It isn't a competition; collect them all! <!-- .element class="fragment fade-in" -->

---

"The Python space is beautiful, and great, and big"

Lorena Mesa, Engineer at GitHub, former chair of Python Software Foundation <!-- .element class="fragment fade-in" -->

---

"I came for the language, I stay for the community."

Brett Cannon, Dev lead on the Python extension for Visual Studio Code <!-- .element class="fragment fade-in" -->

---

"batteries included"

![Battery](/assets/battery.svg)

---

Getting started with Python

Lots of good documentation. Here are a few...

---

[![Automate the Boring Stuff](/assets/AutomatetheBoringStuff_cover.png)][boring]

[boring]: https://automatetheboringstuff.com/

---

[![Django Girls](/assets/djangogirls.png)][djangogirls]

[djangogirls]: https://tutorial.djangogirls.org/en/

---

[![Python](/assets/python-logo.svg)][pythondocs]

[pythondocs]: https://docs.python.org/3/

---

[![Awesome Python cap](/assets/cap.svg) <!-- .element style="height: 10vh" -->][awesomepython] <br>
[Awesome Python][awesomepython]</br>
List

[awesomepython]: https://awesome-python.com/

---

![Python help command](/assets/pyhelp1.gif)

---

<!-- .slide: data-background-image="/assets/pyhelp.gif"  -->

---

Installing Python

---

<!-- .slide: data-background-image="https://imgs.xkcd.com/comics/python_environment.png" data-background-size="contain"  -->

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
- Linux package repos typically label python as python3, and python is launched as `python3` although most distros have ways of making `python` launch python3, such as python-is-python3 (Ubuntu), pythonispython3 (Alpine), python-unversioned-command (Fedora)
- Other Operating Systems you may have heard of: scoop/chocolatey/winget/Store for Windows, homebrew for MacOS

---

Python REPL on the web:

- [pythonanywhere.com](https://www.pythonanywhere.com/)
- [python.org/shell](https://www.python.org/shell/)
- [github.com/codespaces](https://github.com/codespaces/)
- [repl.it/languages/python3](https://replit.com/new/python3)
- [paiza.cloud](https://paiza.cloud/)
- [c9.io](https://aws.amazon.com/cloud9/)

Notes:
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

---

Python editors

- [VSCode](https://code.visualstudio.com/)
- [PyCharm](https://www.jetbrains.com/pycharm/)
- Vim/Neovim, Emacs, Zed, Helix
- For beginners: [Thonny](https://thonny.org/), [Mu](https://codewith.mu/)

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

```python [1-8|1|2|3|4|5|6|7|8|1-8]
a_number = 12
another_number = 7.1
a_string = "Some text"
another_string = "Some more text"
a_range = range(10)
some_bytes = b"\x00\x01\x02\x03Hi"
a_list = ["Some text", 14, another_number, "你好", 1]
a_lonely_number = a_list[4]
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

The same, but with shell mode

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

output = subprocess.check_output("ip addr",
                                  shell=True,
                                  text=True)

print(output)

```

---

A shortcut with `subprocess.check_call` if output capture is not needed

```python
import subprocess

subprocess.check_call("ip addr", shell=True)
```

---

Summary:
- `subprocess.run` for anything and everything
- `subprocess.check_output` for convenience, capturing output
- `subprocess.check_call` if execution is all that is needed
- `shell=True` parameter will pass the whole command as string to `sh` otherwise pass the command as a `["list", "of", "command", "and", "parameters"]`

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

---

[libvirt]: https://www.libvirt.org/docs/libvirt-appdev-guide-python/en-US/html/
[shlex]: https://docs.python.org/3/library/shlex.html
