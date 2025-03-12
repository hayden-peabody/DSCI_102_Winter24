OK_FORMAT = True

test = {
  'name': 'q2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.isin(["htn_yes","htn_no","ane_yes","ane_no"], features.columns)
          array([ True,  True,  True,  True])
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.unique(features["htn_yes"]) == np.array([0,1])
          array([ True,  True])
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
