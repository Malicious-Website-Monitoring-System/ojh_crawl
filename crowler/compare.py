from collections import Counter

def classify_url(x, y, z):
    # 웹툰
    common_keys_xy = x.keys() & y.keys()
    sum_y = sum(x[key] for key in common_keys_xy)  # 공통 키에서 y의 빈도수를 합산
    if sum_y >= 4:  # 빈도수 합이 특정값보다 크면 '무료웹툰'을 반환
        return '무료웹툰'

    # 도박
    common_keys_xz = x.keys() & z.keys()
    sum_z = sum(x[key] for key in common_keys_xz)  # 공통 키에서 x의 빈도수를 합산
    if sum_z >= 8:  # 빈도수 합이 특정값보다 크면 '도박'을 반환
        return '도박'
    
    return '정상'  # 위의 조건을 모두 만족하지 않으면 '정상'을 반환


