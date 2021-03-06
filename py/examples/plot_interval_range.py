# Plot / Interval / Range
# Make a column #plot with each bar representing high/low (or start/end) values.
# Transposing this produces a gantt plot. #interval #range
# ---
import random

from synth import FakeCategoricalSeries
from h2o_wave import site, data, ui

page = site['/demo']

n = 20
f = FakeCategoricalSeries()
v = page.add('example', ui.plot_card(
    box='1 1 4 5',
    title='Interval, range',
    data=data('product low high', n),
    plot=ui.plot([ui.mark(type='interval', x='=product', y0='=low', y='=high')])
))
v.data = [(c, x - random.randint(3, 10), x + random.randint(3, 10)) for c, x, dx in [f.next() for _ in range(n)]]

page.save()
