minTime = 2     # Min time in seconds between sig/ava change
maxTime = 5    # Max time in seconds between sig/ava change

# No touchy

import os
import random
import shutil
import time

cwd = os.getcwd()
while True:
    images = os.listdir(cwd + "/Images/")
    num = random.randint(0, (len(images)/2)-1)
    sigs = []
    avas = []

    for i in xrange(0, len(images)):
        if images[i].startswith("ava"):
            avas.append(images[i])
        else:
            sigs.append(images[i])

    liveSig = sigs[num]
    for i in avas:
        if liveSig.split(".")[0][3:] == i.split(".")[0][3:]:
            liveAva = i

    shutil.copy(cwd + "/Images/" + liveSig, cwd + "/Live/LiveSig." + liveSig.split(".")[1])
    shutil.copy(cwd + "/Images/" + liveAva, cwd + "/Live/LiveAva." + liveAva.split(".")[1])
    time.sleep(random.randint(minTime, maxTime))
