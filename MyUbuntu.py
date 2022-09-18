import os
import shutil
import datetime
import subprocess

from typing import *
from pathlib import Path

TO_LOCAL = 0
TO_REMOTE = 1

home_folder = Path(__file__).resolve().home()
local_config_folder = home_folder.joinpath(".config")
remote_config_folder = Path(__file__).resolve().parent.joinpath(".config")

class MyUbuntu:
    my_config: List[Callable] = []

    def __init__(self) -> None:
        if not remote_config_folder.exists():
            remote_config_folder.mkdir(parents=True, exist_ok=True)

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
                    if result4.returncode == 0:
                        return True
        return False

    def copy_to_local(self):
        assert self._extract(), f"extract not fully functioned!"
        for func in self.my_config:
            print(f"{func.__name__}...")
            func(TO_LOCAL)
    
    def copy_to_remote(self):
        for func in self.my_config:
            print(f"{func.__name__}...")
            func(TO_REMOTE)
        assert self._compress(), "Compress not fully functioned!"


jack_ubuntu = MyUbuntu()


@jack_ubuntu
def typora(mode: int) -> None:
    local_path = local_config_folder.joinpath("Typora/conf/conf.user.json")
    remote_path = remote_config_folder.joinpath("Typora/conf/conf.user.json")
    if mode == TO_LOCAL:
        if not local_path.exists():
            local_path.parent.mkdir(parents=True, exist_ok=True)
            print("local path not exists, creating...")
        else:
            new_path = local_path.rename(f"{local_path}-{datetime.datetime.now()}")
            print(f"{local_path} exists, rename to {new_path}")
        shutil.copyfile(str(remote_path), str(local_path))
        print("Successfully copied local typora config")
    if mode == TO_REMOTE:
        if remote_path.exists():
            new_path = remote_path.rename(f"{remote_path}-{datetime.datetime.now()}")
            print(f"{remote_path} exists, rename to {new_path}")
        else:
            remote_path.parent.mkdir(parents=True, exist_ok=True)
            print(f"{remote_path.parent} not exists, creating...")
        shutil.copyfile(str(local_path), str(remote_path))
        print("Successfully copied local typora config")


@jack_ubuntu
def picogo(mode: int) -> None:
    local_path = home_folder.joinpath(".picgo/config.json")
    remote_path = remote_config_folder.joinpath(".picgo/config.json")
    if mode == TO_LOCAL:
        if not local_path.exists():
            local_path.parent.mkdir(parents=True, exist_ok=True)
            print("local path not exists, creating...")
        else:
            new_path = local_path.rename(f"{local_path}-{datetime.datetime.now()}")
            print(f"{local_path} exists, rename to {new_path}")
        shutil.copyfile(str(remote_path), str(local_path))
        print("Successfully copied local typora config")
    if mode == TO_REMOTE:
        if remote_path.exists():
            new_path = remote_path.rename(f"{remote_path}-{datetime.datetime.now()}")
            print(f"{remote_path} exists, rename to {new_path}")
        else:
            remote_path.parent.mkdir(parents=True, exist_ok=True)
            print(f"{remote_path.parent} not exists, creating...")
        shutil.copyfile(str(local_path), str(remote_path))
        print("Successfully copied local typora config")


@jack_ubuntu
def synth_shell(mode: int) -> None:
    local_path = local_config_folder.joinpath("synth-shell/synth-shell-prompt.config")
    remote_path = remote_config_folder.joinpath("synth-shell/synth-shell-prompt.config")
    if mode == TO_LOCAL:
        if not local_path.exists():
            local_path.parent.mkdir(parents=True, exist_ok=True)
            print("local path not exists, creating...")
        else:
            new_path = local_path.rename(f"{local_path}-{datetime.datetime.now()}")
            print(f"{local_path} exists, rename to {new_path}")
        shutil.copyfile(str(remote_path), str(local_path))
        print("Successfully copied local typora config")
    if mode == TO_REMOTE:
        if remote_path.exists():
            new_path = remote_path.rename(f"{remote_path}-{datetime.datetime.now()}")
            print(f"{remote_path} exists, rename to {new_path}")
        else:
            remote_path.parent.mkdir(parents=True, exist_ok=True)
            print(f"{remote_path.parent} not exists, creating...")
        shutil.copyfile(str(local_path), str(remote_path))
        print("Successfully copied local typora config")


@jack_ubuntu
def terminator(mode: int) -> None:
    local_path = local_config_folder.joinpath("terminator/config")
    remote_path = remote_config_folder.joinpath("terminator/config")
    if mode == TO_LOCAL:
        if not local_path.exists():
            local_path.parent.mkdir(parents=True, exist_ok=True)
            print("local path not exists, creating...")
        else:
            new_path = local_path.rename(f"{local_path}-{datetime.datetime.now()}")
            print(f"{local_path} exists, rename to {new_path}")
        shutil.copyfile(str(remote_path), str(local_path))
        print("Successfully copied local typora config")
    if mode == TO_REMOTE:
        if remote_path.exists():
            new_path = remote_path.rename(f"{remote_path}-{datetime.datetime.now()}")
            print(f"{remote_path} exists, rename to {new_path}")
        else:
            remote_path.parent.mkdir(parents=True, exist_ok=True)
            print(f"{remote_path.parent} not exists, creating...")
        shutil.copyfile(str(local_path), str(remote_path))
        print("Successfully copied local typora config")


@jack_ubuntu
def lunarvim(mode: int) -> None:
    local_path = local_config_folder.joinpath("lvim/config.lua")
    remote_path = remote_config_folder.joinpath("lvim/config.lua")
    if mode == TO_LOCAL:
        if not local_path.exists():
            local_path.parent.mkdir(parents=True, exist_ok=True)
            print("local path not exists, creating...")
        else:
            new_path = local_path.rename(f"{local_path}-{datetime.datetime.now()}")
            print(f"{local_path} exists, rename to {new_path}")
        shutil.copyfile(str(remote_path), str(local_path))
        print("Successfully copied local typora config")
    if mode == TO_REMOTE:
        if remote_path.exists():
            new_path = remote_path.rename(f"{remote_path}-{datetime.datetime.now()}")
            print(f"{remote_path} exists, rename to {new_path}")
        else:
            remote_path.parent.mkdir(parents=True, exist_ok=True)
            print(f"{remote_path.parent} not exists, creating...")
        shutil.copyfile(str(local_path), str(remote_path))
        print("Successfully copied local typora config")


if __name__ == "__main__":
    jack_ubuntu.copy_to_remote()
    # jack_ubuntu.copy_to_local()
