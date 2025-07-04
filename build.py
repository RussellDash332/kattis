import os
from datetime import datetime
from bs4 import BeautifulSoup as bs

# Set up autokattis (hidden file)
try:
    from ak import diff_mapper, iceland_diff_mapper, nus_problems
except:
    diff_mapper = iceland_diff_mapper = nus_problems = None

# Files that do not contribute to the problem ID extraction
file_whitelist = {'bnn_accuracy.py', 'testing_tool.py', 'unununion_find.py', 'comp.py'}

# Force-map problem name to problem ID due to filename issues
pid_force_mapper = {
    '99 Problems (2)': '99problems2',
    '10 Kinds of People': '10kindsofpeople'
}

# Image credits to https://languages.abranhe.com/
image_mapper = {
    'py':   'python',
    'sh':   'bash',
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

# Set up contents
open_html_contents = []
nus_html_contents = []
iceland_html_contents = []
paths = set(); duplicate_paths = set()

# Go through local files
for main_dir in ['src', 'Secret']:
    for path, dirs, files in os.walk(main_dir):
        if os.path.join('Secret', '.git') in path:
            continue

        ori_path, path = path, path.split(os.sep)

        # Black magic!
        if main_dir == 'src':
            if len(path) == 2 and path[1][0] != '.':    path, domain = path[1], 'open'
            elif len(path) == 3 and path[1][0] == '.':  path, domain = path[2], path[1][1:] # .nus, .iceland
            else: continue
        else:
            if not files or path[-1] in ['TLE', 'WA', 'RTE', 'MLE', 'OLE', 'CE', 'Secret']: continue
            elif len(path) == 5 and path[3][0] == '.':  path, domain = path[4], path[3][1:]
            elif len(path) == 4 and path[2][0] == '.':  path, domain = path[3], path[2][1:]
            elif len(path) == 4 and path[3][0] != '.':  path, domain = path[3], 'open'
            elif len(path) == 3 and path[2][0] != '.':  path, domain = path[2], 'open'
            else: continue

        html_image_links = set()
        has_py = has_cpp = has_sh = False; has_java = []
        for file in sorted(files):
            ext = file.split('.')[-1]
            if ext in image_mapper and file not in file_whitelist:
                if main_dir == 'src':
                    html_image_links.add((ext, f'https://raw.githubusercontent.com/RussellDash332/kattis/main/{ori_path}/{file}'))
                else:
                    html_image_links.add((ext, '#'))
            if not has_cpp and ext == 'cpp':
                has_cpp = file
            if not has_java and ext == 'java':
                has_java.append(file.lower())
            if not has_sh and ext == 'sh':
                has_sh = file
            if not has_py and file not in file_whitelist and ext == 'py':
                has_py = file
        has_java = min(has_java) if has_java else []
        html_image_links = sorted(html_image_links)

        # Handle special cases
        if path in pid_force_mapper:
            has_py = has_cpp = has_java = has_sh = pid_force_mapper[path] + '.dummy'

        # Another split to handle variants
        # e.g. autori-regex.py -> autori, iceland.test.py -> iceland.test
        pid = '.'.join((has_py or has_cpp or has_java or has_sh).split('.')[:-1]).split('-')[0]

        if domain == 'nus':
            url = f"https://nus.kattis.com/problems/{pid}"
            nus_html_contents.append([pid, url, path, html_image_links])
            if nus_problems != None:
                nus_problems.remove(pid)
        elif domain == 'iceland':
            url = f"https://iceland.kattis.com/problems/{pid}"
            if iceland_diff_mapper != None:
                iceland_html_contents.append([pid, url, path, iceland_diff_mapper[pid], html_image_links])
                iceland_diff_mapper.pop(pid)
            else:
                iceland_html_contents.append([pid, url, path, html_image_links])
        else:
            url = f"https://open.kattis.com/problems/{pid}"
            if diff_mapper != None:
                open_html_contents.append([pid, url, path, diff_mapper[pid], html_image_links])
                diff_mapper.pop(pid)
            else:
                open_html_contents.append([pid, url, path, html_image_links])
        if path in paths: duplicate_paths.add(path)
        paths.add(path)

# Sanity check before writing
assert not duplicate_paths, duplicate_paths
assert not iceland_diff_mapper, iceland_diff_mapper
assert not diff_mapper, diff_mapper
assert not nus_problems, nus_problems
print('Mapper exists:', f'(open: {diff_mapper != None}, iceland: {iceland_diff_mapper != None})')
today = datetime.today().strftime('%d %B %Y')

# Sort them all
open_html_contents.sort()
nus_html_contents.sort()
iceland_html_contents.sort()

def build_table(table, html_contents, diff_mapper):
    table.clear()
    thead = soup.new_tag('thead')
    tr = soup.new_tag('tr')

    columns = ['Problem Name', 'Problem ID', 'Difficulty', 'Languages']
    if diff_mapper == None:
        columns.remove('Difficulty')

    for column in columns:
        th = soup.new_tag('th')
        th.string = column
        tr.append(th)
    thead.append(tr)
    tbody = soup.new_tag('tbody')

    for row in html_contents:
        tr = soup.new_tag('tr')
        if diff_mapper == None:
            pid, url, path, image_links = row
        else:
            pid, url, path, diff, image_links = row

        # first column: problem name
        td = soup.new_tag('td')
        a = soup.new_tag('a', href=url)
        a.string = path
        td.append(a)
        tr.append(td)

        # second column: problem ID
        td = soup.new_tag('td')
        td.string = pid
        tr.append(td)

        # third column: difficulty?
        if diff_mapper != None:
            td = soup.new_tag('td')
            def get_square(diff):
                try:
                    diff = float(diff)
                    if diff < 2.8: return '🟩'
                    if diff < 5.5: return '🟨'
                    return '🟥'
                except:
                    return '⬛'
            td.string = str(diff) + ' ' + get_square(diff)
            tr.append(td)

        # fourth (or third?) column: languages
        td = soup.new_tag('td')
        for ext, link in image_links:
            img = soup.new_tag('img', src=get_image(ext), alt=ext)
            a = soup.new_tag('a', href=link)
            a.append(img)
            td.append(a)
        tr.append(td)

        tbody.append(tr)

    table.append(thead)
    table.append(tbody)

# For HTML
with open('docs/index.html') as html:
    soup = bs(html, 'html.parser')
    open_table = soup.find('table', {'id': 'open-kattis-table'})
    nus_table = soup.find('table', {'id': 'nus-kattis-table'})
    iceland_table = soup.find('table', {'id': 'iceland-kattis-table'})

    # Last updated
    last_updated = soup.find('p', {'id': 'last-updated'})
    last_updated.string = f'Last updated: {today}'

    # Open Kattis
    build_table(open_table, open_html_contents, diff_mapper)

    # NUS Kattis
    build_table(nus_table, nus_html_contents, None)

    # Iceland Kattis
    build_table(iceland_table, iceland_html_contents, iceland_diff_mapper)

with open('docs/index.html', 'w+', encoding='utf-8') as new_html:
    new_html.write(str(soup.prettify()))
print('HTML build done!')

# For README
# Tables moved to HTML since the contents are now too big :)
with open('README.md', 'r') as readme:
    lines = readme.readlines()[:3]
with open('README.md', 'w+') as new_readme:
    for line in lines:
        new_readme.write(line)
    new_readme.write(f'## Total problems solved: {len(open_html_contents)}\n\n')
    new_readme.write('\n\n'.join([
        '**For the full table of solved problems, refer to [this page](https://russelldash332.github.io/kattis) instead.**',
        'Note that the tables there are auto-generated using [autokattis](https://github.com/RussellDash332/autokattis).',
        '[![autokattis](https://github-readme-stats.vercel.app/api/pin/?theme=react&username=RussellDash332&repo=autokattis)](https://github.com/RussellDash332/autokattis)',
        'For more Python data structure implementations, head over to [pytils](https://github.com/RussellDash332/pytils).',
        '[![pytils](https://github-readme-stats.vercel.app/api/pin/?theme=react&username=RussellDash332&repo=pytils)](https://github.com/RussellDash332/pytils)'
    ])+'\n\n')
    new_readme.write(f'Last updated {today}, **plagiarize at your own risk**.')
print('README build done!')