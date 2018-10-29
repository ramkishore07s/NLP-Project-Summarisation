import sys
import pickle

input_filepath = sys.argv[1]

file = input_filepath.split('/')
fname = file[-1]

ftype = fname.split('.')

if len(ftype) == 3 and ftype[0] == 'doc':
    outfile = 'output'+'.'+ftype[1]+'.'+ftype[2]
    outfilepath = '../../Dataset/Cheng_outputs/' + file[-2]+'/' + outfile
    
annotations = {}

f = open(outfilepath,'r')
data = f.read()
f.close()

data = data.split('\n')

count = 0

# print(data)

for line in data[:-1]:
    annotations[count] = int(line)
    # print(count)
    count += 1

with open('summary.pkl', 'rb') as f:
    selected = pickle.load(f)

# print(len(annotations))

acc = 0

for i in selected:
    if annotations[i]:
        acc += 1
    
print(acc/3)