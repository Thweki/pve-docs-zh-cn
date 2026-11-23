#!/usr/bin/env python3
"""Print a read-only tree of local release downloads or an extracted archive."""

import argparse
import hashlib
from pathlib import Path
import stat
import sys


def print_tree(directory, hashes=False, stream=None):
    """Print sorted entries and logical byte totals; return False on partial scans.

    Symlinks and special files are listed but never intentionally traversed or
    read. Inspect a quiescent directory: this is not an atomic filesystem snapshot.
    """
    if stream is None:
        stream = sys.stdout
    root_stat = directory.lstat()
    if not stat.S_ISDIR(root_stat.st_mode):
        raise ValueError("root must be a directory, not a file or symbolic link")

    files = directories = links = special = total = errors = 0
    # Explicit stack avoids Python's recursion limit for extracted source trees.
    pending = [(directory, "", "", True)]
    while pending:
        path, prefix, connector, is_root = pending.pop()
        # repr preserves readable Chinese names while escaping control characters.
        label = repr(str(path) if is_root else path.name)
        try:
            info = root_stat if is_root else path.lstat()
            if stat.S_ISDIR(info.st_mode):
                label += "/"
                if not is_root:
                    directories += 1
                children = sorted(path.iterdir(), key=lambda child: child.name)
                child_prefix = prefix + ("    " if connector == "`-- " else "|   ")
                if is_root:
                    child_prefix = ""
                for index in range(len(children) - 1, -1, -1):
                    branch = "`-- " if index == len(children) - 1 else "|-- "
                    pending.append((children[index], child_prefix, branch, False))
            elif stat.S_ISREG(info.st_mode):
                files += 1
                total += info.st_size
                label += f" [{info.st_size} bytes]"
                if hashes:
                    digest = hashlib.sha256()
                    with path.open("rb") as source:
                        for chunk in iter(lambda: source.read(1024 * 1024), b""):
                            digest.update(chunk)
                    label += f" [sha256={digest.hexdigest()}]"
            elif stat.S_ISLNK(info.st_mode):
                links += 1
                label += " [symlink, not followed]"
            else:
                special += 1
                label += " [special, not read]"
        except OSError as error:
            errors += 1
            label += f" [ERROR: {str(error)!r}]"
        print(prefix + connector + label, file=stream)

    summary = (f"\n{files} files, {directories} directories, {links} symlinks, "
               f"{special} special entries; {total} bytes")
    if errors:
        summary += f" (incomplete: {errors} errors)"
    print(summary, file=stream)
    return errors == 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path, help="local release directory to inspect")
    parser.add_argument("--sha256", action="store_true",
                        help="also read regular files in chunks and display SHA256 hashes")
    args = parser.parse_args(argv)
    try:
        return 0 if print_tree(args.directory, hashes=args.sha256) else 1
    except (OSError, ValueError) as error:
        print(f"Tree inspection failed: {str(error)!r}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
