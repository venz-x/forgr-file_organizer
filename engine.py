import os
import shutil

def copy_files_by_extensions(source_dir, dest_dir, extention):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    copied_count = 0
    for fname in os.listdir(source_dir):

        if fname.lower().endswith(extention):
            full_source_path = os.path.join(source_dir, fname)
            full_dest_path = os.path.join(dest_dir, fname)

            if os.path.isfile(full_source_path):
                shutil.copy2(full_source_path, full_dest_path)
                print(f"Copied: {fname} -> {os.path.basename(dest_dir)}")
                copied_count += 1

