#ivedami du skaicia. did priskirti didziausia o mz maziausia
#nenaudoti min ir max funkciju

a = int(input('a=...'))
b = int(input('b=...'))

if a > b:
    did = a
    maz = b
else:
    did = b
    maz = a
print(f'{did} yra didesnis uz maz{maz}')