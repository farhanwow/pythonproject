In [x]: theta = np.radians(30)
In [x]: c, s = np.cos(theta), np.sin(theta)
In [x]: R = np.matrix('{} {}; {} {}'.format(c, -s, s, c))
In [x]: print(R)
[[ 0.8660254 -0.5      ]
 [ 0.5        0.8660254]]
