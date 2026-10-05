import re,sys,glob
roots=set("GOOD BIG NEAR ABOVE LIVE SAME TIME INSIDE PART SIDE KNOW WANT HEAT BEGIN GIVE TOUCH MATTER SEX HAPPEN THINK CAN MANY SOMEONE THING MOVE FEEL RULE CHANGE PARTICULAR ART JOIN VALUE CARE TONE CONSUME ABSTRACT MEASURE LONG SAY GRAIN FIGHT BODY SEE DO PLACE TEXT".split())
part={"E","PI","LA","PE","AND"}
def check(code,maxdict=40):
    c=re.sub(r'"[^"]*"','Q',code)
    errs=[]
    for t in re.findall(r"[A-Za-z@][A-Za-z0-9@]*",c):
        if t=="Q" or re.fullmatch(r"[oiae]?[TNMACDRVIK]?",t): continue
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
