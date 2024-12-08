import os
from datetime import datetime
from bs4 import BeautifulSoup as bs

# Set up autokattis
try:
    from ak import diff_mapper, nus_problems
except:
    diff_mapper = nus_problems = None

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
open_readme_contents = []
nus_readme_contents = []
open_html_contents = []
nus_html_contents = []
paths = set(); duplicate_paths = set()

# Go through local files
for main_dir in ['src', 'Secret']:
    for path, dirs, files in os.walk(main_dir):
        if os.path.join('Secret', '.git') in path:
            continue

        ori_path, path = path, path.split(os.sep)

        # Black magic!
        if main_dir == 'src':
            if len(path) == 2 and path[1] != '.nus':    path, nus = path[1], False
            elif len(path) == 3 and path[1] == '.nus':  path, nus = path[2], True
            else: continue
        else:
            if not files or path[-1] in ['TLE', 'WA', 'RTE', 'MLE', 'OLE', 'CE', 'Secret']: continue
            elif len(path) == 5 and path[3] == '.nus':  path, nus = path[4], True
            elif len(path) == 4 and path[2] == '.nus':  path, nus = path[3], True
            elif len(path) == 4 and path[3] != '.nus':  path, nus = path[3], False
            elif len(path) == 3 and path[2] != '.nus':  path, nus = path[2], False
            else: continue

        readme_image_links = set()
        html_image_links = set()
        has_py = has_cpp = has_sh = False; has_java = []
        for file in sorted(files):
            ext = file.split('.')[-1]
            if ext in image_mapper and file not in file_whitelist:
                if main_dir == 'src':
                    readme_image_links.add(f"[![{ext}]({get_image(ext)})]({ori_path}/{file})")
                    html_image_links.add((ext, f'https://raw.githubusercontent.com/RussellDash332/kattis/main/{ori_path}/{file}'))
                else:
                    readme_image_links.add(f"[![{ext}]({get_image(ext)})]()")
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
        readme_image_links = sorted(readme_image_links)
        html_image_links = sorted(html_image_links)

        # Handle special cases
        if path in pid_force_mapper:
            has_py = has_cpp = has_java = has_sh = pid_force_mapper[path]

        # Another split to handle variants like /autori
        pid = (has_py or has_cpp or has_java or has_sh).split('.')[0].split('-')[0]

        if nus:
            url = f"https://nus.kattis.com/problems/{pid}"
            nus_readme_contents.append([pid, f"|[{path}]({url})| {pid} |{''.join(readme_image_links).replace(' ','%20')}|\n"])
            nus_html_contents.append([pid, url, path, html_image_links])
            if nus_problems != None:
                nus_problems.remove(pid)
        else:
            url = f"https://open.kattis.com/problems/{pid}"
            if diff_mapper != None:
                open_readme_contents.append([pid, f"|[{path}]({url})| {pid} |{diff_mapper[pid]}|{''.join(readme_image_links).replace(' ','%20')}|\n"])
                open_html_contents.append([pid, url, path, diff_mapper[pid], html_image_links])
                diff_mapper.pop(pid)
            else:
                open_readme_contents.append([pid, f"|[{path}]({url})| {pid} |{''.join(readme_image_links).replace(' ','%20')}|\n"])
                open_html_contents.append([pid, url, path, html_image_links])
        if path in paths: duplicate_paths.add(path)
        paths.add(path)

# Sanity check before writing
assert not duplicate_paths, duplicate_paths
assert not diff_mapper, diff_mapper
assert not nus_problems, nus_problems
print('Mapper exists:', diff_mapper != None)
today = datetime.today().strftime('%d %B %Y')

# Sort them all
open_readme_contents.sort()
open_html_contents.sort()
nus_readme_contents.sort()
nus_html_contents.sort()

# For HTML
with open('docs/index.html') as html:
    soup = bs(html, 'html.parser')
    open_table = soup.find('table', {'id': 'open-kattis-table'})
    nus_table = soup.find('table', {'id': 'nus-kattis-table'})

    # Last updated
    last_updated = soup.find('p', {'id': 'last-updated'})
    last_updated.string = f'Last updated: {today}'

    # Open Kattis
    open_table.clear()
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
    for row  in open_html_contents:
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

        # third column: difficulty
        if diff_mapper != None:
            td = soup.new_tag('td')
            td.string = str(diff)
            tr.append(td)

        # fourth column: languages
        td = soup.new_tag('td')
        for ext, link in image_links:
            img = soup.new_tag('img', src=get_image(ext), alt=ext)
            a = soup.new_tag('a', href=link)
            a.append(img)
            td.append(a)
        tr.append(td)

        tbody.append(tr)
    open_table.append(thead)
    open_table.append(tbody)

    # NUS Kattis
    nus_table.clear()
    thead = soup.new_tag('thead')
    tr = soup.new_tag('tr')
    columns = ['Problem Name', 'Problem ID', 'Languages']
    for column in columns:
        th = soup.new_tag('th')
        th.string = column
        tr.append(th)
    thead.append(tr)
    tbody = soup.new_tag('tbody')
    for pid, url, path, image_links in nus_html_contents:
        tr = soup.new_tag('tr')

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

        # third column: languages
        td = soup.new_tag('td')
        for ext, link in image_links:
            img = soup.new_tag('img', src=get_image(ext), alt=ext)
            a = soup.new_tag('a', href=link)
            a.append(img)
            td.append(a)
        tr.append(td)

        tbody.append(tr)
    nus_table.append(thead)
    nus_table.append(tbody)
with open('docs/index.html', 'w+', encoding='utf-8') as new_html:
    new_html.write(str(soup.prettify()))
print('HTML build done!')

# For README
with open('README.md', 'r') as readme:
    lines = readme.readlines()[:3]
with open('README.md', 'w+') as new_readme:
    for line in lines:
        new_readme.write(line)
    new_readme.write(f'## Total problems solved: {len(open_readme_contents)}\n\n')
    new_readme.write('\n\n'.join([
        'Note that the tables below are auto-generated using [autokattis](https://github.com/RussellDash332/autokattis).',
        'You might find [this link](https://stackoverflow.com/questions/42843288/is-there-any-way-to-make-markdown-tables-sortable) useful to interact with the table.',
        'For more Python data structure implementations, head over to [pytils](https://github.com/RussellDash332/pytils).'
    ])+'\n\n')

    # Open Kattis
    if diff_mapper != None:
        new_readme.write('|Problem Name|Problem ID|Difficulty|Languages|\n|:---|:---|:---|:---|\n')
    else:
        new_readme.write('|Problem Name|Problem ID|Languages|\n|:---|:---|:---|\n')
    for key, content in open_readme_contents:
        new_readme.write(content)

    # NUS Kattis
    new_readme.write('\n\n'.join([
        '\n## NUS-exclusive problems',
        'These problems can only be found in NUS Kattis and therefore do not contribute to the number of problems solved.',
        '|Problem Name|Problem ID|Languages|\n|:---|:---|:---|'
    ])+'\n')
    for key, content in nus_readme_contents:
        new_readme.write(content)
print('README build done!')