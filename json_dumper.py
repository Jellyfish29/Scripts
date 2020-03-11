import os
import json
lst = []

pathes = [file for file in os.listdir("images")]
desc = [
    {
        "name": "Wormhole",
        "desc": "The Wormhole can be traversed to reach an elite enemy"
    },
    {
        "name": "Gravity Well",
        "desc": "The micro Black Hole in the center slows every object caught in its Gravity"
    },
    {
        "name": "Planet",
        "desc": "A Collision with a planet might result in the destruction of the Ship"
    },
    {
        "name": "Repair Station",
        "desc": "A small Repair Station, repairing 1 damage per second"
    },
    {
        "name": "Mutara Gas Nebula",
        "desc": "Flying into the Nebulae increases the ships Fire Rate"
    },
    {
        "name": "Ion Strom Nebula",
        "desc": "Flying into the Nebula results in Damgage to the Ship"
    },
    {
        "name": "Anti Gravity Well",
        "desc": "Speed up every object caught in the anti gravity field"
    }
]
descs = [i["desc"] for i in desc]
names = [i["name"] for i in desc]

for desc, name, img in zip(descs, names, sorted(pathes)):
    lst.append(
        {
            "desc": desc,
            "name": name,
            "img": img
        }
    )

with open("phenomdesc.json", "w") as f:
    json.dump(lst, f)
