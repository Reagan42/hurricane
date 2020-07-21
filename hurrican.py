# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day',
         'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen',
         'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix',
         'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September',
          'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August',
          'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September',
          'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980,
         1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185,
                       160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
                  ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'],
                  ['The Bahamas', 'Northeastern United States'],
                  ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'],
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'],
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'],
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'],
                  ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'],
                  ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'],
                  ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'],
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'],
                  ['The Caribbean', 'United States East coast'],
                  ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'],
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'],
                  ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'],
                  ['Central America', 'Yucatn Peninsula', 'South Florida'],
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'],
                  ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'],
                  ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'],
                  ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'],
                  ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'],
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'],
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic',
                   'Turks and Caicos Islands'],
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M',
           '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B',
           '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B',
           '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11, 2068, 269, 318, 107, 65, 19325,
          51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]


# write your update damages function here:
def damage(lst):
    new = []
    for i in lst:
        if i == 'Damages not recorded':
            new.append('Damages not recorded')
        if 'M' in i:
            i = i.strip('M')
            x = float(i) * 1000000
            new.append(x)
        if 'B' in i:
            i = i.strip('B')
            y = float(i) * 1000000000
            new.append(y)
    return new


new_damage = damage(damages)


# write your construct hurricane dictionary function here:

def newdict(names, years, max_sustained_winds, areas_affected, damages, deaths):
    dict = {}
    for i in range(0, 34):
        newdict = {names[i]: {'Name': names[i], 'Year': years[i], 'Max Sustained Winds': max_sustained_winds[i],
                              'Areas Affected': areas_affected[i], 'Damages': damages[i], 'Deaths': deaths[i]}}
        dict.update(newdict)
    return dict


hurdict = newdict(names, years, max_sustained_winds, areas_affected, new_damage, deaths)


# write your construct hurricane by year dictionary function here:
def yeardict(dict):
    ydict = {}
    keys = []
    years = []
    for key in dict.keys():
        keys.append(key)
    for i in dict:
        x = dict[i].get('Year')
        years.append(x)
    yklst = list(zip(years, keys))
    for a in yklst:
        ydict.setdefault(a[0], [])
        ydict[a[0]].append(dict[a[1]])
    return ydict


yeardict = yeardict(hurdict)


# write your count affected areas function here:

def area_count(areas):
    total = []
    area_dict = {}
    for lst in areas:
        for val in lst:
            total.append(val)
    total_set = set(total)
    unique_areas = list(total_set)
    for i in unique_areas:
        new = {i: total.count(i)}
        area_dict.update(new)
    return area_dict


area_dict = area_count(areas_affected)


# write your find most affected area function here:
def most_often(areas):
    biggest = 0
    big = {}
    for i in areas:
        num = areas[i]
        if num > biggest:
            biggest = num
            new = {i: num}
    big.update(new)
    return big


most_often = most_often(area_dict)


# write your greatest number of deaths function here:
def dict2(names, deaths):
    dict = {}
    for i in range(0, 34):
        newdict = {names[i]: deaths[i]}
        dict.update(newdict)
    return dict


deathdict = dict2(names, deaths)


def most_deaths(dict):
    highest = 1
    high = {}
    for i in dict:
        x = dict[i]
        if x > highest:
            highest = x
            newd = {i: x}
    high.update(newd)
    return high


most_death = most_deaths(deathdict)


# write your catgeorize by mortality function here:

def mortality(dict):
    mort = {}
    for i in dict:
        x = dict[i]
        if x >= 10000:
            mortal = 4
        elif x > 1000:
            mortal = 3
        elif x > 500:
            mortal = 2
        elif x > 0:
            mortal = 1
        else:
            mortal = 0
        newmor = {i: mortal}
        mort.update(newmor)
    return mort


mortality = mortality(deathdict)

# write your greatest damage function here:
damage_lst = dict2(names, new_damage)


def most_damage(dam_dict):
    highest = 1
    high = {}
    for i in dam_dict:
        x = dam_dict[i]
        if x != 'Damages not recorded':
            if x > highest:
                highest = x
                new = {i: x}
    high.update(new)
    return high


most_dam = most_damage(damage_lst)

# write your catgeorize by damage function here:

damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

def damage_scale(dam_dict):
    dam = {}
    for i in dam_dict:
        x = dam_dict[i]
        if x == 'Damages not recorded':
            dams = 0
        elif x >= 10000000000:
            dams = 4
        elif x > 1000000000:
            dams = 3
        elif x > 100000000:
            dams = 2
        elif x > 0:
            dams = 1
        else:
            dams = 0
        newdam = {i: dams}
        dam.update(newdam)
    return dam

dam_scale_dict = damage_scale(damage_lst)