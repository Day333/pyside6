import subprocess
import sys


def install_package(conda_env, package_name):
    cmd = f"conda activate {conda_env} && pip install {package_name} --yes"
    result = subprocess.run(cmd, shell=True)
    return result.returncode

def uninstall_package(conda_env, package_name):
    cmd = f"conda activate {conda_env} && pip uninstall {package_name} --yes"
    result = subprocess.run(cmd, shell=True)
    return result.returncode

if __name__ == "__main__":
    # 从命令行参数获取 conda 环境名和要安装的包名
    conda_env = "pyside6"
    package_name = "numpy"

    # 安装包
    return_code = install_package(conda_env, package_name)
    if return_code == 0:
        print(f"Successfully installed {package_name} in {conda_env}")
    else:
        print(f"Failed to install {package_name} in {conda_env}")