import os
import shutil

s_folder = "/mnt/Fdrive/low_lvl/test"
d_folder = "/mnt/Fdrive/low_lvl/changed"

if not os.path.exists(d_folder):
    os.makedirs(d_folder)

tar_ext = (".txt", ".rar", ".pdf")

for fname in os.listdir(s_folder):

    if fname.lower().endswith(tar_ext):

        full_source_path = os.path.join(s_folder, fname)
        full_dest_path = os.path.join(d_folder, fname)

        if os.path.isfile(full_source_path):
            shutil.copy2(full_source_path, full_dest_path)
            print(f"Copied: {full_source_path}")