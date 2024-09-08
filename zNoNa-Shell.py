import os
import psutil
import socket
import shutil
import webbrowser
import time
import platform
import subprocess
from colorama import *

init(autoreset=True)

login = os.getlogin()
hostname = socket.gethostname()

# get path
def cwd():
    return os.getcwd()

path = cwd()

prompt = f"""{Style.BRIGHT + Fore.BLUE + hostname + Fore.WHITE}@{Fore.BLUE + login + Fore.WHITE}:{Fore.CYAN + path + Fore.BLUE + Fore.RED}$ {Style.RESET_ALL}"""

def zNoNa(): # zNoNa shell 
    print(f"""{Style.BRIGHT}
{Fore.CYAN}+———————————————————————————————————————————————+
{Fore.CYAN}| {Fore.WHITE}zNoNa-Shell           v-0.1                   {Fore.CYAN}|
{Fore.CYAN}| {Fore.BLUE}shell {Fore.WHITE}by {Fore.RED}Lunar {Fore.WHITE}/ discord : aa_aaaa_bbb_bbbbb  {Fore.CYAN}|
{Fore.CYAN}| {Fore.WHITE}type 'help' for more assistance               {Fore.CYAN}|
{Fore.CYAN}| {Fore.WHITE}© zNoNa-Shell                                 {Fore.CYAN}|
{Fore.CYAN}+———————————————————————————————————————————————+
{Style.RESET_ALL}""")

    while True:

        try: 
            Input = input(prompt)
            
            # ________________________________ #

            if Input == "":
                pass 

            # ________________________________ #

            elif Input == "break":
                break # break the loop 

            # ________________________________ #

            elif Input == "exit":
                exit() # exit

            # ________________________________ #

            elif Input == "clear":
                clear()

            # ________________________________ #

            elif Input == "help":
                help()

            # ________________________________ #

            elif Input == "whoami":
                whoami()

            # ________________________________ #

            elif Input.startswith("say "):
                parts = Input.split(" ", 1)
                Inputsay = parts[1]
                say(Inputsay)

            # ________________________________ #      

            elif Input == "ls":
                ls()

            # ________________________________ #      

            elif Input.startswith("cd "):
                parts = Input.split(" ", 1)
                if len(parts) == 2:
                    cd(parts[1])

            # ________________________________ #

            elif Input.startswith("mkdir "):
                parts = Input.split(" ", 1)
                Inputmkdir = parts[1]
                mkdir(Inputmkdir)

            # ________________________________ #

            elif Input.startswith("touch "):
                parts = Input.split(" ", 1)
                Inputtouch = parts[1]
                touch(Inputtouch)

            # ________________________________ #

            elif Input.startswith("rm "):
                parts = Input.split(" ", 1)
                Inputrm = parts[1]
                rm(Inputrm)

            # ________________________________ #

            elif Input.startswith("rmdir "):
                parts = Input.split(" ", 1)
                Inputrmdir = parts[1]
                rmdir(Inputrmdir)

            # ________________________________ #

            elif Input.startswith("cat "):
                parts = Input.split(" ", 1)
                Inputcat = parts[1]
                cat(Inputcat)

            # ________________________________ #

            elif Input.startswith("cp "):
                parts = Input.split(" ", 2)
                if len(parts) == 3:
                    Inputcpsource = parts[1]
                    Inputcpdestination = parts[2]
                    cp(Inputcpsource, Inputcpdestination)

            # ________________________________ #

            elif Input.startswith("mv "):
                parts = Input.split(" ", 2)
                if len(parts) == 3:
                    Inputmvsource = parts[1]
                    Inputmvdestination = parts[2]
                    mv(Inputmvsource, Inputmvdestination)

            # ________________________________ #

            elif Input.startswith("webopen "):
                parts = Input.split(" ", 1)
                Inputwebopen = parts[1]
                webopen(Inputwebopen)

            # ________________________________ #

            elif Input == "znonafetch":
                znonafetch()

            # ________________________________ #

            elif Input == "re":
                clear()
                zNoNa()

            # ________________________________ #

            elif Input == "ext":
                ext()

            # ________________________________ #

            elif Input == "by?":
                print(f"{Fore.CYAN + Style.BRIGHT}by?:{Style.RESET_ALL} 4c756e6172")

            # ________________________________ #
            
            else:
                print(f"{Fore.RED + Style.BRIGHT}{Input}:{Style.RESET_ALL} not recognized.")

            # ________________________________ #

        except KeyboardInterrupt:
            print(f"{Fore.RED + Style.BRIGHT}KeyboardInterrupt:{Style.RESET_ALL} ^C")

# ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————— # 
# shell cmd                                                                                                                                     #
# ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————— # 

def clear(): # cmd : clear
    os.system('cls' if os.name == 'nt' else 'clear')

def help(): # cmd : help
    print(f"""
{Style.BRIGHT}{Fore.BLUE}Category             Command    Description
{Fore.WHITE}————————————————     ————————   ————————————————————————————————————————
{Fore.GREEN}File Operations:
                     {Fore.CYAN}touch      {Fore.RED}- {Fore.YELLOW}Update the timestamp of a file
                     {Fore.CYAN}rm         {Fore.RED}- {Fore.YELLOW}Remove a file
                     {Fore.CYAN}cp         {Fore.RED}- {Fore.YELLOW}Copy a file
                     {Fore.CYAN}mv         {Fore.RED}- {Fore.YELLOW}Move a file

{Fore.GREEN}Directory Management:
                     {Fore.CYAN}cd         {Fore.RED}- {Fore.YELLOW}Change directory
                     {Fore.CYAN}ls         {Fore.RED}- {Fore.YELLOW}List directory contents
                     {Fore.CYAN}mkdir      {Fore.RED}- {Fore.YELLOW}Create a new directory
                     {Fore.CYAN}rmdir      {Fore.RED}- {Fore.YELLOW}Remove a directory

{Fore.GREEN}Screen and Shell:
                     {Fore.CYAN}clear      {Fore.RED}- {Fore.YELLOW}Clear the screen
                     {Fore.CYAN}help       {Fore.RED}- {Fore.YELLOW}Display this help message
                     {Fore.CYAN}exit       {Fore.RED}- {Fore.YELLOW}Exit the shell

{Fore.GREEN}User Information:
                     {Fore.CYAN}whoami     {Fore.RED}- {Fore.YELLOW}Display the current user

{Fore.GREEN}Control Flow:
                     {Fore.CYAN}break      {Fore.RED}- {Fore.YELLOW}Break out of the current loop

{Fore.GREEN}Miscellaneous:
                     {Fore.CYAN}say        {Fore.RED}- {Fore.YELLOW}Print a message
                     {Fore.CYAN}znonafetch {Fore.RED}- {Fore.YELLOW}Display system information (neofetch-like){Style.RESET_ALL}
""")
    
def ext(): # cmd : ext
    print(f"""
{Style.BRIGHT}{Fore.CYAN}Category             Extension 
{Fore.WHITE}————————————————     ———————— 
{Fore.CYAN}Text Files:
                     {Fore.CYAN}.txt    
                     {Fore.CYAN}.md       

{Fore.GREEN}Image Files:
                     {Fore.GREEN}.jpg     
                     {Fore.GREEN}.jpeg   
                     {Fore.GREEN}.png     
                     {Fore.GREEN}.gif     
                     {Fore.GREEN}.pdf     
                     {Fore.GREEN}.raw      
{Fore.MAGENTA}Web Files:
                     {Fore.MAGENTA}.html     
                     {Fore.MAGENTA}.css       
                     {Fore.MAGENTA}.yaml    
                     {Fore.MAGENTA}.yml      

{Fore.BLUE}Programming Files:
                     {Fore.BLUE}.py     
                     {Fore.BLUE}.js     
                     {Fore.BLUE}.java      
                     {Fore.BLUE}.cpp       
                     {Fore.BLUE}.h       
                     {Fore.BLUE}.rb     
                     {Fore.BLUE}.php      
                     {Fore.BLUE}.sql    
                     {Fore.BLUE}.lua    
                     {Fore.BLUE}.pl      
                     {Fore.BLUE}.r       
                     {Fore.BLUE}.swift   
                     {Fore.BLUE}.go      
                     {Fore.BLUE}.less     
                     {Fore.BLUE}.sass    
                     {Fore.BLUE}.scss    

{Fore.YELLOW}Archive Files:
                     {Fore.YELLOW}.zip    
                     {Fore.YELLOW}.tar       
                     {Fore.YELLOW}.gz       
                     {Fore.YELLOW}.rar      

{Fore.RED}Font Files:
                     {Fore.RED}.ttf     
                     {Fore.RED}.otf       

{Fore.WHITE}Miscellaneous:
                     {Fore.WHITE}.bak      
                     {Fore.WHITE}.tmp     
                     {Fore.WHITE}.ico    
                     {Fore.WHITE}.woff    
                     {Fore.WHITE}.woff2   
                     {Fore.WHITE}.eps    
                     {Fore.WHITE}.psd     
                     {Fore.WHITE}.ai     
                     {Fore.WHITE}.tiff   
                     {Fore.WHITE}.mdx     
                     {Fore.WHITE}.pl      
                     {Fore.WHITE}.svg    
                     {Fore.WHITE}.ts       
                     {Fore.WHITE}.tsx    
{Style.RESET_ALL}""")

def whoami(): # cmd : whoami
    print(f"{Fore.GREEN + Style.BRIGHT}whoami:{Style.RESET_ALL} {hostname}@{login}")

def say(Inputsay): # cmd : say
    print(f"{Fore.GREEN + Style.BRIGHT}say:{Style.RESET_ALL} {Inputsay}")

def colorls(filename):
    extcolor = {
        '.txt': Fore.CYAN,
        '.md': Fore.CYAN,
        '.jpg': Fore.GREEN,
        '.jpeg': Fore.GREEN,
        '.png': Fore.GREEN,
        '.gif': Fore.GREEN,
        '.pdf': Fore.GREEN,
        '.raw': Fore.GREEN,
        '.html': Fore.MAGENTA,
        '.css': Fore.MAGENTA,
        '.yaml': Fore.MAGENTA,
        '.yml': Fore.MAGENTA,
        '.py': Fore.BLUE,
        '.js': Fore.BLUE,
        '.java': Fore.BLUE,
        '.cpp': Fore.BLUE,
        '.h': Fore.BLUE,
        '.rb': Fore.BLUE,
        '.php': Fore.BLUE,
        '.sql': Fore.BLUE,
        '.lua': Fore.BLUE,
        '.pl': Fore.BLUE,
        '.r': Fore.BLUE,
        '.swift': Fore.BLUE,
        '.go': Fore.BLUE,
        '.less': Fore.BLUE,
        '.sass': Fore.BLUE,
        '.scss': Fore.BLUE,
        '.zip': Fore.YELLOW,
        '.tar': Fore.YELLOW,
        '.gz': Fore.YELLOW,
        '.rar': Fore.YELLOW,
        '.ttf': Fore.RED,
        '.otf': Fore.RED,
        '.bak': Fore.WHITE,
        '.tmp': Fore.WHITE,
        '.ico': Fore.WHITE,
        '.woff': Fore.WHITE,
        '.woff2': Fore.WHITE,
        '.eps': Fore.WHITE,
        '.psd': Fore.WHITE,
        '.ai': Fore.WHITE,
        '.tiff': Fore.WHITE,
        '.mdx': Fore.WHITE,
        '.pl': Fore.WHITE,
        '.svg': Fore.WHITE,
        '.ts': Fore.WHITE,
        '.tsx': Fore.WHITE
    }
    
    _, ext = os.path.splitext(filename)
    return extcolor.get(ext, Fore.BLUE)

def ls(): # cmd : ls
    cwd = os.getcwd()
    items = os.listdir(cwd)
    mlength = max(len(item) for item in items)
    ncolumns = max(1, os.get_terminal_size().columns // (mlength + 4)) 

    items.sort()
    
    for i in range(0, len(items), ncolumns):
        rowi = items[i:i + ncolumns]
        row = ''
        for item in rowi:
            ipath = os.path.join(cwd, item)
            if os.path.isdir(ipath):
                row += f"{Style.BRIGHT + Back.LIGHTBLACK_EX + item + Style.RESET_ALL}/ {(' ' * (mlength - len(item)))}"
            else:
                row += f"{Style.BRIGHT + colorls(item) + item.ljust(mlength + 2) + Style.RESET_ALL}"
        print(row)

def cd(path): # cmd : cd
    try:
        os.chdir(path)
        global prompt
        prompt = f"""{Style.BRIGHT + Fore.BLUE + hostname + Fore.WHITE}@{Fore.BLUE + login + Fore.WHITE}:{Fore.CYAN + os.getcwd() + Fore.BLUE + Fore.RED}$ {Style.RESET_ALL}"""
    except FileNotFoundError:
        print(f"{Fore.RED + Style.BRIGHT}cd: {Style.RESET_ALL}No such file or directory '{path}'")
    except PermissionError:
        print(f"{Fore.RED + Style.BRIGHT}cd: {Style.RESET_ALL}Permission denied '{path}'")
    except NotADirectoryError:
        print(f"{Fore.RED + Style.BRIGHT}cd: {Style.RESET_ALL}Not a directory '{path}'")
    except OSError as e:
        print(f"{Fore.RED + Style.BRIGHT}cd: {Style.RESET_ALL}OS error: {e}")
    except Exception as e:
        print(f"{Fore.RED + Style.BRIGHT}cd: {Style.RESET_ALL}Unexpected error: {e}")

def mkdir(Inputmkdir): # cmd : mkdir 
    try:
        os.mkdir(Inputmkdir)
        print(f"{Fore.GREEN + Style.BRIGHT}mkdir: {Style.RESET_ALL}Directory '{Inputmkdir}' created successfully")
    except FileExistsError:
        print(f"{Fore.RED + Style.BRIGHT}mkdir: {Style.RESET_ALL}Directory '{Inputmkdir}' already exists")
    except PermissionError:
        print(f"{Fore.RED + Style.BRIGHT}mkdir: {Style.RESET_ALL}Permission denied to create directory '{Inputmkdir}'")
    except FileNotFoundError:
        print(f"{Fore.RED + Style.BRIGHT}mkdir: {Style.RESET_ALL}Invalid path '{Inputmkdir}'")
    except OSError as e:
        print(f"{Fore.RED + Style.BRIGHT}mkdir: {Style.RESET_ALL}Error creating directory '{Inputmkdir}': {e}")
    except Exception as e:
        print(f"{Fore.RED + Style.BRIGHT}mkdir: {Style.RESET_ALL}Unexpected error: {e}")

def touch(Inputtouch): # cmd : touch 
    try:
        with open(Inputtouch, 'a'):
            os.utime(Inputtouch, None)
        print(f"{Fore.GREEN + Style.BRIGHT}touch: {Style.RESET_ALL}File '{Inputtouch}' touched successfully")
    except PermissionError:
        print(f"{Fore.RED + Style.BRIGHT}touch: {Style.RESET_ALL}Permission denied to create or update file '{Inputtouch}'")
    except FileNotFoundError:
        print(f"{Fore.RED + Style.BRIGHT}touch: {Style.RESET_ALL}File or directory not found '{Inputtouch}'")
    except OSError as e:
        print(f"{Fore.RED + Style.BRIGHT}touch: {Style.RESET_ALL}OS error creating or updating file '{Inputtouch}': {e}")
    except Exception as e:
        print(f"{Fore.RED + Style.BRIGHT}touch: {Style.RESET_ALL}Unexpected error: {e}")

def rm(Inputrm): # cmd : rm
    try:
        os.remove(Inputrm)
        print(f"{Fore.GREEN + Style.BRIGHT}rm: {Style.RESET_ALL}File '{Inputrm}' removed successfully")
    except FileNotFoundError:
        print(f"{Fore.RED + Style.BRIGHT}rm: {Style.RESET_ALL}No such file '{Inputrm}'")
    except PermissionError:
        print(f"{Fore.RED + Style.BRIGHT}rm: {Style.RESET_ALL}Permission denied to remove file '{Inputrm}'")
    except OSError as e:
        print(f"{Fore.RED + Style.BRIGHT}rm: {Style.RESET_ALL}OS error removing file '{Inputrm}': {e}")
    except Exception as e:
        print(f"{Fore.RED + Style.BRIGHT}rm: {Style.RESET_ALL}Unexpected error: {e}")

def rmdir(Inputrmdir): # cmd : rmdir
    try:
        if not os.listdir(Inputrmdir):
            os.rmdir(Inputrmdir)
            print(f"{Fore.GREEN + Style.BRIGHT}rmdir: {Style.RESET_ALL}Directory '{Inputrmdir}' removed successfully")
        else:
            print(f"{Fore.RED + Style.BRIGHT}rmdir: {Style.RESET_ALL}Directory '{Inputrmdir}' is not empty")
    except FileNotFoundError:
        print(f"{Fore.RED + Style.BRIGHT}rmdir: {Style.RESET_ALL}No such directory '{Inputrmdir}'")
    except PermissionError:
        print(f"{Fore.RED + Style.BRIGHT}rmdir: {Style.RESET_ALL}Permission denied to remove directory '{Inputrmdir}'")
    except OSError as e:
        print(f"{Fore.RED + Style.BRIGHT}rmdir: {Style.RESET_ALL}Error removing directory '{Inputrmdir}': {e}")
    except Exception as e:
        print(f"{Fore.RED + Style.BRIGHT}rmdir: {Style.RESET_ALL}Unexpected error: {e}")

def cat(Inputcat): # cmd : cat
    try:
        with open(Inputcat, 'r') as f:
            content = f.read()
            print(f"{Fore.GREEN + Style.BRIGHT}cat: {Style.RESET_ALL}\n{content}")
    except FileNotFoundError:
        print(f"{Fore.RED + Style.BRIGHT}cat: {Style.RESET_ALL}No such file '{Inputcat}'")
    except PermissionError:
        print(f"{Fore.RED + Style.BRIGHT}cat: {Style.RESET_ALL}Permission denied to read file '{Inputcat}'")
    except IsADirectoryError:
        print(f"{Fore.RED + Style.BRIGHT}cat: {Style.RESET_ALL}'{Inputcat}' is a directory, not a file")
    except Exception as e:
        print(f"{Fore.RED + Style.BRIGHT}cat: {Style.RESET_ALL}Unexpected error reading file '{Inputcat}': {e}")

def mv(Inputmvsource, Inputmvdestination): # cmd : mv
    try:
        shutil.move(Inputmvsource, Inputmvdestination)
        print(f"{Fore.GREEN}mv: {Style.RESET_ALL}File moved from '{Inputmvsource}' to '{Inputmvdestination}'")
    except FileNotFoundError:
        print(f"{Fore.RED}mv: {Style.RESET_ALL}No such file '{Inputmvsource}'")
    except PermissionError:
        print(f"{Fore.RED}mv: {Style.RESET_ALL}Permission denied to move file from '{Inputmvsource}' to '{Inputmvdestination}'")
    except shutil.Error as e:
        print(f"{Fore.RED}mv: {Style.RESET_ALL}Shutil error: {e}")
    except Exception as e:
        print(f"{Fore.RED}mv: {Style.RESET_ALL}Unexpected error: {e}")

def cp(Inputcpsource, Inputcpdestination): # cmd : cp
    try:
        shutil.copy(Inputcpsource, Inputcpdestination)
        print(f"{Fore.GREEN}cp: {Style.RESET_ALL}File '{Inputcpsource}' copied to '{Inputcpdestination}'")
    except FileNotFoundError:
        print(f"{Fore.RED}cp: {Style.RESET_ALL}No such file '{Inputcpsource}'")
    except PermissionError:
        print(f"{Fore.RED}cp: {Style.RESET_ALL}Permission denied to copy file from '{Inputcpsource}' to '{Inputcpdestination}'")
    except shutil.SameFileError:
        print(f"{Fore.RED}cp: {Style.RESET_ALL}Source and destination are the same file '{Inputcpsource}'")
    except OSError as e:
        print(f"{Fore.RED}cp: {Style.RESET_ALL}OS error: {e}")
    except Exception as e:
        print(f"{Fore.RED}cp: {Style.RESET_ALL}Unexpected error: {e}")

def webopen(Inputwebopen): # cmd : webopen
    try:
        if not Inputwebopen.startswith(("http://", "https://")):
            Inputwebopen = "http://" + Inputwebopen
        webbrowser.open(Inputwebopen)
        print(f"{Fore.GREEN}webopen: {Style.RESET_ALL}Opening '{Inputwebopen}' in the browser")

    except ValueError as e:
        print(f"{Fore.RED}webopen: {Style.RESET_ALL}Invalid URL '{Inputwebopen}': {e}")
    except Exception as e:
        print(f"{Fore.RED}webopen: {Style.RESET_ALL}Unexpected error: {e}")

def znonafetch(): # cmd : znonafetch
    info = get1()
    os = info['OS']
    kernel = info['Kernel']
    uptime = info['Uptime']
    cpu = info['CPU']
    ram = info['RAM']
    resolution = info['Resolution']
    packages = info['Packages']
    de = info['DE']
    theme = info['Theme']
    pyversion = info['Python Version']
    cpucores = info['CPU Cores']
    logicalcores = info['Logical Cores']
    cputemp = info['CPU Temperature'] if 'CPU Temperature' in info else 'N/A'
    iplocal = info['IP Local']

    znona = [
        f""
        f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}       :---         ---",
        f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}      -=++=-       =+++=",
        f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}      -*##*+=======+*#*=",
        f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}      =*######*########+=",
        f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}     ==*##%%%%%%%%%%##*=++",
        f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}     ++#%%%%%%%%%%%%%##+++                  {Fore.BLUE}{hostname}{Fore.WHITE}@{Fore.LIGHTYELLOW_EX}{login}{Fore.LIGHTBLACK_EX}",
        f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}     +*%%%%%%%%%%%%%%##*+                   {Fore.WHITE}——————————————————————————",                 
        f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}     *#%%#{Fore.BLUE}+*{Fore.LIGHTBLACK_EX}#%%%#{Fore.LIGHTYELLOW_EX}**{Fore.LIGHTBLACK_EX}+###*+                   {Fore.BLUE}OS {Fore.WHITE}: {Fore.LIGHTYELLOW_EX}{os}{Fore.LIGHTBLACK_EX}",
        f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}    +*#%%%%%%%%%%%%%%##**+                  {Fore.BLUE}Kernel {Fore.WHITE}: {Fore.LIGHTYELLOW_EX}{kernel}{Fore.LIGHTBLACK_EX}",
        f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}    +*#%%%%%%%%%%%%%%%#**+                  {Fore.BLUE}Uptime {Fore.WHITE}: {Fore.LIGHTYELLOW_EX}{uptime}{Fore.LIGHTBLACK_EX}",
        f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}    ++#%%%%%%%%%%%%%%%##+++                 {Fore.BLUE}DE {Fore.WHITE}: {Fore.LIGHTYELLOW_EX}{de}{Fore.LIGHTBLACK_EX}",
        f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}    ++#%%%%%%%%%%%%%%%##*+                  {Fore.BLUE}RAM {Fore.WHITE}: {Fore.LIGHTYELLOW_EX}{ram}{Fore.LIGHTBLACK_EX}",
        f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}    +*#%%%%%%%%%%%%%%%%#*+                  {Fore.BLUE}Resolution {Fore.WHITE}: {Fore.LIGHTYELLOW_EX}{resolution}{Fore.LIGHTBLACK_EX}",
        f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}    +*%%%@@@@@@@@@%%%%%#**       --=++++==  {Fore.BLUE}Packages {Fore.WHITE}: {Fore.LIGHTYELLOW_EX}{packages}{Fore.LIGHTBLACK_EX}",
        f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}   **#%%@@@@@@@@@@%%%%%%#*       =*##%#     {Fore.BLUE}Theme {Fore.WHITE}: {Fore.LIGHTYELLOW_EX}{theme}{Fore.LIGHTBLACK_EX}",
        f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}  **%%%@@@@@@@@@@%%%%%%#***   -+*#%%#       {Fore.BLUE}Python Version {Fore.WHITE}: {Fore.LIGHTYELLOW_EX}{pyversion}{Fore.LIGHTBLACK_EX}",
        f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}  *#%%%@@@@@@@@@@%%%%%%%#*    +*#%%%        {Fore.BLUE}IP Local {Fore.WHITE}: {Fore.LIGHTYELLOW_EX}{iplocal}{Fore.LIGHTBLACK_EX}",
        f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}  *##%%%@@@@@@@@@@@@@%%%%#**   +#%%%#       {Fore.BLUE}CPU Cores {Fore.WHITE}: {Fore.LIGHTYELLOW_EX}{cpucores}{Fore.LIGHTBLACK_EX}",
        f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}  *#%%%%@@@@@@@@@@@@@@%%%#*** +*%%%%#       {Fore.BLUE}Logical Cores {Fore.WHITE}: {Fore.LIGHTYELLOW_EX}{logicalcores}{Fore.LIGHTBLACK_EX}",
        f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}  ##%%%%@@@@@@@@@@@@@@%%%%##  *#%%%%%       {Fore.BLUE}CPU Temperature {Fore.WHITE}: {Fore.LIGHTYELLOW_EX}{cputemp}{Fore.LIGHTBLACK_EX}",
        f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}  ##%%%%@@@@@@@@@@@@@@%%%%%##*#%%%%%",
        f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX} ##%%%%@@@@@@@@@@@@@@@@%%%%#**#%%%%%",
        f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX} ##%%%@@@@@@@@@@@@@@@@@@%%%%*#%%%%%",
        f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX} ##%%@@@@@@@@@@@@@@@@@@@@@%%#%%%%%",
        f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX} %%%@@@@@@@@@@@@@@@@@@@@@@@%%%%%%",
        f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}  %%@@@@@@@@@@@@@@@@@@@@@@@@@@@",
        f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}  %@@@@@@@@@@@@@@@@@@@@@@@@@@",
        f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}      @@@@@@@@@@@@@",
        f""
    ]
    for l in znona:
        print(l)
        time.sleep(0.02)

def get1():
    info = {
        'OS': platform.system() + " " + platform.version(),
        'Host': platform.node(),
        'Kernel': platform.release(),
        'Uptime': f"{int(psutil.boot_time() - psutil.time.time()) // 3600} hours, {((int(psutil.boot_time() - psutil.time.time()) % 3600) // 60)} mins",
        'Packages': 'N/A',  
        'Shell': subprocess.getoutput('echo %SHELL%').split('\\')[-1],  
        'Resolution': get3(),  
        'DE': 'N/A',  
        'Theme': 'N/A', 
        'CPU': get4(),  
        'RAM': f"{get2(psutil.virtual_memory().total)} / {get2(psutil.virtual_memory().available)}",
        'Python Version': platform.python_version(),
        'Disk Info': get5(),
        'CPU Cores': psutil.cpu_count(logical=False),
        'Logical Cores': psutil.cpu_count(logical=True),
        'CPU Temperature': get6(),
        'IP Local': get7()
    }
    return info

def get2(bytes):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024:
            return f"{bytes:.2f} {unit}"
        bytes /= 1024
    return f"{bytes:.2f} PB"

def get3():
    try:
        output = subprocess.check_output('wmic desktopmonitor get screenwidth,screenheight', text=True)
        lines = output.strip().split('\n')
        if len(lines) > 1:
            width, height = lines[1].split()
            return f"{width}x{height}"
    except Exception:
        return 'N/A'

def get4():
    try:
        output = subprocess.check_output('wmic cpu get caption', text=True)
        lines = output.strip().split('\n')
        if len(lines) > 1:
            return lines[1].strip()
    except Exception:
        return 'N/A'

def get5():
    partitions = psutil.disk_partitions()
    disk_info = ""
    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            total = get2(usage.total)
            used = get2(usage.used)
            free = get2(usage.free)
            disk_info += f"  {partition.device} {Fore.WHITE}| {Fore.GREEN}{total}{Fore.WHITE} | {Fore.RED}{used}{Fore.WHITE} | {Fore.LIGHTGREEN_EX}{free}{Fore.LIGHTBLACK_EX}\n"
        except PermissionError:
            continue
    return disk_info

def get6():
    try:
        temp = psutil.sensors_temperatures()
        if 'coretemp' in temp:
            return f"{temp['coretemp'][0].current} °C"
        return 'N/A'
    except Exception:
        return 'N/A'

def get7():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except Exception:
        return 'N/A'
    
if __name__ == "__main__":
    zNoNa()
