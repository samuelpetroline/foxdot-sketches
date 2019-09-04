# 1
k1 >> star([4, 9, 0, (-1, 2)], phase=2, pan=PWhite(-1, 1), bits= 3, drive=0.1, delay=[2, 1, 3], dur=(1/2, 1/4), amp=0.5)

# 2
k2 >> sinepad([0, -1, -5, [4, [2], (4, [8, 0])]], dur=[1/4, 1/2, 1], room=1, hpf=PWhite(0, 700), pan=[-2, -1, 0, 1, 2])

# 5
d1 >> play('<(x ) (sx)(@dba)<V: >[--]>')

# 3
d3 >> play('+ + +').every(4, "stutter")

# 4
d2 >> play('<vVvVv [----]>', dur=PDur(3, 8), sample=4, pan=[-1, 1], amp=PWhite(0.5 , 0.8))

