OK_FORMAT = True

test = {   'name': 'q1_1',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> weather_sub.shape[1]\n'
                                               '3',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> np.array(weather_sub.columns) == np.array(["Summary", "Temperature (C)", "Humidity"])\n'
                                               'array([ True,  True,  True])',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
