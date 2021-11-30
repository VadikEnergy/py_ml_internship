#def vectorizer(test.txt)

f = open("test.txt", encoding="utf8")

st = f.readlines()

def translit(name):
    name = str(name)
    dict = {'а': 'a','б': 'b','в': 'v','зг': 'zgh','Зг': 'Zgh','г': 'h','ґ': 'g',
    'д': 'd','е': 'e',"'є": 'ye','є': 'ie','ж': 'zh','з': 'z','и': 'y','і': 'i',
    "'ї": 'yi','ї': 'i','^й': 'y','й': 'i','к': 'k','л': 'l','м': 'm','н': 'n',
    'о': 'o','п': 'p','р': 'r','с': 's','т': 't','у': 'u','ф': 'f','х': 'kh',
    'ц': 'ts','ч': 'ch','ш': 'sh','щ': 'shch','ьо': 'io','ьї': 'ii','ь': '',
    "'ю": 'yu','ю': 'iu',"'я": 'ya','я': 'ia','А': 'A','Б': 'B','В': 'V',
    'Г': 'H','Ґ': 'G','Д': 'D','Е': 'E',"'Є": 'Ye','Є': 'Ie','Ж': 'Zh','З': 'Z',
    'И': 'Y','І': 'I',"'Ї": 'Yi','Ї': 'I',"'Й": 'Y','Й': 'I','К': 'K','Л': 'L',
    'М': 'M','Н': 'N','О': 'O','П': 'P','Р': 'R','С': 'S','Т': 'T','У': 'U',
    'Ф': 'F','Х': 'Kh','Ц': 'Ts','Ч': 'Ch','Ш': 'Sh','Щ': 'Shch','Ь': '',
    "'Ю": 'Yu','Ю': 'Iu',"'Я": 'Ya','Я': 'Ia','’': ''}
    for key in dict:
        name = name.replace(key, dict[key])
    return name
transl = translit(st)
print(transl)
f.close()

word = transl

total = []
var = 0

chars = {'A': 1,'B': 2, 'C': 3, 'D': 4,'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 
'J':10,'K': 11, 'L': 12,'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 
'S': 19, 'T':20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

for w in word:
    print(w)
    for ch in chars:
        print(ch)
        if w.upper() == ch:
            var+=chars[ch]
            total.append(var)
        elif w == ' ':
            total.append(0)
            break

            
print('Sum of word:',total)

    