import re,sys,glob
roots=set("SOMEONE THING BODY PART HAPPEN MOVE THINK KNOW WANT FEEL SEE TOUCH PLACE INSIDE SIDE SAY DO GOOD BIG NEAR ABOVE LIVE SAME MAYBE TIME SEX MANY CAN CONSUME CONTAINER HEAT BEGIN GIVE MATTER RULE FIGHT CHANGE PARTICULAR".split())
part={"E","PI","LA","PE"}
def check(code,maxdict=40):
    c=re.sub(r'"[^"]*"','Q',code)
    errs=[]
    for t in re.findall(r"[A-Za-z@][A-Za-z0-9@]*",c):
        if t=="Q" or re.fullmatch(r"[oiae]?[TNMACDRV]?",t): continue
        if t.isupper() and t not in roots and t not in part: errs.append(t)
        elif t.startswith("@") and not (t[1:].isdigit() and 1<=int(t[1:])<=maxdict): errs.append(t)
    for w in c.split("|")[:-1]:
        pass
    return errs
if __name__=="__main__":
    pat=sys.argv[1]; tot=bad=0
    for f in sorted(glob.glob(pat)):
        for l in open(f):
            m=re.match(r'^\d+\.\s*(.*)',l)
            if not m: continue
            tot+=1; e=check(m.group(1))
            if e: bad+=1
    print(tot,bad)
