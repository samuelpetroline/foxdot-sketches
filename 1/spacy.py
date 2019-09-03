Scale.default = "minor"
Scale.bpm=120
k1 >> space(var([4, 0, 1, 2], [2, 8, 4, 2]), sus=2, rate=4, dur=PDur(3, 8), pan=PWhite(-2, 2), echo=0.5, echotime=(3,2)     , amp=PWhite(0.4, 0.7), oct=[3, 4])
b1 >> bass(k1.follow() + [0, 1, 2], dur=PDur(1, 16), amp=PWhite(0.4, 0.7), oct=(4, 5), sus=8, pan=[-1, [1, 0]], lpf=300)
