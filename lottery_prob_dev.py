#
# 확률 분포
#

PDF = [0] * 55  # 각 숫자합이 발생한 횟수를 여기에 저장
for i0 in range(10):
    for i1 in range(10):
        for i2 in range(10):
            for i3 in range(10):
                for i4 in range(10):
                    for i5 in range(10):
                        PDF[i0 + i1 + i2 + i3 + i4 + i5] += 1

for i in range(55):
    print(f'{i:>2} ==> {PDF[i]:>6,}')

#
# 확률 분포 (누적)
#

CDF = [0] * 55  # 각 숫자합이 발생한 횟수를 누적해 가며 여기에 저장
for i in range(55):
    CDF[i] = CDF[i-1] + PDF[i]

for i in range(55):
    print(f'{i:>2} ==> {CDF[i]:>9,}')

#
# 당첨 숫자 예측
#

rate = 17
print(f'경쟁률 [{rate} 대 1]')

percentile = 1.0 - (1.0 / rate)
print(f'목표 백분위 : {percentile * 100.0}+')

percentile *= 1000000
predict = 0
for i in range(55):
    if percentile < CDF[i]:
        predict = i
        break

print(f'당첨되려면 아마도 {predict} 이상이 필요할거에요~')
