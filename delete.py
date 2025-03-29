import os
import shutil
import stat

def remove_readonly(func, path, _):
    os.chmod(path, stat.S_IWRITE)
    func(path)

folder = "output"
if os.path.exists(folder):
    shutil.rmtree(folder, onerror=remove_readonly)