# coding: utf-8
"""
======================
Using display.specshow
======================

This notebook gives a more in-depth demonstration of all things that `specshow`
can do to help generate beautiful visualizations of spectro-temporal data.

"""

# Code source: Brian McFee
# License: ISC
# sphinx_gallery_thumbnail_number = 6

# %%
# All of librosa's plotting functions rely on matplotlib.
# To demonstrate everything we can do, it will help to
# import matplotlib's pyplot API here.
import numpy as np
import matplotlib.pyplot as plt

import librosa

# %%
# First, we'll load in a demo track

y, sr = librosa.load("my_stammer.wav")


# %%
# The first thing we might want to do is display an ordinary
# (linear) spectrogram.
# We'll do this by first computing the short-time Fourier
# transform, and then mapping the magnitudes to a decibel
# scale.
#

D = librosa.stft(y)  # STFT of y
S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)

# %%
# If you're familiar with matplotlib already, you may know
# that there are two ways of using it: the `pyplot` interface
# and the object-oriented interface.
# Both are supported by librosa, as we'll show here.
#
# First, the pyplot interface:

# %%
# And now the object-oriented interface
fig, ax = plt.subplots()
# %%
# Note that only the parameters which are strictly necessary are supported by
# `specshow`.  For example, without the `hop_length`, we wouldn't know how to
# translate frame indices to time indices.
#
# A full list of the supported parameters is provided in the
# `librosa.display.specshow` documentation.

# %%
# Other types of spectral data
# ----------------------------
# The examples above illustrate how to plot linear spectrograms,
# but librosa provides many kinds of spectral representations:
# Mel-scaled, constant-Q, variable-Q, chromagrams, tempograms, etc.
#
# specshow can plot these just as well.  For example, a Mel spectrogram
# can be displayed as follows:

fig, ax = plt.subplots()
M = librosa.feature.melspectrogram(y=y, sr=sr)
M_db = librosa.power_to_db(M, ref=np.max)
img = librosa.display.specshow(M_db, y_axis='mel', x_axis='time', ax=ax)
ax.set(title='Mel spectrogram display')
fig.colorbar(img, ax=ax, format="%+2.f dB")

plt.show()
# %%
# Conclusion
# ----------
# This series of examples demonstrates most of the functionality of
# `librosa.display.specshow`, but it does not exhaustively show
# every option, e.g., for axis decoration.
# Interested readers should look through the rest of the API
# documentation to see how these other options can be used
# effectively.
