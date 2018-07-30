import pip
from subprocess import call
from pip._internal.utils.misc import get_installed_distributions

source = ""

sources = ["http://mirrors.aliyun.com/pypi/simple/","https://pypi.mirrors.ustc.edu.cn/simple/",\
"https://pypi.tuna.tsinghua.edu.cn/simple/"]

print("Please select a mirror, -1 to quit")

i = 0
for item in sources:
    print(str(i) + " " + item)
    i += 1

i = input("Please input a value:")

i = int(i)

if i < 0 and i > len(sources):
    source = " -i " + sources[i]

command = input(
    "Please input a command or do nothing*Follow with pip description:")

if command.strip() == '':
    for dist in get_installed_distributions():
        call(
            "pip install --upgrade " + dist.project_name + source,
            shell=True)
else:
    call("pip install " + command +  source, shell=True)
