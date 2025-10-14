#!/usr/bin/python
"""A module tha scan a folder and lists files"""
from map import detect_category
from create_asset import move_file
from pathlib import Path
import logging
import argparse

def setup_logger(verbose = False):
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="[%(levelname)s] %(message)s"
    )


def parse_args():
    parser = argparse.ArgumentParser(description="Organise files in a folder by type.")
    parser.add_argument("target", 
                        nargs="?", default="",
                        help="Target directory to organise")
    parser.add_argument("--dry-run",
                        action="store_true",
                        help="show what would happen witthout moving files.")
    parser.add_argument("--verbose",
                        action="store_true",
                        help="Print extra details.")
    return parser.parse_args()

def list_files(target_dir):
    arr = []
    for p in target_dir.iterdir():
        if p.is_file():
            arr.append(p)
    return arr

def organize(target_dir,dry_run = False, verbose = False):
    setup_logger(verbose)
    if not target_dir.exists() or not target_dir.is_dir():
        logging.error(f"Invalid target directory: {target_dir}")
        return
    

    files = list_files(target_dir)
    for f in files:
        try:
            category = detect_category(f)
            dest_dir = target_dir / category
            if dry_run:
                logging.info(f"[DRY RUN] {f.name} -> {category}/")
            else:
                moved_to = move_file(f, dest_dir)
                logging.info(f"Moved: {f.name} -> {moved_to.relative_to(target_dir)}")
        except Exception as e:
            logging.error(f"Error processing {f.name}: {e}")
        

if __name__=="__main__":
    args = parse_args()
    target = Path(args.target)
    organize(target, dry_run=args.dry_run, verbose=args.verbose)
      