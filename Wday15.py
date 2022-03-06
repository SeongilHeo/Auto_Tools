text="""intact	손상되지 않은	undamaged, unbroken, whole
albeit	비록 ~이지만	although, even though, though
complex	복잡한	intricate, complicated, elaborate
conventional	전통적인; 통례의	traditional, customary, standard
reasonable	합리적인; 적당한	sensible, rational, logical
attainment	성취	achievement, accomplishment, fulfillment
progressively	점진적으로	increasingly
drawback	결점	disadvantage, problem, defect
suppress	억제하다, 참다	hold back, restrain
incidentally	덧붙여 말하자면, 그런데	by the way
tactic	전략	strategy, maneuver
substantial	상당한	considerable, significant, large
verify	입증하다	confirm, establish the truth of, validate
sustained	지속적인	continued, constant, uninterrupted
radical	근본적인, 극단적인	fundamental, basic, extreme
prime	최고의, 주요한	peak, high-quality, superior
grasp	이해하다	understand, catch, comprehend
prominently	눈에 띄게	very noticeably, conspicuously, notably
precipitate	재촉하다, 촉진하다	bring about, cause, give rise to
interlock	서로 맞물리다	link, connect, join
accordingly	그에 따라서	consequently, for that reason
relevant	관련된, 적절한	applicable,
remarkably	신기하게도	surprisingly
disputable	논란의 여지가 있는	challengeable, debatable
ambitious	야심 있는	desiring success, aspiring
congeal	굳다, 응고하다	solidify, harden, stiffen
cautious	신중한, 조심성 있는	careful, wary, prudent"""
text="""realm	영역, 범위	field, area, sphere
dam	막다	block, obstacle
flattery	아첨	praise
amplify	확대하다, 증대하다	increase, magnify, enlarge
dimension	크기, 규모	size, magnitude
deplete	다 써버리다, 대폭 감소시키다	exhaust, reduce, empty
characteristic	특유의; 특징, 특성	distinctive, peculiar, special
ice sheet	대륙 빙하	glacier
spectator	관객, 구경꾼	viewer, onlooker
bountifully	풍부하게	plentifully, abundantly, copiously
suffer paralysis	마비를 겪다	lose the ability to move
variation	변동, 차이	fluctuation, variance, different
periphery	주변	boundary, border, edge
apparently	외관상으로	seemingly"""
"""far-reaching	광범위한	extensive, widespread, bread
embody	구체적으로 나타내다, 포함하다	incarnate, represent, manifest
evade	피하다	avoid, escape, elude
against	~에 붙여, ~에 가까이	next to, beside
due to	~로 인한, ~에 기인하는	caused by, owing to, attributable to
classify	분류하다	categorize, arrange, assort
oblige	강요하다	compel, force, require
identical	동일한	same, equal, indistinguishable
intimately	친밀하게	closely
questionable	의심스러운	doubtful, dubious, suspicious
spot	발견하다	detect, see, find
immerse	잠그다, 담그다	cover, dip, 
not in consensus with	~와 일치하지 않는	not in agreement with
be tempted to	~하고 싶어지다	be inclined to
inception	시작, 개시	beginning"""

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