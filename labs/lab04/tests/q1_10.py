OK_FORMAT = True

test = {   'name': 'q1_10',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> weather_sub_pivot.shape\n'
                                               '(2, 27)',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> np.isin(np.round(np.array(weather_sub_pivot["Breezy"])), np.array([1., 8.]))\n'
                                               'array([ True,  True])',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
