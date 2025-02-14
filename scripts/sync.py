#!/usr/bin/env python3

import logging
import os
import sys
import shutil
import subprocess
from pathlib import Path

import mkdocs.plugins
from dotenv import load_dotenv

from scripts.config import PACKAGES

load_dotenv()

# Setup logging
log = logging.getLogger('mkdocs')


@mkdocs.plugins.event_priority(100)
def on_startup(command, *, clear = True, **kwargs):
    """MkDocs public directory sync startup hook"""
    log.debug("Public directory sync started")

    # Ensure script runs from the root of the project
    if not Path('mkdocs.yml').is_file():
        log.error("Script must be run from the root of the project")
        sys.exit(1)

    # Check public directory
    if Path('public').exists() and clear:
        shutil.rmtree('public')
        log.debug("Public directory cleared")

    # Sync directories
    os.makedirs('public')

    # Sync overrides
    overrides = Path('overrides')
    if not overrides.is_dir():
        log.error(f"Overrides directory not found: {overrides}")
        sys.exit(1)

    try:
        subprocess.run(
            ['rsync', '-a', f'{overrides}/', 'public'],
            check=True,
        )
    except subprocess.CalledProcessError:
        log.error("Failed to sync 'overrides'")
        shutil.rmtree('public')
        sys.exit(1)

    # Sync packages
    packages_path = os.getenv('PACKAGES_PATH')
    if not packages_path:
        log.info("Skipping packages sync")
        sys.exit(0)
    else:
        packages_path = Path(packages_path)
        packages_target = Path('public')

    for package_name, package_dirs in PACKAGES.items():
        package_path = packages_path / package_dirs[0]
        package_target = packages_target / package_dirs[1]
        if not package_path.is_dir():
            log.error(f"Package directory not found: {package_path}")
            sys.exit(1)

        try:
            subprocess.run(
                ['rsync', '-a', f'{package_path}/', package_target],
                check=True,
            )
        except subprocess.CalledProcessError:
            log.error(f"Failed to sync '{package_name}'")
            sys.exit(1)

    log.info("Public folder synced successfully")


def main():
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    on_startup('serve', force='--force' in sys.argv)


if __name__ == '__main__':
    main()
