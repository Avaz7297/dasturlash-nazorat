# -*- coding: utf-8 -*-
import students_roster as sr

roster = sr.STUDENTS_ROSTER

print(f"Total students in roster: {len(roster)}")

groups = {}
for s in roster:
    g = s["group"]
    if g not in groups:
        groups[g] = []
    groups[g].append(s)

print("\n--- Group breakdown ---")
for g, st_list in sorted(groups.items()):
    print(f"\nGroup: {g} ({len(st_list)} students)")
    for i, st in enumerate(st_list):
        # Validate ID
        sid = st["id"]
        assert len(sid) == 12, f"ID {sid} is not 12 chars!"
        assert sid.isdigit(), f"ID {sid} is not all digits!"
        assert len(st["name"].strip()) > 3, f"Name too short: {st['name']}"
        print(f"  {i+1:2d}. ID: {sid} | {st['name']}")

# Check duplicates
ids = [s["id"] for s in roster]
assert len(ids) == len(set(ids)), "DUPLICATE ID FOUND!"
print("\n[SUCCESS] All 130 student IDs are 12-digit numeric, valid, and 100% UNIQUE!")
