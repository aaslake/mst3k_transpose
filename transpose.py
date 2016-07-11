#!/usr/bin/env python
"""This lets you derive the transpose watchthrough order of MST3k.

Running it will print out the modified order where season 8 is treated like
a 24-episode season, except for the last episode:

101 201 301 401 501 601 701 801 901 1001
302 402 502 602 802
102 202 902 1002
303 403 503 603 803
304 404 504 604 804
103 203 903 1003
305 405 505 605 805
702
306 406 506 606 806
104 204 904 1004
307 407 507 607 807
308 408 508 608 808
105 205 905 1005
309 409 509 609 809
310 410 510 610 810
703
106 206 906 1006
311 411 511 611 811
312 412 512 612 812
107 207 M01 907 1007
313 413 513 613 813
314 414 514 614 814
108 208 908 1008
704
315 415 515 615 815
316 416 516 616 816
109 209 909 1009
317 417 517 617 817
318 418 518 618 818
110 210 910 1010
319 419 519 619 819
705
320 420 520 620 820
111 211 911 1011
321 421 521 621 821
322 422 522 622
112 212 912 1012
323 423 523 623
113 213 324 424 524 624 706 822 913 1013
"""

import json


class Season(object):
  def __init__(self, value, num_episodes):
    self.value = value
    self.num_episodes = num_episodes

  @property
  def numerical_value(self):
    return 6.5 if self.value == 'M' else float(self.value)


class Episode(object):
  def __init__(self, season, number):
    self.season = season
    self.number = number

  def __repr__(self):
    return '%s%02d' % (str(self.season.value), self.number)

  @property
  def numerical_value(self):
    if self.season.num_episodes == 1:
      return 0.5

    num_episodes = self.season.num_episodes
    if num_episodes == 22 and self.number != 22:
      num_episodes = 24

    return float(self.number - 1) / float(num_episodes - 1)


seasons = [
  Season(1, 13),
  Season(2, 13),
  Season(3, 24),
  Season(4, 24),
  Season(5, 24),
  Season(6, 24),
  Season('M', 1),
  Season(7, 6),
  Season(8, 22),
  Season(9, 13),
  Season(10, 13),
]

episodes = [
  Episode(season, episode)
  for season in seasons
  for episode in range(1, season.num_episodes + 1)
]

episodes.sort(key=lambda e: (e.numerical_value, e.season.numerical_value))

last_season = 0
line = []
for episode in episodes:
  if episode.season.numerical_value < last_season:
    print ' '.join(str(_) for _ in line)
    line = []

  line.append(episode)
  last_season = episode.season.numerical_value

if line:
  print ' '.join(str(_) for _ in line)
  line = []
