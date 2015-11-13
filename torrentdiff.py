#!/usr/bin/env python

from torrentool.api import Torrent
import os


def get_torrents_in_dir(path):
    torrent_files = (fn for fn in os.listdir(path) if fn.endswith('.torrent'))
    return (Torrent.from_file(name) for name in torrent_files)


def get_included_files_for_torrents(torrents):
    files = set()
    for torrent in torrents:
        # Annoyingly torrentool doesn't use namedtuples. Index 0 is the path
        # (and 1 is the size, which we don't care about).
        files.update(torrent_file[0] for torrent_file in torrent.files)
    return files


def get_recursive_files_in_dir(base_dir):
    relative_paths = set()
    for root, _, files in os.walk(base_dir):
        relative_paths.update(
            os.path.relpath(os.path.join(root, fn), base_dir) for fn in files
        )
    return relative_paths


if __name__ == '__main__':
    import sys
    torrents = get_torrents_in_dir(sys.argv[1])
    files_in_torrents = get_included_files_for_torrents(torrents)
    files_in_directory = get_recursive_files_in_dir(sys.argv[2])
    print(files_in_directory - files_in_torrents)
