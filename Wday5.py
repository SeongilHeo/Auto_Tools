text="""compelling	설득력 있는	convincing, persuasive, cogent
ultimately	마침내	eventually, finally, in the end
bulk	큰규모, 대부분	mass, majority, large quantity
incompatible	양립할 수 없는	in conflict, discrepant, contradictory
substantially	상당히 / 대체로 	significantly, considerably, largely
seek	찾다/ 시도하다	look for, attempt, try
unanticipated	예상치 못한	not expected, unforeseen
merge	융합하다	combine, blend, fuse
encounter	마주치다	meet, experience, confront
residue	잔여물	remnant, remainder, remains
circumstance	상황	condition, situation"""
text="""astonishing	놀라운	incredible, amazing, startling
intermittently	간헐적으로	occasionally, periodically, from time to time
application	응용 이용	use, utilization, employment
predominant	주된 주요한	 principal, main, primary
remote	멀리 떨어진	distant, secluded, removed
inordinate	과도한	excessive, exorbitant, undue
launch	시작하다 착수하다	start, begin, initiate
trend	경향 추세	tendency, inclination, direction
embodiment	정형, 구체화된 것	concrete example, epitome
colonize	동식물이 거주하다/ 식민지화하다	inhabit, populate, conquer"""
"""
affect	영향을 미치다	influence, impact, act on
speculation	추측	supposition, conjecture, surmise
compound	더하다 정도를 악화하다	add to, intensify, worsen
fascinating	매력있는	extremely attractive, captivating
combination	유사한 것들의 모임 무리	collection, group, constellation
unconsolidated	굳지 않은	loose, incoherent
outstanding	뛰어난 / 미지불의 처리되지 않은	excellent, remarkable, unpaid
outcome	결과	result, consequence, conclusion
document	문서 기록	record, report, paper
intrinsically	내재적으로 본질적으로	fundamentally, essentially
disputatious	논쟁의 여지가 있는	contentious, argumentative, quarrelsome

diverse	다양한	varied, dissimilar, various
strange	기묘한 이상한	 eerie, odd
tenuous	약한	weak, insubstantial
eradicate	근절하다	remove, root up, extirpate
prone to	~하기 쉬운	likely to get, susceptible to
lodge	박히다	embed, implant
gather momentum	탄력이 붙다	make progress, gain impetus
viable	생존할 수 있는	able to survive
impediment	장애물	obstacle, obstruction, barrier
arid	매마른	dry, barren, sterile
credible	믿을 수 있는	believable, reliable, plausible
vacate	떠나다 비우다	abandon, evacuate, void
cushion	충격을 완화하다	protect, buffer
peculiar	독특한 이상한	unique, distinct, strange
attributable to	~에 기인하는	caused by, ascribable to
enact	법률을 제정하다	make into law, pass, establish
stratified	층으로 이루어진	layered
with regard to	~에 관하여	in terms of, with respect to, concerning
turbulent	격동하는	violent, agitated, tumultuous
appraisal	평가	assessment, evaluation, estimation
erroneous	잘못된	wrong, incorrect, mistaken
proponent	지지자	supporter, advocate, adherent
absolute	절대적인 완전한	unqualified, complete, utter
gratify	만족시키다	satisfy, please"""

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