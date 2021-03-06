var CDF = [    1,       7,      28,      84,     210,     462,     924,
            1716,    3003,    5005,    8002,   12334,   18396,   26628,
           37500,   51492,   69069,   90651,  116578,  147070,  182197,
          221859,  265776,  313488,  364365,  417627,  472374,  527626,
          582373,  635635,  686512,  734224,  778141,  817803,  852930,
          883422,  909349,  930931,  948508,  962500,  973372,  981604,
          987666,  991998,  994995,  996997,  998284,  999076,  999538,
          999790,  999916,  999972,  999993,  999999, 1000000];

// 경쟁률이 [3.5 대 1] 이면 rate = 3.5
function predict(rate) {
    if (rate < 1) return 0;
    var pct = (1 - (1 / rate)) * CDF[CDF.length-1];
    n = CDF.length
    for (i=0; i<n; ++i)
        if (pct < CDF[i])
            return i;
    return n - 1
}

ret = predict(2.0)
console.log(ret)

ret = predict(1e6)
console.log(ret)
