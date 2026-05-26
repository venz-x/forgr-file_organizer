#!/usr/bin/env python3

import cmd
import shlex
import argparse
import sys
import os

# look at right file
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(SCRIPT_DIR)

from extension import docs_ext, imgs_ext, archive_ext,bin_ext, bak_ext, audio_ext, code_ext, db_ext, lib_ext,pkg_ext, video_ext, web_ext

from engine import copy_files_by_extensions

class ForgrShell(cmd.Cmd):
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    RESET = "\033[0m"


    logo = r"""
                            _  .-')              _  .-')   
                       ( \( -O )            ( \( -O )  
   ,------. .-'),-----. ,------.   ,----.    ,------.  
('-| _.---'( OO'  .-.  '|   /`. ' '  .-./-') |   /`. ' 
(OO|(_\    /   |  | |  ||  /  | | |  |_( O- )|  /  | | 
/  |  '--. \_) |  |\|  ||  |_.' | |  | .--, \|  |_.' | 
\_)|  .--'   \ |  | |  ||  .  '.'(|  | '. (_/|  .  '.' 
  \|  |_)     `'  '-'  '|  |\  \  |  '--'  | |  |\  \  
   `--'         `-----' `--' '--'  `------'  `--' '--' 

    """

    intro = f"{CYAN}{logo}{RESET}\n" + "="*40 + "\nWelcome to FORGR.\nType 'help' or '?' to list commands.\n" + "="*40
    
    prompt = f"{GREEN}forgr>{RESET} "

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
            print(f"[-] Error: Unknown extension type '{ex_type}'.")
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
    # Setup the Argument Parser with RawTextHelpFormatter
    parser = argparse.ArgumentParser(
        prog="forgr",
        description="FORGR: A fast and interactive file organizer.",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="""
Usage Examples:
--------------------------------
Syntax: 
  run s="<source_dir>" d="<dest_dir>" ex="<extension_group>"

Available Extension Groups:
  images, docs, code, web, audio, video, archives, binaries, packages, libraries, database, backup
        """
    )

    parser.add_argument(
        '-v', '--version', 
        action='version', 
        version='%(prog)s v1.0.0'
    )

    args = parser.parse_args()


    try:
        ForgrShell().cmdloop()
    except KeyboardInterrupt:
        print("\n\n[*] --------- ")
        sys.exit(0)