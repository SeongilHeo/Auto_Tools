text="""subsequently	그 후에	later, afterward
explicit	분명한	clear, specific obvious
prevailing	지배적인	dominant, widespread, current
rudimentary	기본적인, 미발달의	basic, elementary, primitive
allude to	~을 넌지시 언급하다	suggest, refer to
assertive	자기주장이 강한	forceful, dogmatic
fuse	녹다, 융합하다	melt, dissolve, combine
transitory	일시적인	short-lived, brief
inviolable	신성한	without exception
supersede	대신하다	replace, displace, supplant
abundant	풍부한	plentiful, bountiful, ample
significant	상당한	considerable, substantial, serious
elaboration	공들여 다듬기	development, improvement
pristine	자연 그대로의	unspoiled, pure
steadily	끊임없이	consistently, continuously
hence	따라서, 그러므로	therefore, consequently, thus
fabricate	만들어 내다	make, produce, build
meet	대처하다	deal with, handle
devour	게걸스럽게 먹다	eat, consume, gulp
amiss	잘못된	wrong, erroneous, faulty
figure out	알아내다	determine, calculate, work out
augment	증가시키다	supplement
trespass	불법 침입하다	invade, encroach, infringe
deduce	추론하다	conclude, infer
quantify	측정하다	measure
aggregation	집단	group, body, assemblage
lax	태만한	careless, neglectful
pace	속도	speed, rate, tempo
inspect	검사하다	examine, scan, check
keen	예리한	sharp, acute
abandon	포기하다	desert, give up
prowess	뛰어난 솜씨	ability, competence, expertise
anyone can see	누가 봐도 알 수 있듯이	it is clear, it is apparent
coarse	거친	rough, crude
impervious	통과할 수 없는	impermeable, resistant, impenetrable
moderate	누그러지다, 온화한	lessen, gentle, temperate
stagnant	활발하지 않은	inactive, sluggish
drive	몰아가다; 추진력	propel, force, ambition
anxiety	걱정	worry, angst, uneasiness
allegedly	전해지는 바에 의하면	supposedly, reportedly
utilize	이용하다	employ, use, make use of
differential	차별적인	uneven, discriminatory
maintain	유지하다	preserve, continue, sustain
jointly	함께	together, in conjunction with, as one
catastrophic	비극적인, 파멸의	disastrous, harmful
aridity	건조함	dryness, waterlessness
paradoxically	역설적으로	contradictorily, surprisingly
archetypal	전형적인	ideal, classic, exemplary
purposely	고의로	intentionally, deliberately, knowingly
collision	충돌	crash, smash
implant	심다, 끼워 넣다	insert, embed
standpoint	관점	perspective, point of view
cue	신호	signal, sign
trappings	장신구	decoration, ornament, adornment
spawn	야기하다	give rise to, create, produce
outbreak	급격한 증가	sudden increase, upsurge"""

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