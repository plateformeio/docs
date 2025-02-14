#!/usr/bin/env python3

import atexit
import logging
import os
import sys
import threading
import time
from pathlib import Path

import mkdocs.plugins
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer, ObserverType

from scripts.config import PACKAGES
from scripts.sync import on_startup as sync

# Setup logging
log = logging.getLogger('mkdocs')


class WatchHandler(FileSystemEventHandler):
    """MkDocs public directory sync handler"""
    def __init__(self):
        log.debug("Initializing watch handler")
        self.sync_delay = 1
        self.timer = None
        self.lock = threading.Lock()

    def sync_directories(self):
        with self.lock:
            sync('serve', force=True)

    def on_any_event(self, event):
        if event.is_directory:
            return
        log.debug(f"Event detected: {event.src_path}")
        if self.timer:
            self.timer.cancel()
        self.timer = threading.Timer(self.sync_delay, self.sync_directories)
        self.timer.start()


observer: ObserverType | None = None
handler: 'WatchHandler | None' = None


def cleanup():
    global observer
    if observer:
        log.debug("Cleanup called")
        observer.stop()
        observer.join()
        log.info("File watcher stopped")


@mkdocs.plugins.event_priority(-50)
def on_startup(command, **kwargs):
    """MkDocs public directory watcher startup hook"""
    if command != 'serve':
        return

    global observer, handler
    log.debug("Public directory watcher started")

    # Ensure script runs from the root of the project
    if not Path('mkdocs.yml').is_file():
        log.error("Script must be run from the root of the project")
        sys.exit(1)

    # Setup observer
    handler = WatchHandler()

    try:
        log.debug("Setting up observer")
        observer = Observer()

        # Watch overrides
        observer.schedule(handler, 'overrides', recursive=True)

        # Watch packages
        if packages_path := os.getenv('PACKAGES_PATH'):
            packages_path = Path(packages_path)
            for package_dirs in PACKAGES.values():
                package_path = packages_path / package_dirs[0]
                if not package_path.is_dir():
                    continue
                observer.schedule(handler, package_path, recursive=True)

        observer.start()
        atexit.register(cleanup)
        log.info("File watcher started successfully...")
    except Exception as e:
        log.error(f"Error setting up file watcher: {e}")


def main():
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    on_startup('serve')

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        cleanup()
        sys.exit(0)


if __name__ == '__main__':
    main()
