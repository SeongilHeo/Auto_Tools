text="""readily	손쉽게, 즉시	easily, quickly, willingly
advocate	지지하다	promote, speak in favor of, proponent
utterly	완전히	completely, totally
abound	풍부하다	overflow, teem, be plentiful
formidable	어마어마한, 만만치 않은	impressive, difficult to handle
enormous	거대한	huge, very large, great
disband	해산시키다	dismiss, disperse, break up
alleged	추정의	supposed, assumed
renowned	유명한	famous, celebrated, prominent
versatile	다방면의	adaptable, flexible
prohibitive	값이 엄청나게 비싼	unaffordable, extreme, exorbitant
option	선택	choice, selection
inherent	타고난	innate, built-in, essential
justly	공정하게	rightfully, justifiably, lawfully
provoke	불러일으키다	incite, bring about, give rise to
impermeable	침투되지않은	impenetrable, impervious
momentous	중대한	significant, major, meaningful
forestall	미연에 방지하다	prevent, hinder, avert
therefore	그 결과	consequently, as a result, thus
persuade	설득하다	convince, induce
proximity	가까움	closeness, nearness
dependable	신뢰할 수 있는	reliable, trustworthy
ensuing	뒤이은	subsequent, following, succeeding
appreciably	상당히	noticeably, significantly, considerably
obligate	의무를 지우다	force, coerce, compel
wholesale	대규모의, 모조리	extensive, mass, completely
dweller	거주자	inhabitant, resident, occupant
tacit	무언의	implicit, implied, unspoken
resolve	해결하다	settle, find a solution for, solve
merit	가치	value, worth, virtue
notion	개념	concept, general idea, opinion
synthesize	통합하다	integrate, combine, coalesce
spectrum	범위	range, scope, extent
stream	흐름	flow, current"""
text="""rupture	파열되다, 불화	burst, break apart, breach
presuppose	가정하다	assume, suppose, presume
well-to-do	부유한	wealthy, affluent, rich
appeal	간청하다	plead, request, ask
accurately	정확하게	correctly, precisely, exactly
fastidious	까다로운	demanding, choosy
contraction	감소, 축소	reduction, diminution
stimulus	자극제	impetus, motivation, incentive
track	추적하다	follow, chase, monitor
tame	길들이다	domesticate, train
install	설치하다	put in place, set up, position
chronicle	기록, 연대기	record, history
novel	새로운, 신기한	new, innovative, unusual
isolated	외딴	remote, solitary, secluded
exposed	드러난, 노출된	visible, revealed, uncovered
intermingled	섞인	mixed, combined, blended
succulent	즙이 많은	juicy, pulpy
homogeneous	동종의	unvarying, akin
era	시대	period, epoch, age
threat	위협	intention to harm, menace
foul	더럽히다	pollute, contaminate
prey	희생자	victim
practically	거의	nearly"""

data=[x.split('\t') for x in text.split('\n')]
data


D=dict()
for a,b,c in data:
    D[b]=[a]+[x.strip() for x in c.split(', ')]

L=list(D.keys())
while L:
    print(len(L))
    key=L.pop(0)
    value=list(D[key])
    v_count=len(value)
    print(key,v_count-1,':',end=" ")
    for _ in range(v_count):
        x=input()
        if x not in value:
            print("ㄴ________________________ BEEP")
            continue           
            
        else:
            value.remove(x)
    print(value)
    if value:
        L.append(key)
    for _ in range(len(value)):
        input("--")
    print("----------------------------------------------------------------------------")