import os

print("processing")
fout = os.getcwd() + "/tr.txt"
print(fout)

new_lines = []
words_to_exclude = ['the', 'a']
fn = os.getcwd() +  "/RI/lemmatized.text"

t_i = 0
a = 0
with open(fn, 'r') as fd:
    lines = fd.readlines()
    a = len(lines)

    for line in lines:
        ls = line

        for c in words_to_exclude:
            ls = ls.replace(' ' + c + ' ', ' ')
            ls = ls.replace(' ' + c + ' ', ' ') 
            ls = ls.replace(' ' + c + ' ', ' ') 

        new_lines.append(ls.replace('\n', ''))     
        t_i += 1

print(t_i, a, t_i == a, len(new_lines))

def w():
    with open(fout, 'a') as fd:
        for i in range(0, len(new_lines)-1):
            fd.write(new_lines[i] + "\n")
        fd.write(new_lines[len(new_lines)-1])
w()