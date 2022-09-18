import shutil
import argparse
import datetime
import subprocess

from typing import *
from pathlib import Path

from colorama import init, Fore

TO_LOCAL = 0
TO_REMOTE = 1

home_folder = Path(__file__).resolve().home()
local_config_folder = home_folder.joinpath(".config")
remote_config_folder = Path(__file__).resolve().parent.joinpath(".config")

init(autoreset=True)

class MyUbuntu:
    my_config: List[Callable] = []

    def __init__(self) -> None:
        pass

    def __call__(self, func: Callable) -> None:
        self.my_config.append(func)
    
    def _compress(self) -> bool:
        password = input("Please enter encrypt password: ")
        zipfile_name = remote_config_folder.parent.relative_to(
            Path(__file__).resolve().parent
        ) / '.config.zip'
        result1 = subprocess.Popen(
            args=f"zip --password {password} -r {zipfile_name} {remote_config_folder}", 
            shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
        )
        text = result1.communicate()[0]
        if result1.returncode == 0:
            result2 = subprocess.Popen(
                args=f"rm -r {remote_config_folder}",
                shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
            )
            text = result2.communicate()[0]
            if result2.returncode == 0:
                return True
        return False

    def _extract(self) -> bool:
        password = input("Please enter encrypt password: ")
        zipfile = remote_config_folder.parent / '.config.zip'
        result1 = subprocess.Popen(
            args=f"unzip -P {password} {zipfile}",
            shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
        )
        text = result1.communicate()[0]
        if result1.returncode == 0:
            project_root_folder = Path(__file__).resolve().parent
            result2 = subprocess.Popen(
                args=f"mv {project_root_folder}{project_root_folder}/.config -b {project_root_folder}",
                shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
            )
            text = result2.communicate()[0]
            if result2.returncode == 0:
                result3 = subprocess.Popen(
                    f"rm -r {project_root_folder}/home {zipfile}",
                    shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
                )
                text = result3.communicate()[0]
                if result3.returncode == 0:
                    result4 = subprocess.Popen(
                        args=f"rm -r {project_root_folder}/.config~",
                        shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
                    )
                    text = result4.communicate()[0]
                    return True
        return False

    def copy_to_local(self):
        assert self._extract(), f"{Fore.RED}extract not fully functioned!"
        for func in self.my_config:
            print(f"{Fore.MAGENTA}{func.__name__}...")
            func(TO_LOCAL)
    
    def copy_to_remote(self):
        for func in self.my_config:
            print(f"{Fore.MAGENTA}{func.__name__}...")
            func(TO_REMOTE)
        assert self._compress(), f"{Fore.RED}Compress not fully functioned!"


jack_ubuntu = MyUbuntu()


@jack_ubuntu
def typora(mode: int) -> None:
    local_path = local_config_folder.joinpath("Typora/conf/conf.user.json")
    remote_path = remote_config_folder.joinpath("Typora/conf/conf.user.json")
    if mode == TO_LOCAL:
        if not local_path.exists():
            local_path.parent.mkdir(parents=True, exist_ok=True)
            print(f"{Fore.YELLOW}local path not exists, creating...")
        else:
            new_path = local_path.rename(f"{local_path}-{datetime.datetime.now()}")
            print(f"{Fore.YELLOW}{local_path} exists, rename to {new_path}")
        shutil.copyfile(str(remote_path), str(local_path))
        print(f"{Fore.GREEN}Successfully copied local typora config")
    if mode == TO_REMOTE:
        if remote_path.exists():
            new_path = remote_path.rename(f"{remote_path}-{datetime.datetime.now()}")
            print(f"{Fore.YELLOW}{remote_path} exists, rename to {new_path}")
        else:
            remote_path.parent.mkdir(parents=True, exist_ok=True)
            print(f"{Fore.YELLOW}{remote_path.parent} not exists, creating...")
        shutil.copyfile(str(local_path), str(remote_path))
        print(f"{Fore.GREEN}Successfully copied local typora config")


@jack_ubuntu
def picogo(mode: int) -> None:
    local_path = home_folder.joinpath(".picgo/config.json")
    remote_path = remote_config_folder.joinpath(".picgo/config.json")
    if mode == TO_LOCAL:
        if not local_path.exists():
            local_path.parent.mkdir(parents=True, exist_ok=True)
            print(f"{Fore.YELLOW}local path not exists, creating...")
        else:
            new_path = local_path.rename(f"{local_path}-{datetime.datetime.now()}")
            print(f"{Fore.YELLOW}{local_path} exists, rename to {new_path}")
        shutil.copyfile(str(remote_path), str(local_path))
        print(f"{Fore.GREEN}Successfully copied local typora config")
    if mode == TO_REMOTE:
        if remote_path.exists():
            new_path = remote_path.rename(f"{remote_path}-{datetime.datetime.now()}")
            print(f"{Fore.YELLOW}{remote_path} exists, rename to {new_path}")
        else:
            remote_path.parent.mkdir(parents=True, exist_ok=True)
            print(f"{Fore.YELLOW}{remote_path.parent} not exists, creating...")
        shutil.copyfile(str(local_path), str(remote_path))
        print(f"{Fore.GREEN}Successfully copied local typora config")


@jack_ubuntu
def synth_shell(mode: int) -> None:
    local_path = local_config_folder.joinpath("synth-shell/synth-shell-prompt.config")
    remote_path = remote_config_folder.joinpath("synth-shell/synth-shell-prompt.config")
    if mode == TO_LOCAL:
        if not local_path.exists():
            local_path.parent.mkdir(parents=True, exist_ok=True)
            print(f"{Fore.YELLOW}local path not exists, creating...")
        else:
            new_path = local_path.rename(f"{local_path}-{datetime.datetime.now()}")
            print(f"{Fore.YELLOW}{local_path} exists, rename to {new_path}")
        shutil.copyfile(str(remote_path), str(local_path))
        print(f"{Fore.GREEN}Successfully copied local typora config")
    if mode == TO_REMOTE:
        if remote_path.exists():
            new_path = remote_path.rename(f"{remote_path}-{datetime.datetime.now()}")
            print(f"{Fore.YELLOW}{remote_path} exists, rename to {new_path}")
        else:
            remote_path.parent.mkdir(parents=True, exist_ok=True)
            print(f"{Fore.YELLOW}{remote_path.parent} not exists, creating...")
        shutil.copyfile(str(local_path), str(remote_path))
        print(f"{Fore.GREEN}Successfully copied local typora config")


@jack_ubuntu
def terminator(mode: int) -> None:
    local_path = local_config_folder.joinpath("terminator/config")
    remote_path = remote_config_folder.joinpath("terminator/config")
    if mode == TO_LOCAL:
        if not local_path.exists():
            local_path.parent.mkdir(parents=True, exist_ok=True)
            print(f"{Fore.YELLOW}local path not exists, creating...")
        else:
            new_path = local_path.rename(f"{local_path}-{datetime.datetime.now()}")
            print(f"{Fore.YELLOW}{local_path} exists, rename to {new_path}")
        shutil.copyfile(str(remote_path), str(local_path))
        print(f"{Fore.GREEN}Successfully copied local typora config")
    if mode == TO_REMOTE:
        if remote_path.exists():
            new_path = remote_path.rename(f"{remote_path}-{datetime.datetime.now()}")
            print(f"{Fore.YELLOW}{remote_path} exists, rename to {new_path}")
        else:
            remote_path.parent.mkdir(parents=True, exist_ok=True)
            print(f"{Fore.YELLOW}{remote_path.parent} not exists, creating...")
        shutil.copyfile(str(local_path), str(remote_path))
        print(f"{Fore.GREEN}Successfully copied local typora config")


@jack_ubuntu
def lunarvim(mode: int) -> None:
    local_path = local_config_folder.joinpath("lvim/config.lua")
    remote_path = remote_config_folder.joinpath("lvim/config.lua")
    if mode == TO_LOCAL:
        if not local_path.exists():
            local_path.parent.mkdir(parents=True, exist_ok=True)
            print(f"{Fore.YELLOW}local path not exists, creating...")
        else:
            new_path = local_path.rename(f"{local_path}-{datetime.datetime.now()}")
            print(f"{Fore.YELLOW}{local_path} exists, rename to {new_path}")
        shutil.copyfile(str(remote_path), str(local_path))
        print(f"{Fore.GREEN}Successfully copied local typora config")
    if mode == TO_REMOTE:
        if remote_path.exists():
            new_path = remote_path.rename(f"{remote_path}-{datetime.datetime.now()}")
            print(f"{Fore.YELLOW}{remote_path} exists, rename to {new_path}")
        else:
            remote_path.parent.mkdir(parents=True, exist_ok=True)
            print(f"{Fore.YELLOW}{remote_path.parent} not exists, creating...")
        shutil.copyfile(str(local_path), str(remote_path))
        print(f"{Fore.GREEN}Successfully copied local typora config")


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=f"{Fore.GREEN}A python script used for quickly clone configurations on a new Ubuntu{Fore.RESET}")
    parser.add_argument(
        "-s", "--sync",
        action="store_true", dest="sync",
        help=f"{Fore.YELLOW}sync configuration on this Ubuntu{Fore.RESET}")
    parser.add_argument(
        "-u", "--update", 
        action="store_true", dest="update",
        help=f"{Fore.YELLOW}update configuration using configuration on this Ubuntu{Fore.RESET}")
    return parser.parse_args()


def main(args: argparse.Namespace):
    assert not (args.sync and args.update), f"{Fore.RED}Conflict command! Can only be either sync or update!"
    if args.sync:
        jack_ubuntu.copy_to_local()
    elif args.update:
        jack_ubuntu.copy_to_remote()
    else:
        print(f"{Fore.GREEN}Nothing happened, use -h to see valid options, see you!")


if __name__ == "__main__":
    # jack_ubuntu.copy_to_remote()
    # jack_ubuntu.copy_to_local()
    main(get_args())