"""disperse	 흩어지게 하다, 퍼뜨리다	scatter, spread, disseminate
adjacent	인접한	nearby, neighboring, adjoining
sequence	연속, 순서	progression, series, order
detect	발견하다	discover, find, identify
flexible	유연한, 적응성 있는	pliable, bendable, adaptable
surpass	능가하다	exceed, outrun, be higher than
invariable	변함없는	constant, consistent, unchanging
dramatic	극적인, 인상적인	striking, significant, impressive
master	습득하다	learn thoroughly, learn, acquire
assimilate	(지식 등을)흡수하다, 이해하다	absorb, take in, digest
overwhelming	압도적인, 굉장한	powerful, enormous, compelling
curious	호기심이 강한; 이상한, 별난	inquisitive, questioning,strange
alteration	변화, 수정	change, modification
consequence	결과; 중요성	result, effect, ramification, importance
deceive	속이다	mislead, delude, cheat
ample	넓은, 광대한; 풍부한	sizable, large, plentiful
resilient	금방 회복하는	quick to recover, easy to recover
detach	분리하다	separate, disconnect, disengage
account	(사건 등에 대한) 기술, 보고	description, report, narrative
equilibrium	균형	balance, symmetry
surmise	추측하다	infer, guess, speculate
unsuitable	적합하지 않은	inappropriate, unfit, improper
imaginative	창의적인	creative, inventive, original
imposing	인상적인	impressive, striking
vitality	활력	energy, liveliness, vigor"""
text="""vehicle	수단, 매체	means, medium, instrument
hitherto	지금까지	previously, so far, until now
plague	괴롭히다	cause a problem for, bother, annoy
domain	영역	area, field
indifferent	무관심한	uninterested, unconcerned, careless
champion	옹호하다	support, promote, advocate
deteriorate	악화되다	get worse, degenerate
assault	폭행하다, 공격하다	attack, aggress, assail
appropriate	적절한	suitable, proper, applicable
adept	능숙한	skillful, proficient, deft
indeed	사실은	in truth, in fact
pursuit	취미, 오락	interest, pastime, hobby
incite	자극하다	stimulate, provoke, inflame
guarantee	보장하다	ensure, secure, warrant
prosperity	번영	economic well-being, wealth, fortune
primarily	주로; 원래, 처음에	mostly, mainly, originally"""
text="""erupt	폭발하다	explode, burst, blow up
trace	자취, 흔적	evidence, vestige, imprint
prestigious	명성이 있는	highly regard, respected, esteemed
shape	(영향을 미쳐)형성하다	affect, form, influence
inflict	(고통 등을) 주다, 가하다	cause, exact, administer
portion	부분	part, segment, fragment
coincidence	우연의 일치	chance happening
propel	몰아대다	push, force, drive
thoroughly	철저히, 완전히	completely, entirely
contemplate	곰곰이 생각하다	consider, ponder
unethical	비윤리적인	improper, immoral
replicate	모사하다, 복제하다	reproduce, copy, duplicate
hasty	황급한, 서두르는	hurried, rushed
representative	나타내는; 전형적인	indicative, typical, exemplary
range	범위	scope, spectrum, extents"""

data=[x.split('\t') for x in text.split('\n')]
data


D=dict()
for a,b,c in data:
    D[b]=[a]+[x.strip() for x in c.split(',')]

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