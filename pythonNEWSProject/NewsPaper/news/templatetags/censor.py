from django import template


register = template.Library()
baza_slov = ['редис', 'капуст', 'морков']


@register.filter()
def censor(a):
    b = a.lower()
    c = b.split('. ')
    for i in baza_slov:
        if b.find(i) + 1 > 0:
            for j in c:
                if j.find(i) + 1 > 0:
                    r = j.split()
                    f = c.index(j)
                    for k in r:
                        if k.find(i) + 1 > 0:
                            if not k.isalpha():
                                e = k[0] + ('*' * (len(k) - 2)) + k[-1]
                                j = j.replace(k, e)
                            else:
                                e = k[0] + ('*' * (len(k) - 1))
                                j = j.replace(k, e)
                    c[f] = j
    d = []
    for item in c:
        d.append(item.capitalize())
    a = '. '.join(d)
    return a

