OK_FORMAT = True

test = {   'name': 'q1_2',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> # Correlation is a number '
                                               'between -1 and 1;\n'
                                               '>>> -1 <= '
                                               'pick_length_correlation <= 1\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'np.round(pick_length_correlation, '
                                               '3) == -0.165\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
