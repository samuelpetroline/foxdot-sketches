Scale.default="minor"
Root.default=var([0, 5], [32])

k1 >> space([0, 8], dur=(4, 2, 5, 4, 2, 4, 8), room=[3, 1], freq=2, dirty=1, phase=2, sample=2, delay=3, amp=0.3).stop()

k2 >> sitar([4, 2, 8, 0], pan=PWhite(-4, 4), room=2, oct=4).stop()

k3 >> sinepad([2, 2, 2, 2], dur=8, sus=8, blur=2, freq=PWhite(0, 100))

k3 >> pads([2, 8, 0, 4, [4, 3, 6, 3], (4, 3)], dur=1/4, rate=linvar(2, 4))

d1 >> play('<[@@@@]: V>').stop()

d2 >> play(' - - - -').shuffle().stop()

d3 >> play('X ', amp=3).stop()

d4 >> play('ASDG')

d5 >> play('G @ G @')

d6 >> play('<xxxxxxxxxxxxxxxxxxxxxxxxxxXxXX>')
