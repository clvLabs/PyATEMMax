#!/usr/bin/env python3
# coding: utf-8
"""switcher-spy.py - Simple UDP man-in-the-middle for switcher debugging.
   Part of the PyATEMMax library."""

import socket
import json
import argparse
from datetime import datetime

import importlib
log_reader = importlib.import_module("log-reader")

args = None

UDP_PORT = 9910   # Standard ATEM UDP port
LOG_FILE_NAME = "switcher-spy-log-{y:04}{m:02}{d:02}-{h:02}{mm:02}{s:02}.jsonl"


def tsstr(ts):
    return f"{ts.hour:02}:{ts.minute:02}:{ts.second:02}.{ts.microsecond:06}"


def log(msg="", end=None):
    print(f"[{tsstr(datetime.now())}] {msg}", end=end)


def start_server(args, server_addr, switcher_addr, log_name):
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(server_addr)
    clients = []
    switcher_messages = 0
    switcher_bytes = 0
    client_messages = 0
    client_bytes = 0

    log("Listening, press <CTRL+C> to stop.")
    while True:
        data, addr = server.recvfrom(10240)
        is_switcher_msg = (addr == switcher_addr)

        if is_switcher_msg:
            switcher_messages += 1
            switcher_bytes += len(data)
            for client_addr in clients:
                server.sendto(data, client_addr)
        else:
            client_messages += 1
            client_bytes += len(data)
            if addr not in clients:
                print()
                log(f"New client connected from {addr[0]}:{addr[1]} - total: {len(clients)}")
                clients.append(addr)
            server.sendto(data, switcher_addr)

        total_messages = client_messages + switcher_messages
        total_bytes = client_bytes + switcher_bytes

        source = "SW " if is_switcher_msg else "CLI"
        log("" \
            + f"[TOTAL: {total_messages:,} msgs, {total_bytes:,}b]" \
            + f" [Switcher: {switcher_messages:,} msgs, {switcher_bytes:,}b]" \
            + f" [Client: {client_messages:,} msgs, {client_bytes:,}b]" \
            + f" [Last: {source}, {len(data):,}b]" \
            + " "*10
            , end='\r')


        if args.show_messages:
            if len(data) > 12:
                msg = log_reader.LogMessage(
                        "now",
                        source,
                        data,
                        log_reader.parse_switcher_message(data),)

                log_reader.show_message(args, msg)


        if log_name:
            if len(data) > 12 or args.save_keepalive:
                log_obj = {
                    "ts": tsstr(datetime.now()),
                    "source": source,
                    "data": "".join([f"{b:02X} " for b in data]),
                }
                log_json = json.dumps(log_obj)
                with open(log_name, "a") as log_file:
                    log_file.write(f"{log_json},\n")


def main():
    global args
    parser = argparse.ArgumentParser()
    parser.add_argument("ip", help="switcher IP address")
    parser.add_argument('-s', '--show-messages', action='store_true', help='Show parsed messages')
    parser.add_argument('-d', '--dry-run', action='store_true', help='Dry run, do not save output')
    parser.add_argument('-k', '--save-keepalive', action='store_true', help='Save "keep-alive" messages')
    args = parser.parse_args()

    start_time = datetime.now()
    log_name = LOG_FILE_NAME.format(
        y = start_time.year, m = start_time.month, d = start_time.day,
        h = start_time.hour, mm = start_time.minute, s = start_time.second)

    log("ATEM debug switcher spy")
    log('-'*80)
    log(f"Server port.....: {UDP_PORT}")
    log(f"Switcher address: {args.ip}:{UDP_PORT}")
    if args.dry_run:
        log(f"Log file........: NONE (dry run)")
    else:
        log(f"Log file........: {log_name}")
    log('-'*80)

    switcher_addr = (args.ip, UDP_PORT)
    server_addr = ("0.0.0.0", UDP_PORT)

    try:
        if args.dry_run:
            start_server(args, server_addr, switcher_addr, None)
        else:
            start_server(args, server_addr, switcher_addr, log_name)
    except KeyboardInterrupt:
        print()
        log("Server STOPPED")


if __name__ == "__main__":
    main()
