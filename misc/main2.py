import numpy as np
import time

def create_probability_table(n):
    '''
        n : 각 자리에 가능한 값 갯수. [0,9]라면 10
    '''
    digit = 6
    array_len = ((n - 1) * digit) + 1
    P = np.zeros(array_len, dtype=np.int)  # 각 숫자합(= index)이 발생한 횟수를 여기에 저장
    C = np.zeros(array_len, dtype=np.int)  # 각 숫자합(= index)이 발생한 횟수를 여기에 저장(Cumulative)

    # compute P
    start_time = time.time()
    for i0 in range(n):
        for i1 in range(n):
            start_time1 = time.time()
            for i2 in range(n):
                for i3 in range(n):
                    for i4 in range(n):
                        for i5 in range(n):
                            P[i0 + i1 + i2 + i3 + i4 + i5] += 1
            print(f'DEBUG: i0={i0}, i1={i1}, elapsed_time={time.time() - start_time1}')
    print(f'DEBUG: elapsed_time={time.time() - start_time}')
    assert (n ** digit) == np.sum(P)

    # comput C
    for i in range(len(P)):
        C[i] = C[i-1] + P[i]

    print(repr(P))
    print(repr(C))

    return P, C


# n = 10, scale = 1
# [0, 9]
# array_len : 9 * 6 + 1 = 55
C01 = [      1,       7,      28,      84,     210,     462,     924,
          1716,    3003,    5005,    8002,   12334,   18396,   26628,
         37500,   51492,   69069,   90651,  116578,  147070,  182197,
        221859,  265776,  313488,  364365,  417627,  472374,  527626,
        582373,  635635,  686512,  734224,  778141,  817803,  852930,
        883422,  909349,  930931,  948508,  962500,  973372,  981604,
        987666,  991998,  994995,  996997,  998284,  999076,  999538,
        999790,  999916,  999972,  999993,  999999, 1000000]

# n = 10, scale = 4
# [0, 9] ==> [0, 39]
# array_len : 39 * 6 + 1 = 235
C_10_4 = [      1,          7,         28,         84,        210,
              462,        924,       1716,       3003,       5005,
             8008,      12376,      18564,      27132,      38760,
            54264,      74613,     100947,     134596,     177100,
           230230,     296010,     376740,     475020,     593775,
           736281,     906192,    1107568,    1344904,    1623160,
          1947792,    2324784,    2760681,    3262623,    3838380,
          4496388,    5245786,    6096454,    7059052,    8145060,
          9366813,   10737531,   12271344,   13983312,   15889440,
         18006688,   20352976,   22947184,   25809147,   28959645,
         32420388,   36213996,   40363974,   44894682,   49831300,
         55199788,   61026841,   67339839,   74166792,   81536280,
         89477388,   98019636,  107192904,  117027352,  127553335,
        138801313,  150801756,  163585044,  177181362,  191620590,
        206932188,  223145076,  240287509,  258386947,  277469920,
        297561888,  318687096,  340868424,  364127232,  388483200,
        413954178,  440556046,  468302584,  497205352,  527273580,
        558514068,  590931096,  624526344,  659298822,  695244810,
        732357808,  770628496,  810044704,  850591392,  892250640,
        935001648,  978820746, 1023681414, 1069554312, 1116407320,
       1164205588, 1212911596, 1262485224, 1312883832, 1364062350,
       1415973378, 1468567296, 1521792384, 1575594952, 1629919480,
       1684708768, 1739904096, 1795445394, 1851271422, 1907319960,
       1963528008, 2019831996, 2076168004, 2132471992, 2188680040,
       2244728578, 2300554606, 2356095904, 2411291232, 2466080520,
       2520405048, 2574207616, 2627432704, 2680026622, 2731937650,
       2783116168, 2833514776, 2883088404, 2931794412, 2979592680,
       3026445688, 3072318586, 3117179254, 3160998352, 3203749360,
       3245408608, 3285955296, 3325371504, 3363642192, 3400755190,
       3436701178, 3471473656, 3505068904, 3537485932, 3568726420,
       3598794648, 3627697416, 3655443954, 3682045822, 3707516800,
       3731872768, 3755131576, 3777312904, 3798438112, 3818530080,
       3837613053, 3855712491, 3872854924, 3889067812, 3904379410,
       3918818638, 3932414956, 3945198244, 3957198687, 3968446665,
       3978972648, 3988807096, 3997980364, 4006522612, 4014463720,
       4021833208, 4028660161, 4034973159, 4040800212, 4046168700,
       4051105318, 4055636026, 4059786004, 4063579612, 4067040355,
       4070190853, 4073052816, 4075647024, 4077993312, 4080110560,
       4082016688, 4083728656, 4085262469, 4086633187, 4087854940,
       4088940948, 4089903546, 4090754214, 4091503612, 4092161620,
       4092737377, 4093239319, 4093675216, 4094052208, 4094376840,
       4094655096, 4094892432, 4095093808, 4095263719, 4095406225,
       4095524980, 4095623260, 4095703990, 4095769770, 4095822900,
       4095865404, 4095899053, 4095925387, 4095945736, 4095961240,
       4095972868, 4095981436, 4095987624, 4095991992, 4095994995,
       4095996997, 4095998284, 4095999076, 4095999538, 4095999790,
       4095999916, 4095999972, 4095999993, 4095999999, 4096000000]

# n = 10, scale = 5
# [0, 9] ==> [0, 49]
# array_len : 49 * 6 + 1 = 295





# def get_probable_num(rate, n_event, C):
#     if rate < 1.0:
#         return 0
#     percentile = (1 - (1 / rate)) * n_event
#     if percentile >= n_event:
#         return (len(C) - 1)
#     for i in range(len(C)):
#         if percentile <= C[i]:
#             return i
#     raise Exception('hmm')

def get_probable_num2(percentile, n_event, C):
    if percentile < 0.0:
        return 0
    if percentile >= 1.0:
        return (len(C) - 1)
    percentile *= n_event
    for i in range(len(C)):
        if percentile <= C[i]:
            return i
    raise Exception('hmm')

def run(rate):
    digit = 6
    n = 10  # [0, 9]

    scale = 1  # [0,  9]
    # scale = 2  # [0, 19]
    # scale = 3  # [0, 29]
    # scale = 4  # [0, 39]
    # scale = 5  # [0, 49]

    scaled_n = n * scale
    n_event = scaled_n ** digit
    diff_n = scaled_n - n

    if rate < 1.0:
        rate = 1.0

    # 백분위 경쟁률
    percentile = 1.0 - (1.0 / rate)
    print(f'DEBUG: Target percentile : {percentile * 100.0}+')

    create_prob_table = True
    if create_prob_table:
        P, C = create_probability_table(scaled_n)
    else:
        C = C_10_4

    middle_idx = len(C) // 2
    print(f'DEBUG: n={n}, len(C)={len(C)}, middle_idx={middle_idx}')

    scaled_solution = get_probable_num2(percentile, n_event, C)
    print(f'DEBUG: scaled_solution={scaled_solution}')

    denominator = (scaled_n - 1) / (n - 1)
    print(f'DEBUG: denominator : {denominator}')

    solution = scaled_solution/denominator
    # print(f'Maybe you need {solution} or more.')
    print(f'당첨되려면 아마도 {solution} 이상이 필요할거에요~')

run(3600)
