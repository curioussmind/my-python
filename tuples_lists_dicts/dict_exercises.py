from typing_extensions import Unpack


captains = {} # 1. create an empty list called captain

# 2 
captains["Enterprise"] = "Picard"
captains["Voyager"] = "Janeway"
captains["Defiant"] = "Sisko"

# 3 check if the items is in the list
if "Enterprise" not in captains:
    captains["Enterprise"] = 'Unknown'
if "Discovery" not in captains:
    captains["Discovery"] = 'Unknwn'

# alternatives to if
for ship in ["Enterprise", "Discovery"]:
    if not ship in captains:
        captains[ship] = "unknown"

for ship in captains:
    print(f"The {ship} is captained by {captains[ship]}")

del captains["Discovery"]
print(captains)


# bonus
captains = dict(
    [
        ("Enterprise", "Picard"),
        ("Voyager", "Janeway"),
        ("Defiant", "Sisko"),
    ]
)
ship_captain = dict(captains)
print(ship_captain)




