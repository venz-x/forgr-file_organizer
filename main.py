#!/usr/bin/env python3

import cmd
import shlex

from extension import docs_ext, imgs_ext, archive_ext,bin_ext, bak_ext, audio_ext, code_ext, db_ext, lib_ext,pkg_ext, video_ext, web_ext

from engine import copy_files_by_extensions

class ForgrShell(cmd.Cmd):
    intro = "\n" + "="*40 + "\nWelcome to FORGR.\nType 'help' or '?' to list commands.\n" + "="*40
    prompt = "forgr> "

    ext_groups = {
        "images": imgs_ext,
        "docs": docs_ext,
        "code": code_ext,
        "web": web_ext,
        "audio": audio_ext,
        "video": video_ext,
        "archives": archive_ext,
        "binaries": bin_ext,
        "packages": pkg_ext,
        "libraries": lib_ext,
        "database": db_ext,
        "backup": bak_ext
    }

    def do_run(self, arg):
        """Run the copy tool. 
        Syntax: run s="/path/to/source" d="/path/to/dest" ex=images"""

        args = shlex.split(arg)

        s_folder = ""
        d_folder = ""
        ex_type = ""

        for item in args:
            if item.startswith("s="):
                s_folder = item[2:]  
            elif item.startswith("d="):
                d_folder = item[2:]  
            elif item.startswith("ex="):
                ex_type = item[3:]
        

        if not s_folder or not d_folder or not ex_type:
            print("[-] Error: Missing arguments.")
            print("    Usage: run s=\"/mnt/...\" d=\"/mnt/...\" ex=images")
            return
        
        if ex_type not in self.ext_groups:
            print(f"[-] Error: You are using Unknown extension type '{ex_type}'.")
            print(f"    Available types: {', '.join(self.ext_groups.keys())}")
            return
        
        print(f"[*] Starting FORGR process...")
        print(f"    Source: {s_folder}")
        print(f"    Destination:   {d_folder}")
        print(f"    Target: {ex_type}\n")

        copy_files_by_extensions(s_folder, d_folder, self.ext_groups[ex_type])
        print("\n[*] Process Complete.")


    def do_exit(self, arg):
        """Exit the FORGR."""
        print("-----------------")
        return True  

    def emptyline(self):
        pass


if __name__ == "__main__":
    ForgrShell().cmdloop()
