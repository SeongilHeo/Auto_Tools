text="""simultaneous	동시에	synchronous, happening at the same time, concurrent
vast	광대한, 거대한	immense, great, extensive
reluctant	꺼리는 	unwiling, loath, disinclined
conjecture	추측	supposition, guess, speculation
embed	박아넣다	insert, fix, implant
vow	맹세, 서약	pledge, promise, oath
counter	반박하다	oppose, act against, refute
apparent	분명한, 외견상의	clear, evident, seeming
bombard	폭격하다	attack, assail, strike
reveal	밝히다, 드러내다	unveil, make known, show
sturdy	튼튼한	robust, strong, well-built
traditionally	전형적인 	typically
correspondingly	그에 상응하는	similarly, likewise
trigger	일으키다	generate, cause, initate
vigorous	강력한, 활기찬, 강건한	energetic, strong, forceful
spontaneous	자발적인	automatic, voluntary, unprompted
miniature	소형의	tiny, small, diminutive
commission	의뢰하다	hire, order
remarkable	놀라운, 주목할만한	notable, incredible, extraordinary
effort	노력	exertion, endeavor, attempt
manifestation	증상	symptom, sign, indication
prior	이전의	eariler, former, previous
cast about	찾아다니다	seek, hunt, search
rigorous	엄격한, 혹독한	strict, severe, harsh
compulsory	의무적인	obligatory, forced, required
subsidiary	부수적인	subordinate, less important, auxiliary
status	지위, 위신	standing, prestige, importance
emphasize	강조하다	highlight, underline, stress
largely	대부분	mostly, mainly, generally
experimental	시험적인	trial, tentative
drain	물을 빼내다	remove water, withdraw liquid graduallay
denote	의미하다, 나타내다	represent, signify, indicate
repudiate	거부하다	reject, declaim
contradictory	모순되는 	paradoxial, conflicting, inconsistent
propagate	번식하다, 증식시키다	reproduce, multiply
ensure	보장하다	guarantee, assure, warrant
pore	작은 구멍	hole, gaze, stare
alternate	번간아 일어나다	rotate, interchange, take turns
devastating	파괴적인 	destructive, ruinous
mingle with	~와 어울리다	mix with, consort with, associate with
continued	계속적인 	ongoing, incessant, constant
attempt	시도하다	endeavor, try, seek
subterfuge	속임수	trick, deception
convert	바꾸다	change, transform
contention	논쟁	debate, disagreement, argument
migrate	이주하다	move around, travel
succession	연속	series, sequence
tentativeness	망설임	hesitation, indecision
fragmentary	단편적인	incomplete, fractional, partial
legendary	전설상의, 유명한	famous, mythical
setback	패배	defeat, reverse
fine-tune	미세하게 조정하다	adjust slightly
enthusiastic	열광적인	zealous, ardent, eager
loose	느슨한	slack, relaxed, not strict
portrait	초상화	picture
terminology	전문 용어	vocabulary, language, jargon"""

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