text="""merely	단지	simply, only, no more than
decimate	(많은 사람을) 죽이다	destroy, eliminate, wipe out
incentive	동기, 자극	motivation, motive, encouragement
retrieve	되찾다	bring back, get back, recover
compress	압축하다	condense, compact, contract
designate	명시하다	indicate, identify, specify
dissemination	보급, 유포	spread, distribution, diffusion
marked	두드러진, 현저한	noticeable, considerable, prominent
hypothetical	가상의, 가정의	supposed, imaginary
flow	흐름; 이동	stream, current, movement, motion
precise	정확한	exact, accurate, definite
stipulate	(조건으로서) 요구하다	require, demand, call for
perspective	관점	point of view, viewpoint, orientation
enhance	향상시키다	improve, enrich, intensify
fundamental	근본적인, 기본적인	essential, basic, primary
evident	분명한	clear, apparent, obvious
shift	옮기다, 바꾸다	move, transfer, change
unique among	~중에서 유일무이한	different from other
full-fledged	완전히 발달한	well-developed, full-blown
laborious	인내를 요하는, 힘든	difficult, strenuous
emit	내뿜다, 방출하다	give off, exhale, release
stunning	놀랄 만큼 멋진	amazing, impressive, breathtaking
tantalizing	흥미를 돋우는; 감질나는	tempting, enticing, teasing
abandoned	버려진	no longer occupied, deserted, vacant
transmit	전하다	convey, communicate, send
candidly	솔직히	honestly, frankly, plainly
compulsorily	의무적으로	by requirement, obligatorily, mandatorily
aid	도다	assist, support, help
deliberation	토의	discussion, debate, conference
preposterous	터무니없는	unbelievable, absurd, nonsensical
sparse	드문드문한; 부족한	scattered, thinly distributed
occasionally	가끔	scanty, meager, scarce, limited
inconceivable	상상도 할 수 없는	once in a while, now and them, sometimes
breeding	번식	unthinkable, unimaginable
overriding	가장 중요한	reproduction, propagation
favor	더 좋아하다	dominant, chief, principal
sediment	침전물	prefer, lean toward
clever	영리한	remains, deposition
consistently	일관되게	ingenious, smart, brilliant
rate	평가하다	regularly, typically, unchangingly
predominate	우세하다; 지배적인, 우세한	judge, assess, evaluate
realize	깨닫다, 이해하다; 달성하다, 실현하다	outweigh, prevail, most popular
circuitous	우회하는	be aware of, understand, achieve
owing to	~ 때문에	due to, because of, as a result of
model	견본	specimen, prototype, example
with respect to	~에 관하여	with regard to, in terms of, in reference to
continuous	계속되는	uninterrupted, ongoing, unceasing
collaborate	협력하다	cooperate, put effort together, work together
anonymous	익명의, 신원 불명의	unknown, unnamed, unidentified
somewhat	어느 정도	to some degree, to some extent, rather
damaging	해로운	harmful, detrimental, noxious
dramatically	극적으로, 몹시	greatly, substantially, remarkably
highten	고조시키다	increase, intensify
share	몫	portion, part, allotment
shortly	곧	soon, presently
besides	게다가; ~외에	in addition, moreover, apart from
seep	스며 나오다	ooze, flow slowly, pass through slowly
habit	습관	usual behavior, custom, practice"""

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