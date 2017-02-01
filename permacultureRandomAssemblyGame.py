#! python3
# permacultureRandomAssemblyGame.py - Program used to combine elements randomly
# in order to view them in different ways in order to innovate or see things in
# a different way.

import random

#Setting the function to be multiplied.
def createSentenceSheet():

#List of elements
    elements = ["attic",
                "barn", "barnyard", "basement", "bee hive", "berms", "brook",
                "building",

                "cattle", "center", "chicken", "chicken coop", "chicken tractor",
                "cob building", "cob oven", "cold", "community",
                "community garden", "companion plants", "compost",
                "compost pile", "composting toilet", "core", "culvert",

                "desire line", "drain", "duck",

                "east", "edge", "electric fence", "electricity", "elevation", "erosion", "espalier",

                "fence", "field", "finger-styled beds", "flower bed", "forest", "fruit",

                "goat", "greenhouse", "guest building", "gravity-fed irrigation", "greywater",
                "greywater filtration", "gulley",

                "hay", "hay bale", "hay field", "herbs", "high elevation", "home building", "hose", "hot",

                "irrigtation",

                "lagoon",

                "mandala garden", "midsuccession", "moon", "moveable greenhouse", "mulch", "mushroom",

                "north",

                "outdoor shower",

                "parking", "path", "perennials", "permanent greenhouse", "pig pen", "piping", "pole barn",
                "pollinator", "polyculture", "pond", "power",

                "rain barrel", "raised bed", "riparian buffer", "river", "road", "rock wall", "root cellar",
                "rocket mass heater",

                "seedlings", "septic tank", "shack", "sheep", "shrub", "silo", "spigot", "spring house", "snow", "snow plow",
                "solar panel", "solar oven", "source", "south", "spiral", "spring", "stream", "sun", "swales",
                "swamp",

                "tent", "tractor", "tractor-pulled water supply", "tree", "trellis", "trench", "truck", "tool shed",

                "vegetable", "vermicomposting",

                "wall", "washing station", "watershed", "well", "west", "wetlands", "wind", "windmill", "wood",
                "wood pile", "wood shed", "workshop",

                "yurt",

                "zone 00 (me)", "zone 0 (home)", "zone 1", "zone 2", "zone 3", "zone 4",
                "zone 5", "zone 6 (beyond site)"]

#Create second list of prepositions
    prepositionList = ["aboard", "about", "above", "across", "after", "against",
                       "along", "alongside", "amid", "amidst", "among", "amonsgt",
                       "anti", "around", "as", "astride", "at", "atop", "according to",
                       "ahead of", "a la", "along with", "apart from", "as for",
                       "aside from", "as per", "as to", "as well as", "away from",
                       "bar", "barring", "before", "behind", "below", "beneath", "beside",
                       "besides", "between", "beyond", "but", "by", "because of", "but for",
                       "by means of", "circa", "concerning", "considering", "counting", "cum",
                       "close to", "contrary to", "despite", "down", "during", "depending on",
                       "due to", "except", "excepting", "excluding", "except for", "following",
                       "for", "from", "forward of", "further to", "given", "gone", "in",
                       "including", "inside", "into", "in addition to", "in between",
                       "in case of", "in face of", "in favour of", "in front of", "in lieu of",
                       "in spite of", "instead of", "in view of", "less", "like", "minus",
                       "near", "notwithstanding", "near to", "next to", "of", "off", "on",
                       "onto", "opposite", "outside", "over", "on account of", "on behalf of",
                       "on board", "on to", "on top of", "opposite to", "other than", "out of",
                       "outside of", "owing to", "past", "pending", "per", "plus", "pro",
                       "preparatory to", "prior to", "re", "regarding", "respecting", "round",
                       "regardless of", "save", "saving", "since", "save for", "than",
                       "through", "throughout", "till", "to", "touching", "toward", "towards",
                       "thanks to", "together with", "under", "underneath", "unlike", "until",
                       "up", "upon", "up against", "up to", "up until", "versus", "via",
                       "vis-a-vis", "with", "within", "without", "worth", "with reference to",
                       "with regard to"]

#Randomly choose one entry from each list to print into sentence.
    randomSentence = (random.choice(elements) + ' ' + random.choice(prepositionList) + ' ' +
                      random.choice(elements))

    print(randomSentence)

#Creates 3 sentences for this game.
for i in range(1):
    createSentenceSheet()
