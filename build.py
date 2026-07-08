#!/usr/bin/env python3
"""
Build the static index.html from template.html.

Injects PLAYERS: the deduped player list (name, team, count, goals, years,
positions) computed from players.txt.

Usage:  python3 build.py
"""

import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "players.txt")
TEMPLATE = os.path.join(HERE, "template.html")
OUT = os.path.join(HERE, "index.html")


def players_json():
    txt = open(SRC, encoding="utf-8").read()
    kicks = json.loads(txt[txt.index("["):txt.rindex("]") + 1])
    order, by = [], {}
    for k in kicks:
        key = (k["name"], k["team"])
        if key not in by:
            by[key] = {"name": k["name"], "team": k["team"], "count": 0,
                       "goals": 0, "years": set(), "positions": set()}
            order.append(key)
        p = by[key]
        p["count"] += 1
        p["goals"] += k.get("goal", 0) or 0
        if k.get("year") is not None:
            p["years"].add(k["year"])
        if k.get("bucket"):
            p["positions"].add(k["bucket"])
    out = []
    for key in order:
        p = by[key]
        out.append({"name": p["name"], "team": p["team"], "count": p["count"],
                    "goals": p["goals"], "years": sorted(p["years"]),
                    "positions": sorted(p["positions"])})
    return out


def main():
    tpl = open(TEMPLATE, encoding="utf-8").read()
    players = players_json()
    html = tpl.replace("/*PLAYERS*/", json.dumps(players, ensure_ascii=False))
    open(OUT, "w", encoding="utf-8").write(html)
    print("Wrote %s  (%d players)" % (OUT, len(players)))


if __name__ == "__main__":
    main()
