import os
import shutil

from extension import docs_ext, imgs_ext, archive_ext,bin_ext, bak_ext, audio_ext, code_ext, db_ext, lib_ext,pkg_ext, video_ext, web_ext


def copy_files_by_extentions(source_dir, dest_dir, extention):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    for fname in os.listdir(s_folder):

        if fname.lower().endswith(extention):
            full_source_path = os.path.join(source_dir, fname)
            full_dest_path = os.path.join(dest_dir, fname)

            if os.path.isfile(full_source_path):
                shutil.copy2(full_source_path, full_dest_path)
                print(f"Copied: {fname} -> {os.path.basename(dest_dir)}")





s_folder = "/mnt/Fdrive/low_lvl/test"
