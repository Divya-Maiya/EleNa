import json

def test_server_start(test_client):
    response = test_client.get('/')
    assert response.status_code == 200

def test_post_data(test_client):
    request_body = {
        "algorithm": "Dijkstra",
        "start": "Brandywine Dr, Amherst, MA 01002",
        "dest": "Rolling Green Drive, Amherst, MA 01002",
        "mode": "max",
        "limit": 50,
        "city": "Amherst"
    }
    expected_response = \
        {
    "path": [
        [
            -72.532612,
            42.406836
        ],
        [
            -72.532467,
            42.406033
        ],
        [
            -72.532283,
            42.404933
        ],
        [
            -72.5306636,
            42.4050095
        ],
        [
            -72.529686,
            42.404986
        ],
        [
            -72.529687,
            42.404537
        ],
        [
            -72.529264,
            42.403496
        ],
        [
            -72.528496,
            42.402328
        ],
        [
            -72.52805,
            42.398794
        ],
        [
            -72.52807,
            42.398044
        ],
        [
            -72.527685,
            42.396801
        ],
        [
            -72.5271308,
            42.3955888
        ],
        [
            -72.5271008,
            42.3952846
        ],
        [
            -72.5271111,
            42.3952655
        ],
        [
            -72.5270352,
            42.395106
        ],
        [
            -72.5270134,
            42.3950966
        ],
        [
            -72.526813,
            42.3948838
        ],
        [
            -72.522654,
            42.386922
        ],
        [
            -72.52252,
            42.386783
        ],
        [
            -72.5225601,
            42.3859808
        ],
        [
            -72.5226108,
            42.3858612
        ],
        [
            -72.5224872,
            42.3858248
        ],
        [
            -72.5218793,
            42.3854455
        ],
        [
            -72.5216833,
            42.3850786
        ],
        [
            -72.521259,
            42.384304
        ],
        [
            -72.520714,
            42.383315
        ],
        [
            -72.520048,
            42.382266
        ],
        [
            -72.5196838,
            42.3818572
        ],
        [
            -72.5194327,
            42.3815923
        ],
        [
            -72.5193804,
            42.3814713
        ],
        [
            -72.519268,
            42.381446
        ],
        [
            -72.5190694,
            42.3813486
        ],
        [
            -72.5188682,
            42.3812348
        ],
        [
            -72.517764,
            42.380448
        ],
        [
            -72.516599,
            42.379629
        ],
        [
            -72.516687,
            42.379075
        ],
        [
            -72.515637,
            42.378391
        ],
        [
            -72.515079,
            42.378582
        ],
        [
            -72.513816,
            42.377692
        ],
        [
            -72.5134867,
            42.3771595
        ],
        [
            -72.512862,
            42.375906
        ],
        [
            -72.511444,
            42.375868
        ],
        [
            -72.510099,
            42.375818
        ],
        [
            -72.509776,
            42.375805
        ],
        [
            -72.508494,
            42.375767
        ],
        [
            -72.5063624,
            42.3757117
        ],
        [
            -72.5050498,
            42.3756788
        ],
        [
            -72.504849,
            42.372965
        ],
        [
            -72.5011874,
            42.3729074
        ],
        [
            -72.499927,
            42.372559
        ],
        [
            -72.492426,
            42.366246
        ],
        [
            -72.4897726,
            42.3641006
        ],
        [
            -72.4890161,
            42.3632273
        ],
        [
            -72.488204,
            42.36229
        ],
        [
            -72.487822,
            42.361811
        ]
    ],
    "path_data": [
        {
            "elevation": 50.139,
            "grade": 0,
            "length": 90.08
        },
        {
            "elevation": 49.522,
            "grade": 0.004,
            "length": 123.268
        },
        {
            "elevation": 50.046,
            "grade": 0.007,
            "length": 134.75799999999998
        },
        {
            "elevation": 50.981,
            "grade": 0.034,
            "length": 81.21300000000001
        },
        {
            "elevation": 53.772,
            "grade": 0,
            "length": 49.928000000000004
        },
        {
            "elevation": 53.491,
            "grade": 0.003,
            "length": 122.50299999999999
        },
        {
            "elevation": 53.856,
            "grade": 0.008,
            "length": 144.425
        },
        {
            "elevation": 55.049,
            "grade": 0.019,
            "length": 400.834
        },
        {
            "elevation": 62.486,
            "grade": 0.021,
            "length": 83.426
        },
        {
            "elevation": 64.21,
            "grade": 0.035,
            "length": 142.381
        },
        {
            "elevation": 69.144,
            "grade": 0.017,
            "length": 142.42099999999996
        },
        {
            "elevation": 71.608,
            "grade": 0.002,
            "length": 34.385999999999996
        },
        {
            "elevation": 71.665,
            "grade": 0.003,
            "length": 2.286
        },
        {
            "elevation": 71.671,
            "grade": 0,
            "length": 20.07
        },
        {
            "elevation": 71.449,
            "grade": 0,
            "length": 2.073
        },
        {
            "elevation": 71.431,
            "grade": 0,
            "length": 28.967
        },
        {
            "elevation": 71.115,
            "grade": 0.006,
            "length": 970.0240000000002
        },
        {
            "elevation": 77.277,
            "grade": 0.023,
            "length": 18.982999999999997
        },
        {
            "elevation": 77.707,
            "grade": 0,
            "length": 91.946
        },
        {
            "elevation": 76.968,
            "grade": 0,
            "length": 13.936
        },
        {
            "elevation": 76.786,
            "grade": 0.03,
            "length": 10.929
        },
        {
            "elevation": 77.111,
            "grade": 0.021,
            "length": 66.00399999999999
        },
        {
            "elevation": 78.528,
            "grade": 0.024,
            "length": 43.915
        },
        {
            "elevation": 79.567,
            "grade": 0.029,
            "length": 92.92599999999999
        },
        {
            "elevation": 82.234,
            "grade": 0.014,
            "length": 118.735
        },
        {
            "elevation": 83.893,
            "grade": 0.023,
            "length": 128.95000000000002
        },
        {
            "elevation": 86.886,
            "grade": 0.016,
            "length": 54.474000000000004
        },
        {
            "elevation": 87.733,
            "grade": 0,
            "length": 36.205
        },
        {
            "elevation": 87.596,
            "grade": 0,
            "length": 14.896
        },
        {
            "elevation": 87.45,
            "grade": 0,
            "length": 9.871
        },
        {
            "elevation": 87.295,
            "grade": 0,
            "length": 19.86
        },
        {
            "elevation": 87.081,
            "grade": 0,
            "length": 20.838
        },
        {
            "elevation": 87.012,
            "grade": 0,
            "length": 126.018
        },
        {
            "elevation": 86.877,
            "grade": 0.014,
            "length": 132.099
        },
        {
            "elevation": 88.691,
            "grade": 0.035,
            "length": 62.025
        },
        {
            "elevation": 90.89,
            "grade": 0.062,
            "length": 114.993
        },
        {
            "elevation": 98.005,
            "grade": 0,
            "length": 50.702
        },
        {
            "elevation": 94.967,
            "grade": 0.015,
            "length": 143.414
        },
        {
            "elevation": 97.075,
            "grade": 0,
            "length": 65.672
        },
        {
            "elevation": 95.259,
            "grade": 0,
            "length": 148.529
        },
        {
            "elevation": 85.279,
            "grade": 0,
            "length": 116.55799999999999
        },
        {
            "elevation": 79.76,
            "grade": 0,
            "length": 110.62700000000001
        },
        {
            "elevation": 74.605,
            "grade": 0,
            "length": 26.572
        },
        {
            "elevation": 72.915,
            "grade": 0,
            "length": 105.39499999999998
        },
        {
            "elevation": 67.395,
            "grade": 0,
            "length": 175.22
        },
        {
            "elevation": 61.813,
            "grade": 0,
            "length": 107.887
        },
        {
            "elevation": 61.139,
            "grade": 0,
            "length": 302.42
        },
        {
            "elevation": 55.866,
            "grade": 0,
            "length": 300.86199999999997
        },
        {
            "elevation": 54.599,
            "grade": 0,
            "length": 115.01599999999999
        },
        {
            "elevation": 54.298,
            "grade": 0,
            "length": 934.7780000000001
        },
        {
            "elevation": 52.551,
            "grade": 0,
            "length": 323.2459999999999
        },
        {
            "elevation": 49.602,
            "grade": 0.031,
            "length": 115.803
        },
        {
            "elevation": 53.196,
            "grade": 0.027,
            "length": 123.755
        },
        {
            "elevation": 56.518,
            "grade": 0.017,
            "length": 61.822
        },
        {
            "elevation": 57.545,
            "length": 0
        }
    ]
}
    request_json = json.dumps(request_body)
    actual_response = test_client.post('/route', data = request_json,content_type='application/json')
    assert actual_response.status_code==200

