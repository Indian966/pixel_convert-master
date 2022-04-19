import pandas as pd


def rgb2dmc(rgb) :
    dmc_list = pd.read_csv('static/resource/DMC Cotton Floss converted to RGB Values.csv',
                      encoding=' CP949', engine='python')
    res = [[999, 'hello world']]
    for i in range(len(dmc_list)):
        r, g, b = dmc_list.loc[i][2], dmc_list.loc[i][3], dmc_list.loc[i][4]
        gap = abs(r - rgb[0]) + abs(g - rgb[1]) + abs(b - rgb[2])

        if res[-1][0] > gap:
            res.append([gap, dmc_list.loc[i][0]])
    return res[-1][1]

def dmc2rgb(dmc_code) :
    dmc_list = pd.read_csv('static/resource/DMC Cotton Floss converted to RGB Values.csv',
                           encoding=' CP949', engine='python')
    row = dmc_list.loc[(dmc_list['Floss#'] == str(dmc_code))]
    r, g, b = int(row['Red'].values), int(row['Green'].values), int(row['Blue'].values)
    result = [r, g, b]
    return result

# def color_check (color, dmc_code) :
#     if color