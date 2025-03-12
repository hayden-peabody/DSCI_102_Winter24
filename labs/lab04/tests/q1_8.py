OK_FORMAT = True

test = {   'name': 'q1_8',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> precip_tab.shape\n'
                                               '(2, 27)',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> np.isin(np.array(precip_tab["Breezy"]), np.array([42, 12]))\n'
                                               'array([ True,  True])',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
