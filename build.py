import os

try: from ak import diff_mapper, nus_problems
except: diff_mapper = nus_problems = None

file_whitelist = {'bnn_accuracy.py', 'testing_tool.py', 'unununion_find.py', 'comp.py'}

# Image credits to https://languages.abranhe.com/
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
get_image = lambda e: f'images/{image_mapper[e]}.png'

contents = []
nus_contents = []
for main_dir in ['src', 'Secret']:
    for path, dirs, files in os.walk(main_dir):
        if os.path.join('Secret', '.git') in path: continue

        ori_path, path = path, path.split(os.sep)

        if main_dir == 'src':
            if len(path) == 2 and path[1] != '.nus': path, nus = path[1], False
            elif len(path) == 3 and path[1] == '.nus': path, nus = path[2], True
            else: continue
        else:
            if not files or path[-1] in ['TLE', 'WA', 'RTE', 'MLE', 'OLE', 'CE', 'Secret']: continue
            elif len(path) == 5 and path[3] == '.nus': path, nus = path[4], True
            elif len(path) == 4 and path[2] == '.nus': path, nus = path[3], True
            elif len(path) == 4 and path[3] != '.nus': path, nus = path[3], False
            elif len(path) == 3 and path[2] != '.nus': path, nus = path[2], False
            else: continue

        hyps = []
        has_py = has_cpp = False; has_java = []
        for file in sorted(files):
            ext = file.split('.')[-1]
            if ext in image_mapper and file not in file_whitelist:
                if main_dir == 'src': hyps.append(f"[![{ext}]({get_image(ext)})]({ori_path}/{file})")
                else: hyps.append(f"[![{ext}]({get_image(ext)})]()")
            if not has_cpp and ext == 'cpp': has_cpp = file
            if not has_java and ext == 'java': has_java.append(file.lower())
            if not has_py and file not in file_whitelist and ext == 'py': has_py = file
        has_java = min(has_java) if has_java else []

        # special cases
        if path == '99 Problems (2)': has_py = has_cpp = has_java = '99problems2'
        elif path == '10 Kinds of People': has_py = has_cpp = has_java = '10kindsofpeople'

        pid = (has_py or has_cpp or has_java).split('.')[0].split('-')[0] # another split to handle /autori
        
        if nus:
            url = f"https://nus.kattis.com/problems/{pid}"
            nus_contents.append([pid, f"|[{path}]({url})| {pid} |{''.join(hyps).replace(' ','%20')}|\n"])
            if nus_problems != None: nus_problems.remove(pid)
        else:
            url = f"https://open.kattis.com/problems/{pid}"
            if diff_mapper: contents.append([pid, f"|[{path}]({url})| {pid} |{diff_mapper[pid]}|{''.join(hyps).replace(' ','%20')}|\n"]); diff_mapper.pop(pid)
            else:           contents.append([pid, f"|[{path}]({url})| {pid} |{''.join(hyps).replace(' ','%20')}|\n"])

lines = open('README.md', 'r').readlines()[:3]
assert not diff_mapper, diff_mapper
assert not nus_problems, nus_problems
with open('README.md', 'w+') as f:
    for line in lines: f.write(line)
    f.write(f'## Total problems solved: {len(contents)}\n\n')
    f.write('\n\n'.join([
        'Note that the table below is auto-generated using [autokattis](https://github.com/RussellDash332/autokattis).',
        'You might find [this link](https://stackoverflow.com/questions/42843288/is-there-any-way-to-make-markdown-tables-sortable) useful to interact with the table.',
        'For more Python data structure implementations, head over to [pytils](https://github.com/RussellDash332/pytils).'
    ])+'\n\n')
    if diff_mapper != None: f.write('|Problem Name|Problem ID|Difficulty|Languages|\n|:---|:---|:---|:---|\n')
    else:                   f.write('|Problem Name|Problem ID|Languages|\n|:---|:---|:---|\n')
    for key, content in sorted(contents): f.write(content)

    f.write('\n\n'.join([
        '\n## NUS-exclusive problems',
        'These problems can only be found in NUS Kattis and therefore do not contribute to the number of problems solved.',
        '|Problem Name|Problem ID|Languages|\n|:---|:---|:---|'
    ])+'\n')
    for key, content in sorted(nus_contents): f.write(content)
print('Build done! Mapper exists:', diff_mapper != None)