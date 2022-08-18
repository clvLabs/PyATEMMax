#!/usr/bin/env python3
# coding: utf-8
"""log-reader.py - Log reader for switcher debugging.
   Part of the PyATEMMax library."""

import json
import argparse
from datetime import datetime
from dataclasses import dataclass

ATEM_HEADER_LEN = 12
ATEM_CMD_HEADER_LEN = 8

@dataclass
class SwitcherCommand:
    len: int
    name: str
    header: bytes
    payload: bytes


@dataclass
class SwitcherMessage:
    header_bitmask: int
    packet_len: int
    session_id: int
    ack_id: int
    resend_packet_id: int
    unknown: int
    packet_id: int
    commands: list


@dataclass
class LogMessage:
    ts: str
    source: str
    data: bytes
    message: SwitcherMessage


def tsstr(ts):
    return f"{ts.hour:02}:{ts.minute:02}:{ts.second:02}.{ts.microsecond:06}"


def hexstr(buf):
    return ' '.join([f'{b:02X}' for b in buf])


def log(msg="", end=None):
    print(f"[{tsstr(datetime.now())}] {msg}", end=end)


def parse_int16(buf, pos):
    return (buf[pos] << 8) + buf[pos+1]


def parse_int8(buf, pos):
    return buf[pos]


def bitmask_str(bm):
    bmstr = ""
    if bm & 0x01: bmstr += "[01 ackReq] "
    if bm & 0x02: bmstr += "[02 hello] "
    if bm & 0x04: bmstr += "[04 resend] "
    if bm & 0x08: bmstr += "[08 reqNxtAft] "
    if bm & 0x10: bmstr += "[10 ack] "
    return bmstr


def parse_command(buf):
    cmd_len = parse_int16(buf, 0)
    cmd_str = ''.join([chr(x) for x in [ buf[4], buf[5], buf[6], buf[7]]])

    cmd = SwitcherCommand(
        cmd_len,
        cmd_str,
        buf[:ATEM_CMD_HEADER_LEN],
        buf[ATEM_CMD_HEADER_LEN:cmd_len],
    )
    return(cmd, buf[cmd_len:])


def parse_switcher_message(buf):
    # bytes 0-1: header_bitmask / packet_len
    header_bitmask = buf[0] >> 3
    packet_len = (buf[0] << 8 & 0x07) + (buf[1])

    # bytes 2-3: session_id
    session_id = parse_int16(buf, 2)

    # bytes 4-5: ack_id
    ack_id = parse_int16(buf, 4)

    # bytes 6-7: resend_packet_id
    resend_packet_id = parse_int16(buf, 6)

    # bytes 8-9: unknown
    unknown = parse_int16(buf, 8)

    # bytes 10-11: packet_id
    packet_id = parse_int16(buf, 10)

    commands = []

    if packet_len > ATEM_HEADER_LEN:
        cmdbuf = buf[ATEM_HEADER_LEN:]
        while cmdbuf:
            try:
                (cmd, cmdbuf) = parse_command(cmdbuf)
                commands.append(cmd)
            except Exception:
                raise
                # print("PASSING !!")
                # cmdbuf = None
                # pass

    switcher_msg = SwitcherMessage(
        header_bitmask,
        packet_len,
        session_id,
        ack_id,
        resend_packet_id,
        unknown,
        packet_id,
        commands,
    )
    return switcher_msg


def read_messages(args):
    messages = []
    with open(args.log) as f:
        for line in f.readlines():
            line = line[:-2] # Remove trailing comma
            jsondata = json.loads(line)
            buf = bytes.fromhex(jsondata['data'])

            msg = LogMessage(
                jsondata['ts'],
                jsondata['source'],
                buf,
                parse_switcher_message(buf),)
            messages.append(msg)

            show_message(args, msg)

    log(f"{len(messages)} messages read")
    return messages


def show_message(args, logmsg):
    log("*"*80)
    log(f"--- {logmsg.ts} {logmsg.source} " + '-'*30)
    swmsg = logmsg.message
    print(f"[DBG] msg len               {len(logmsg.data):,}")
    print(f"[DBG] msg                   {hexstr(logmsg.data)}")
    print(f"[DBG] header_bitmask        0x{swmsg.header_bitmask:02X}    {bitmask_str(swmsg.header_bitmask)}")
    print(f"[DBG] packet_len            0x{swmsg.packet_len:04X}  {swmsg.packet_len}")
    print(f"[DBG] session_id            0x{swmsg.session_id:04X}")
    print(f"[DBG] ack_id                0x{swmsg.ack_id:04X}")
    print(f"[DBG] resend_packet_id      0x{swmsg.resend_packet_id:04X}")
    print(f"[DBG] unknown               0x{swmsg.unknown:04X}")
    print(f"[DBG] packet_id             0x{swmsg.packet_id:04X}")

    for cmd in swmsg.commands:
        print(f"[DBG]   - {cmd.name} ({cmd.len}b) - {hexstr(cmd.header)} - {hexstr(cmd.payload)}")

    xstr = ""
    for b in logmsg.data:
        char = chr(b)
        if char.isalpha() and char.isascii():
            xstr += chr(b)
        else:
            xstr += "."
    if xstr:
        print(f"[DBG] {xstr = }")


def show_messages(args, log_messages):
    for logmsg in log_messages:

        showmsg = False

        if True:
            showmsg = True

        if showmsg:
            show_message(args, logmsg)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("log", help="log file")
    args = parser.parse_args()

    start_time = datetime.now()

    log("ATEM debug switcher spy - log reader")
    log('-'*80)

    log_messages = read_messages(args)
    # show_messages(args, log_messages)


if __name__ == "__main__":
    main()
