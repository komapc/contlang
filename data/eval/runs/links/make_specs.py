"""Спецификации вариантов теста связок: A — только PI (как в ../pi_for), B — FROM / FOR / PI, C — FROM / FOR / LIKE / PI.
Порядок вопросов для кодера: первая подходящая связка. Примеры — не цели теста."""
LINKS = {
 "FROM": ('X is made of Y (material, source)', '"drink FROM apple" = cider, "house FROM ice" = igloo'),
 "FOR": ('X is made for Y: to be used with, on or by Y', '"tool FOR hair" = comb, "container FOR flowers" = vase'),
 "LIKE": ('X looks like Y but is not Y', '"fish LIKE sword" = swordfish, "insect LIKE stick" = stick insect'),
 "PI": ('anything else: X is a part of Y, or X is found or lives in Y', '"seed PI fruit" = pip, "edge PI river" = riverbank'),
}
def block(names):
    order = ", ".join(names)
    rows = "\n".join(f"- `{n}` — {LINKS[n][0]} ({LINKS[n][1]})" for n in names)
    return (f"LINKS: two nouns can be joined as `X | o LINK Y | o`. The first word X is always the general kind of the thing; the second word Y only narrows it. "
            f"LINK is one of:\n{rows}\nThe writer asks in this order — {order} — and takes the first that fits. The reader reads each link one way only: "
            + "; ".join({"FROM": "FROM = made of", "FOR": "FOR = made for", "LIKE": "LIKE = looks like", "PI": "PI = part of / found in"}[n] for n in names) + ".")
short = {"B": "`FROM`, `FOR`, `PI` join a noun to the preceding noun (see LINKS).", "C": "`FROM`, `FOR`, `LIKE`, `PI` join a noun to the preceding noun (see LINKS)."}
names = {"B": ["FROM", "FOR", "PI"], "C": ["FROM", "FOR", "LIKE", "PI"]}
OLD_SHORT = "`PI` marks a noun used as a modifier."
OLD_PHR = 'PI = a noun that defines the preceding noun (compound / "of");'
OLD_DEC = "or as two words joined by `PI` (head noun + a noun that defines it, like a compound)"
for v in "BC":
    for kind in ("enc", "dec"):
        s = open(f"spec_{kind}_A.md").read()
        assert OLD_SHORT in s and OLD_PHR in s
        s = s.replace(OLD_SHORT, short[v]).replace(OLD_PHR, " / ".join(names[v]) + " = links between nouns, see LINKS;")
        s = s.replace("PHRASES:", block(names[v]) + "\n\nPHRASES:", 1)
        if kind == "dec":
            assert OLD_DEC in s
            s = s.replace(OLD_DEC, "or as two words joined by a link (" + ", ".join(names[v]) + "; see LINKS)")
        open(f"spec_{kind}_{v}.md", "w").write(s)
print("ok")
