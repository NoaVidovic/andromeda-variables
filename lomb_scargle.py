import numpy as np

from astropy.timeseries import LombScargle

from util import where_eq


MIN_PERIOD = 10  # day
MAX_PERIOD = 1000  # day

MIN_FREQ = 1/MAX_PERIOD
MAX_FREQ = 1/MIN_PERIOD


def lomb_scargle(band, epoch_data, sid_list):
    if band not in ('G', 'BP', 'RP'):
        print('Invalid band')
        return

    data_filtered_band = where_eq('band', band, epoch_data)

    freqs, powers = [], []
    for sid in sid_list:
        tmp = where_eq('source_id', sid, data_filtered_band)
        t, mag = tmp['time'], tmp['mag']

        frequency, power = LombScargle(t, mag).autopower(minimum_frequency=MIN_FREQ, maximum_frequency=MAX_FREQ)

        freqs.append(frequency)
        powers.append(power)
        
    return dict(zip(sid_list, zip(freqs, powers)))

def top_freqs(freqs, powers, n=3):
    ind = np.argpartition(powers, -n)[-n:]  # gets the indexes of the n frequencies with the highest power
    return freqs[ind]