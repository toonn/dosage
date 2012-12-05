#!/usr/bin/env python
# Copyright (C) 2012 Bastian Kleineidam
"""
Script to get drunkduck comics and save the info in a JSON file for further processing.
"""
from __future__ import print_function
import re
import sys
import os
import json
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from dosagelib.util import tagre, getPageContent
from scriptutil import contains_case_insensitive

json_file = __file__.replace(".py", ".json")

# names of comics to exclude
exclude_comics = [
    "Monster_Lover", # start page is broken
    "Legacy_of_Blaze", # broken images
    "Dead_Strangers", # broken images
    "Crack", # broken images
    "Iron_Wolf", # broken images
    "A_Call_to_Destiny__NC_17", # start page requires login
    "A_Call_to_Destiny_Reloaded", # start page requires login
    "A_Day_in_the_Life_for_Erik", # broken images
    "A_Fairly_Twisted_Reality", # start page requires login
    "Al_and_Scout", # broken images
    "ANGELOU_____Las_aventuras_de_Nikole", # broken images
    "Apartment_408_Full_Size", # broken images
    "Apple_Valley", # broken images
    "Apt_408_Minis", # broken images
    "atxs", # broken images
    "A_Word_Of_Wisdom", # broken images
    "Brathalla", # broken images
    "Binary_Souls_Other_Dimensions", # broken images
    "BK_Shattered_Hate", # broken images
    "Chomp", # broken images
    "Chu_and_Kenny", # broken images
    "Coga_Suro_2", # broken images
    "Creepy_Girl_and_Her_Zombie_Dog", # broken images
    "CuoreVoodoo", # broken images
    "dairyaire", # broken images
    "DIS", # broken images
    "Dot_TXT", # broken images
    "Dreadnought_Invasion_Six", # broken images
    "Emerald_Winter", # broken images
    "Enter_the_Duck_2", # broken images
    "ffff", # broken images
    "Function_Over_Fashion", # broken images
    "Funday_Morning", # broken images
    "greys_journey", # broken images
    "Head_over_Heart", # broken images
    "Hurrocks_Fardel", # broken images
    "Bhaddland", # start page requires login
    "Bouncing_Orbs_of_Beauty", # start page requires login
    "Busty_Solar", # start page requires login
    "Illusional_Beauty", # broken images
    "Indigo_Bunting__Vampire", # start page requires login
    "Irrumator", # start page requires login
    "Its_A_Boy_Thing", # start page requires login
    "Kokuahiru_comics", # start page requires login
    "Inside_OuT", # broken images
    "Journey_to_Raifina", # broken images
    "KALA_dan", # broken images
    "Live_to_tell", # start page requires login
    "Locoma", # broken images
    "London_Underworld", # broken images
    "Louder_Than_Bombs", # broken images
    "Lucky_Dawg", # broken images
    "Mario_in_Johto", # broken images
    "Master", # start page requires login
    "Mastermind_BTRN", # broken images
    "MAYA_____The_legend_of_Wolf", # broken images
    "Megaman_Zero", # broken images
    "Monster_Lover_Destinys_Path", # start page requires login
    "M_Organ_Art", # start page requires login
    "Morning_Squirtz", # start page requires login
    "MOSAIC", # broken images
    "My_Angel_and_My_Devil", # broken images
    "Nemution_Jewel", # start page requires login
    "Nemution_Redux", # start page requires login
    "New_Pages", # broken images
    "Ninja_Shizatch", # broken images
    "Normalcy_is_for_Wimps", # broken images
    "MIKYAGU", # broken images
    "One_Third_Of_Your_Life_Is_Spent_Sleeping_One_Third_Of_Your_Life_Is_Spent_Working_And_Half_Of_One_Third_Is_Spent_Waiting_The_Question_Is_It_Really_Your_Life", # broken images
    "OTENBA_Files", # start page requires login
    "Panacea", # start page requires login
    "Parker_Lot", # broken images
    "Peter_And_The_Wolf", # start page requires login
    "Perspectives", # broken images
    "Pokemon_Sinnoh_Surfer", # broken images
    "Pokemon_World_Trainers", # broken images
    "Potpourri_of_Lascivious_Whimsy", # start page requires login
    "Pr0nCrest", # start page requires login
    "punished_girls", # start page requires login
    "Powerjeff", # broken images
    "Comicarotica", # start page requires login
    "Dark_Sisters", # start page requires login
    "Death_P0rn", # start page requires login
    "Dreams_in_Synergy", # broken images
    "GNight_Shade", # start page requires login
    "GRIND", # start page requires login
    "HUSS", # start page requires login
    "Red_Dog_Venue", # start page is broken
    "rubber_girls", # start page requires login
    "Robomeks", # broken images
    "Robot_Friday", # broken images
    "SFA", # start page requires login
    "Shadow_Root", # start page requires login
    "Shiro_Karasu", # start page requires login
    "Shelter_of_Wings", # broken images
    "Some_Notes", # broken images
    "Sonic_Advanced_Online", # broken images
    "Sonic_and_tails_corner", # broken images
    "Sonic_Unreal", # broken images
    "Tales_of_Schlock", # start page requires login
    "Splices_of_Life", # broken images
    "STARSEARCHERS", # broken images
    "Ted_The_Terrible_Superhero", # broken images
    "Terra_online_comic", # broken images
    "The_Auragon_Base", # broken images
    "The_Bend", # broken images
    "The_Chronicles_of_Drew", # broken images
    "The_Devils_Horn", # broken images
    "The_Dragon_and_the_Lemur", # start page requires login
    "The_Fighting_Stranger", # broken images
    "The_Mighty_Omega", # broken images
    "The_Misadventures_of_Everyone", # start page requires login
    "The_NEW_Life_Of_TimmY", # broken images
    "The_SSA", # broken images
    "Tony_The_Hedgehog", # broken images
    "Trapped_in_a_Comic", # start page requires login
    "Unsound_of_Mind", # broken images
    "Vampire_Chronicles__Dark_Lust", # start page requires login
    "WarMage", # start page requires login
    "Watashi_No_Ame", # broken images
    "Weave", # broken images
    "Weirdlings", # template error
    "Welcome_To_Border_City", # broken images
    "what_comes_first", # start page requires login
    "Within_Shadows", # broken images
    "Xolta", # start page requires login
    "XTIN__The_Dragons_Dream_World", # start page requires login
    "X_UP", # start page requires login
    "Zandars_Saga", # start page requires login
    "Twonks_and_Plonkers", # broken images, no real content
    "U_Chuu_No_Hoshi_Hotoshi_Tsuko", # broken images
]


def handle_url(url, url_matcher, num_matcher, res):
    """Parse one search result page."""
    try:
        data, baseUrl = getPageContent(url)
    except IOError as msg:
        print("ERROR:", msg, file=sys.stderr)
        return
    for match in url_matcher.finditer(data):
        comicurl = match.group(1)
        name = comicurl[:-1].rsplit('/')[-1]
        if contains_case_insensitive(res, name):
            # we cannot handle two comics that only differ in case
            print("WARN: skipping possible duplicate", name, file=sys.stderr)
            continue
        if name in exclude_comics:
            continue
        # find out how many images this comic has
        end = match.end(1)
        mo = num_matcher.search(data[end:])
        if not mo:
            print("ERROR:", repr(data[end:end+300]), file=sys.stderr)
            continue
        num = int(mo.group(1))
        res[name] = num


def save_result(res):
    """Save result to file."""
    with open(json_file, 'wb') as f:
        json.dump(res, f, sort_keys=True)


def get_results():
    """Parse all search result pages."""
    base = "http://www.drunkduck.com/search/?page=%d&search=&type=0&type=1&last_update="
    href = re.compile(tagre("a", "href", r'(/[^"]+/)', before="size24 yanone blue"))
    num = re.compile(r'(\d+) pages?</span>')
    # store info in a dictionary {name -> number of comics}
    res = {}
    # a search for an empty string returned 825 result pages
    result_pages = 825
    print("Parsing", result_pages, "search result pages...", file=sys.stderr)
    for i in range(1, result_pages + 1):
        print(i, file=sys.stderr, end=" ")
        handle_url(base % i, href, num, res)
    save_result(res)


def print_results(min_strips):
    """Print all comics that have at least the given number of minimum comic strips."""
    with open(json_file, "rb") as f:
        comics = json.load(f)
    for name, num in sorted(comics.items()):
        if name in exclude_comics:
            continue
        if num >= min_strips:
            print("add('%s')" % name)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print_results(int(sys.argv[1]))
    else:
        get_results()
