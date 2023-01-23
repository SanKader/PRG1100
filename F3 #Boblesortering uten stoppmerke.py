#Boblesortering uten stoppmerke

usortert = [5,3,1,2,4]
print('listen før sortering er', usortert)
print()
print()
for m in range(1,5,1):
    print('da starter gjennomgang nr',m)
    for n  in range(0,4,1):
        if usortert[n]>usortert[n+1]:
            #da skal de bytte plass
            bytte=usortert[n]
            usortert[n]=usortert[n+1]
            usortert[n+1]=bytte
            print('resultatet etter bytte nr',n+1,usortert)
        print()
    print()
print('den sorterte lista er:',usortert)
