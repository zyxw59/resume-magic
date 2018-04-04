#!/usr/bin/env python3
import sys
import json
import latexcodec

l_preamble = r"""\documentclass[11pt]{article}
\usepackage{resume}
\usepackage[rm]{roboto}
"""

l_titling = r"""\def\name{{{name}}}
\def\phone{{{phone}}}
\def\email{{{email}}}
\def\github{{{github}}}
\def\termstreet{{{termstreet}}}
\def\termcity{{{termcity}}}
\def\homestreet{{{homestreet}}}
\def\homecity{{{homecity}}}

\begin{{document}}
\maketitle

"""

l_section = "\\section{{{section}}}\n"

l_position = r"""\def\employer{{{employer}}}
\def\location{{{location}}}
\def\title{{{title}}}
\def\dates{{{dates}}}
"""

l_description = r"""\begin{{position}}
{}
\end{{position}}

"""

l_nodescription = r"""\positionnolist{}

"""

l_itemize = r"\item {}"

l_skills = r"""\section{{skills}}
\begin{{itemize}}
{}
\end{{itemize}}
"""

l_end = r"\end{document}"

h_preamble = ""

h_titling = """\
<h2>{name}</h2>
<table class="address">
<tr><th class="termaddr">Term Address</th>
<td class="phone">{phone}</td>
<th class="homeaddr">Permanent Address</th></tr>
<tr><td class="termaddr">{termstreet}</td>
<td class="email"><a href="mailto:{email}">{email}</a></td>
<td class="homeaddr">{homestreet}</td></tr>
<tr><td class="termaddr">{termcity}</td>
<td class="github"><a href="{github}">{github}</a></td>
<td class="homeaddr">{homecity}</td></tr>
</table>

"""

h_section = "<h3>{section}</h3>"

h_position = """\
<table class="position">
<tr><td class="employer">{employer}</td><td class="location">{location}</td></tr>
<tr><td class="title">{title}</td><td class="dates">{dates}</td></tr>
</table>
"""

h_description = """\
<ul class="description">
{}
</ul>
"""

h_itemize = "<li>{}</li>"

h_skills = """\
<h3>Skills</h3>
<ul class="skills">
{}
</ul>
"""

h_end = ""


def load(argv):
    if len(argv) == 2:
        name = argv[1]
    else:
        raise TypeError('{} takes 1 argument but {} were '
                        'given'.format(argv[0], len(argv) - 1))
    if '.' not in name:
        inf = open(name + '.json')
    else:
        inf = open(name)
        name = name.rsplit('.', 1)[0]
    html_out = open(name + '.html', 'w', encoding='ascii', errors='xmlcharrefreplace')
    latex_out = open(name + '.tex', 'w', encoding='latex')
    return inf, html_out, latex_out


def main(argv):
    try:
        inf, html_out, latex_out = load(argv)
        d = json.load(inf)
        latex_out.write(l_preamble)
        html_out.write(h_preamble)
        latex_out.write(l_titling.format(**d))
        html_out.write(h_titling.format(**d))
        for sec in d['sections']:
            latex_out.write(l_section.format(section=sec['title']))
            html_out.write(h_section.format(section=sec['title']))
            for index in sec['positions']:
                pos = [p for p in d['positions'] if p['id'] == index][0]
                latex_out.write(l_position.format(**pos))
                html_out.write(h_position.format(**pos))
                if pos['description']:
                    l_items = (l_itemize.format(i) for i in pos['description'])
                    h_items = (h_itemize.format(i) for i in pos['description'])
                    latex_out.write(l_description.format('\n'.join(l_items)))
                    html_out.write(h_description.format('\n'.join(h_items)))
                else:
                    latex_out.write(l_nodescription)
                    html_out.write(h_description.format(''))
        l_items, h_items = zip(*((l_itemize.format(i), h_itemize.format(i))
                                 for i in d['skills']))
        latex_out.write(l_skills.format('\n'.join(l_items)))
        html_out.write(h_skills.format('\n'.join(h_items)))
        latex_out.write(l_end)
        html_out.write(h_end)
    finally:
        inf.close()
        html_out.close()
        latex_out.close()

if __name__ == '__main__':
    main(sys.argv)
