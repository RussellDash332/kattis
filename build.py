import os

file_whitelist = {'bnn_accuracy.py', 'testing_tool.py', 'unununion_find.py'}
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
    'rb':   'ruby',
    'js':   'javascript'
}
get_image = lambda e,s=24: f'{image_src}{image_mapper[e]}/{image_mapper[e]}_{s}x{s}.png'

contents = []
for path, dirs, files in os.walk('src'):
    ori_path, path = path, path.split(os.sep)
    if len(path) == 2 and path[1] != '.nus': path, nus = path[1], False
    elif len(path) == 3 and path[1] == '.nus': path, nus = path[2], True
    else: continue
    hyps = []
    has_py = has_cpp = False; has_java = []
    for file in sorted(files):
        ext = file.split('.')[-1]
        if ext in image_mapper and file not in file_whitelist: hyps.append(f"[![{ext}]({get_image(ext)})]({ori_path}/{file})")
        if not has_cpp and ext == 'cpp': has_cpp = file
        if not has_java and ext == 'java': has_java.append(file.lower())
        if not has_py and file not in file_whitelist and ext == 'py': has_py = file

    has_java = min(has_java) if has_java else []
    if path == '99 Problems (2)': has_py = has_cpp = has_java = '99problems2'

    pid = (has_py or has_cpp or has_java).split('.')[0].split('-')[0] # another split to handle /autori
    url = f"https://open.kattis.com/problems/{pid}"

    if nus:
        url = url.replace('open.kattis.com', 'nus.kattis.com').replace('problems/', 'problems/nus.')
        contents.append([f'!nus.{pid}', f"|[[NUS] {path}]({url})| nus.{pid} |{''.join(hyps).replace(' ','%20')}|\n"]) # NUS-exclusive problems first
    else:
        contents.append([pid, f"|[{path}]({url})| {pid} |{''.join(hyps).replace(' ','%20')}|\n"])

HIDDEN = 19 + 10
lines = open('README.md', 'r').readlines()[:3]
with open('README.md', 'w+') as f:
    for line in lines: f.write(line)
    f.write(f'## Total problems solved: {len(contents) + HIDDEN}\n\n')
    f.write(f'Note that the table below is auto-generated. There might be slight inaccuracies.\n\n')
    f.write('|Problem Name|Problem ID|Languages|\n|:---|:---|:---|\n')
    for key, content in sorted(contents): f.write(content)