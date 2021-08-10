test = {   'name': 'q1',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> # chances are less than 5.8 in 10^20 that this test fails when the function is correct;\n'
                                               '>>> sum((4 in simple_resample(100)) for _ in range(10000)) in range(6323-150,6323+150)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> len(simple_resample(1000)) == 1000\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
