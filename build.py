import os, requests

use_requests = False

file_whitelist = {'bnn_accuracy.py'}

image_src = 'https://github.com/abrahamcalf/programming-languages-logos/blob/master/src/' # hey this a credit!
image_mapper = {
    'py':   'python',
    'c':    'c',
    'cpp':  'cpp',
    'cs':   'csharp',
    'go':   'go',
    'hs':   'haskell',
    'java': 'java',
    'kt':   'kotlin',
    'php':  'php',
    'rb':   'ruby'
}
get_image = lambda e,s=24: f'{image_src}{image_mapper[e]}/{image_mapper[e]}_{s}x{s}.png'

contents = []
for path, dirs, files in os.walk('src'):
    ori_path, path = path, path.split(os.sep)
    if len(path) == 2 and path[1] != '.nus': path, nus = path[1], False
    elif len(path) == 3 and path[1] == '.nus': path, nus = path[2], True
    else: continue
    hyps = []
    has_py = has_cpp = False
    for file in sorted(files):
        ext = file.split('.')[-1]
        if ext in image_mapper: hyps.append(f"[![{ext}]({get_image(ext)})]({ori_path}/{file})")
        if not has_cpp and ext == 'cpp': has_cpp = file
        if not has_py and file not in file_whitelist and ext == 'py': has_py = file
    if has_py or has_cpp: url = f"https://open.kattis.com/problems/{(has_py or has_cpp).split('.')[0]}"
    else: url = f"https://open.kattis.com/search?q={path.replace(' ','%20')}"
    
    if nus:
        url = url.replace('open.kattis.com', 'nus.kattis.com').replace('problems/', 'problems/nus.')
        contents.append(f"|[[NUS] {path}]({url})|{''.join(hyps).replace(' ','%20')}|\n")
    else:
        contents.append(f"|[{path}]({url})|{''.join(hyps).replace(' ','%20')}|\n")

lines = open('README.md', 'r').readlines()[:6] + ['\n']
with open('README.md', 'w+') as f:
    for line in lines: f.write(line)
    f.write('|Problem Name|Languages|\n|:---|:---|\n')
    for content in sorted(contents): f.write(content)