import os, subprocess, shutil
from imgcat import imgcat

for directory, subs, files in os.walk('screenshots'):
    for file in files:
        path = f'screenshots/{file}'
        print(path)
        # subprocess.run(f"imgcat {path}", shell=True)
        imgcat(open(path))
        action = input("; (enter) to delete. (enter) to keep: ")
        if action != ";":
            shutil.move(path, f"keepers/{file}")
        else:
            shutil.move(path, f"tossers/{file}")
    print ("deleting " + directory)
    try:
        os.rmdir(directory)  # this will only remove if empty
    except:
        pass