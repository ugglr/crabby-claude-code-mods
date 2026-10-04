# Writes README.md from mods.json: a gallery of the mods with a picture, then every mod by category.
import json
from html import escape

mods = sorted(json.load(open('mods.json')), key=lambda m: m['name'].lower())
pictured = [m for m in mods if m.get('mediaUrl')]
owner = lambda m: m['url'].split('/')[3]
order = ['pets and fun', 'usage and limits', 'context and sessions', 'agents and tasks',
         'reading and viewing', 'themes and looks', 'sound and alerts', 'productivity']
assert {m['category'] for m in mods} <= set(order), 'unknown category in mods.json'

out = [
    '<img src="assets/crab.png" alt="" width="120" align="right">',
    '',
    '# Crabby Claude Code mods',
    '',
    f'{len(mods)} Claude Code mods, each one checked to be a mod, with a picture where the author published one. '
    'For an index of every mod on GitHub, see the catalogue under [Related](#related).',
    '',
    'Mods are plugins that run code inside Claude Code: they draw panes, bands and status lines, and hook into prompts and tool calls. '
    'They need Claude Code 2.1.287 or later. Mods are not sandboxed, so read the source before you install one.',
    '',
    '## Gallery',
    '',
    '<table>',
]
for i in range(0, len(pictured), 3):
    out.append('<tr>')
    for m in pictured[i:i + 3]:
        url, name = escape(m['url']), escape(m['name'])
        out.append(f'<td width="33%" valign="top"><a href="{url}"><img src="{escape(m["mediaUrl"])}" alt="{name}" width="260"></a><br>'
                   f'<a href="{url}"><b>{name}</b></a> by {escape(owner(m))}<br>{escape(m["description"])}</td>')
    out.append('</tr>')
out += ['</table>', '', '## All mods', '']
out += [f'- [{c.capitalize()}](#{c.replace(" ", "-")})' for c in order]
for c in order:
    group = [m for m in mods if m['category'] == c]
    out += ['', f'## {c.capitalize()}', '']
    out += [f'- [{m["name"]}]({m["url"]}) by {owner(m)} - {m["description"]}' for m in group]
out += [
    '',
    '## Add a mod',
    '',
    'Add an entry to `mods.json`, run `python3 build.py` and open a pull request. '
    'A mod qualifies when its repository is public, its `hooks/hooks.json` lists `modules`, and its README says how to install it. '
    'Describe what it does in one plain sentence, and pick a category: ' + ', '.join(order) + '.',
    '',
    '## Related',
    '',
    '- [Mods documentation](https://code.claude.com/docs/en/plugins/mods/overview)',
    '- [karanb192/awesome-claude-code-mods](https://github.com/karanb192/awesome-claude-code-mods): a scanned catalogue showing what each mod can read, write, run or send',
    '- [lycfyi/awesome-claude-code-mods](https://github.com/lycfyi/awesome-claude-code-mods): a short list, each entry validated',
    '',
    'List content: [CC0](license). Each mod belongs to its author under its own license.',
    '',
]
open('README.md', 'w').write('\n'.join(out))
print(len(mods), 'mods,', len(pictured), 'pictured')
