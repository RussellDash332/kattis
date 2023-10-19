import os

try: from ak import diff_mapper
except: diff_mapper = None

file_whitelist = {'bnn_accuracy.py', 'testing_tool.py', 'unununion_find.py', 'comp.py'}
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
for main_dir in ['src', 'Secret']:
    for path, dirs, files in os.walk(main_dir):
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

        url = f"https://open.kattis.com/problems/{pid}"
        if nus:
            url = url.replace('open.kattis.com', 'nus.kattis.com').replace('problems/', 'problems/nus.')
            # NUS-exclusive problems first
            if diff_mapper: contents.append([f'!nus.{pid}', f"|[[NUS] {path}]({url})| nus.{pid} |N/A|{''.join(hyps).replace(' ','%20')}|\n"])
            else:           contents.append([f'!nus.{pid}', f"|[[NUS] {path}]({url})| nus.{pid} |{''.join(hyps).replace(' ','%20')}|\n"]) 
        else:
            if diff_mapper: contents.append([pid, f"|[{path}]({url})| {pid} |{diff_mapper[pid]}|{''.join(hyps).replace(' ','%20')}|\n"])
            else:           contents.append([pid, f"|[{path}]({url})| {pid} |{''.join(hyps).replace(' ','%20')}|\n"])

lines = open('README.md', 'r').readlines()[:3]
with open('README.md', 'w+') as f:
    for line in lines: f.write(line)
    f.write(f'## Total problems solved: {len(contents)}\n\n')
    f.write('\n\n'.join([
        'Note that the table below is auto-generated using [autokattis](https://github.com/RussellDash332/autokattis).',
        'You might find [this link](https://stackoverflow.com/questions/42843288/is-there-any-way-to-make-markdown-tables-sortable) useful to interact with the table.',
        'For more Python data structure implementations, head over to [pytils](https://github.com/RussellDash332/pytils).'
    ])+'\n\n')
    if diff_mapper: f.write('|Problem Name|Problem ID|Difficulty|Languages|\n|:---|:---|:---|:---|\n')
    else:           f.write('|Problem Name|Problem ID|Languages|\n|:---|:---|:---|\n')
    for key, content in sorted(contents): f.write(content)