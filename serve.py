#!/usr/bin/env python3
"""Server statis sederhana untuk website komunitas.

Melayani file di folder ini. Menerima --port dan --bind (ditambahkan
otomatis oleh lingkungan preview), plus -p sebagai sinonim port.
"""
import argparse
import os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", "-p", type=int, default=8080)
    parser.add_argument("--bind", "-b", default="0.0.0.0")
    parser.add_argument("-d", "--directory", default=".")
    args, _unknown = parser.parse_known_args()

    os.chdir(args.directory)
    handler = SimpleHTTPRequestHandler
    server = ThreadingHTTPServer((args.bind, args.port), handler)
    print(f"Serving on http://{args.bind}:{args.port}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()


if __name__ == "__main__":
    main()
