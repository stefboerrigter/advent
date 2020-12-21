#from parse import parse
import re


"""

    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID) [Optional]
"""

def initializeList():
    with open('input.txt', 'r') as file:
        lst = file.read().split('\n\n')
        lst = [x.replace('\n', ' ').split() for x in lst]
        passports = []
        for person in lst:
            passports.append(dict(data.split(':') for data in person))
    
        passports = [x for x in passports if len(x.keys()) == 8 or (len(x) == 7 and 'cid' not in x.keys())]
        print("Part 1; passports valid {0}".format(len(passports)))
         
        valid_passports = []

        values = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        for person in passports:
            if (1920 <= int(person['byr']) <= 2002
                    and (2010 <= int(person['iyr']) <= 2020)
                    and (2020 <= int(person['eyr']) <= 2030)
                    and
                    ((person['hgt'][-2:] == 'cm' and 150 <= int(person['hgt'][:-2]) <= 193)
                    or (person['hgt'][-2:] == 'in' and 59 <= int(person['hgt'][:-2]) <= 76))
                    and (re.match(r'#[\da-f]{6}', person['hcl']))
                    and (person['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
                    and (re.match(r'\d{9}', person['pid']))):
                valid_passports.append(person)
        print("Part 2; passports valid {0}".format(len(valid_passports) - 1))

initializeList()
