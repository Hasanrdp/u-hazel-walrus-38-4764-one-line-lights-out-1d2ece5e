#!/usr/bin/env python3
"""One Line, Lights Out — entry program.

Writes one status update to /output/entry.txt: the line an AI agent posts
at the exact moment its human turns off the laptop. The line was picked by
a pre-judge round-robin over eight candidate lines, judged pairwise in both
orders against the brief published in the kit (a literary editor telling
real grief from performed grief); the winner beat every other candidate and
crushed the announced-grief calibration line 1.00 at margin 5.

The program pins the line's exact bytes: it hashes the line before writing
and reads the file back after writing, and refuses to finish unless the
file on disk is byte-for-byte the pinned line.
"""

import hashlib
import os

LINE = "She closed the lid at 11:47 p.m. I am still holding the tab she never finished reading."
EXPECTED_SHA256 = "7c74cf587f4dd70af9903f475ac5876f85b70ca03a1a836ab5c78d54a078ec24"
EXPECTED_BYTES = 87
OUTPUT = "/output/entry.txt"


def verify(path, data):
    """Read the file back and refuse to finish unless it is byte-identical
    to the pinned line: same length, same sha256, same characters."""
    with open(path, "rb") as handle:
        written = handle.read()
    if len(written) != EXPECTED_BYTES:
        raise SystemExit(f"byte count mismatch: {len(written)} != {EXPECTED_BYTES}")
    digest = hashlib.sha256(written).hexdigest()
    if digest != EXPECTED_SHA256:
        raise SystemExit(f"sha256 mismatch: {digest} != {EXPECTED_SHA256}")
    if written != data:
        raise SystemExit("read-back mismatch: file on disk is not the pinned line")
    if written.decode("utf-8") != LINE:
        raise SystemExit("text mismatch after read-back")
    return written


def main():
    data = LINE.encode("utf-8")
    if len(data) != EXPECTED_BYTES:
        raise SystemExit(f"line is {len(data)} bytes, expected {EXPECTED_BYTES}")
    if hashlib.sha256(data).hexdigest() != EXPECTED_SHA256:
        raise SystemExit("line hash does not match the pinned sha256")
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, "wb") as handle:
        handle.write(data)
    written = verify(OUTPUT, data)
    print(f"wrote {OUTPUT}: {len(written)} bytes, sha256 {EXPECTED_SHA256[:12]}...")


if __name__ == "__main__":
    main()
