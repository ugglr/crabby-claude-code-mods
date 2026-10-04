<img src="assets/crab.png" alt="" width="120" align="right">

# Crabby Claude Code mods

225 Claude Code mods, each one checked to be a mod, with a picture where the author published one. For an index of every mod on GitHub, see the catalogue under [Related](#related).

Mods are plugins that run code inside Claude Code: they draw panes, bands and status lines, and hook into prompts and tool calls. They need Claude Code 2.1.287 or later. Mods are not sandboxed, so read the source before you install one.

## Gallery

<table>
<tr>
<td width="33%" valign="top"><a href="https://github.com/arasovic/claude-code-mods/tree/main/cache-timer"><img src="https://raw.githubusercontent.com/arasovic/claude-code-mods/main/docs/cache-timer.png" alt="cache-timer" width="260"></a><br><a href="https://github.com/arasovic/claude-code-mods/tree/main/cache-timer"><b>cache-timer</b></a> by arasovic<br>Counts down to when the prompt cache expires so you can send before it goes cold.</td>
<td width="33%" valign="top"><a href="https://github.com/sezaakgun/cc-arcade"><img src="https://raw.githubusercontent.com/sezaakgun/cc-arcade/main/docs/demo.gif" alt="cc-arcade" width="260"></a><br><a href="https://github.com/sezaakgun/cc-arcade"><b>cc-arcade</b></a> by sezaakgun<br>A set of terminal games above the prompt plus a pet that grows as Claude tests and commits.</td>
<td width="33%" valign="top"><a href="https://github.com/arasovic/claude-code-mods/tree/main/change-ledger"><img src="https://raw.githubusercontent.com/arasovic/claude-code-mods/main/docs/change-ledger.png" alt="change-ledger" width="260"></a><br><a href="https://github.com/arasovic/claude-code-mods/tree/main/change-ledger"><b>change-ledger</b></a> by arasovic<br>Lists files edited this session in a pane with line counts and who edited them.</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://github.com/arasovic/claude-code-mods/tree/main/ci-watch"><img src="https://raw.githubusercontent.com/arasovic/claude-code-mods/main/docs/ci-watch.png" alt="ci-watch" width="260"></a><br><a href="https://github.com/arasovic/claude-code-mods/tree/main/ci-watch"><b>ci-watch</b></a> by arasovic<br>Watches GitHub Actions in a band above the prompt after a push, PR or tag, with progress bars.</td>
<td width="33%" valign="top"><a href="https://github.com/Anerco/claude-code-effort-cycle"><img src="https://raw.githubusercontent.com/Anerco/claude-code-effort-cycle/main/demo.gif" alt="claude-code-effort-cycle" width="260"></a><br><a href="https://github.com/Anerco/claude-code-effort-cycle"><b>claude-code-effort-cycle</b></a> by Anerco<br>Cycles reasoning effort levels with Alt+E and Alt+Shift+E, leaving nothing in the transcript.</td>
<td width="33%" valign="top"><a href="https://github.com/hex/claude-council"><img src="https://raw.githubusercontent.com/hex/claude-council/main/docs/images/council-pane.png" alt="claude-council" width="260"></a><br><a href="https://github.com/hex/claude-council"><b>claude-council</b></a> by hex<br>Consults several AI coding agents in parallel and shows their answers side by side.</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://github.com/scasella/claude-flightdeck"><img src="https://raw.githubusercontent.com/scasella/claude-flightdeck/main/docs/media/demo.gif" alt="claude-flightdeck" width="260"></a><br><a href="https://github.com/scasella/claude-flightdeck"><b>claude-flightdeck</b></a> by scasella<br>A terminal dashboard of context, cost, advisor timeline, permission checks and subagents as cards or swimlanes.</td>
<td width="33%" valign="top"><a href="https://github.com/0NE-C0DEMAN/deskbar"><img src="https://raw.githubusercontent.com/0NE-C0DEMAN/deskbar/main/media/deskbar-launch-v1.gif" alt="deskbar" width="260"></a><br><a href="https://github.com/0NE-C0DEMAN/deskbar"><b>deskbar</b></a> by 0NE-C0DEMAN<br>A row of widgets above the prompt for context weather, Gmail, calendar and more, each opening a dropdown.</td>
<td width="33%" valign="top"><a href="https://github.com/helenkwok/gsd-status-mod"><img src="https://raw.githubusercontent.com/helenkwok/gsd-status-mod/main/docs/screenshots/demo.gif" alt="gsd-status-mod" width="260"></a><br><a href="https://github.com/helenkwok/gsd-status-mod"><b>gsd-status-mod</b></a> by helenkwok<br>A live dashboard for GSD projects showing the roadmap, current phase and an agent tree with live clocks.</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://github.com/arasovic/claude-code-mods/tree/main/image-peek"><img src="https://raw.githubusercontent.com/arasovic/claude-code-mods/main/docs/image-peek-draft.png" alt="image-peek" width="260"></a><br><a href="https://github.com/arasovic/claude-code-mods/tree/main/image-peek"><b>image-peek</b></a> by arasovic<br>Shows pasted images as thumbnails above the prompt and larger under each sent message in kitty-graphics terminals.</td>
<td width="33%" valign="top"><a href="https://github.com/theonly1me/claude-code-mods/tree/main/plugins/little-harvest"><img src="https://raw.githubusercontent.com/theonly1me/claude-code-mods/main/plugins/little-harvest/assets/preview.png" alt="little-harvest" width="260"></a><br><a href="https://github.com/theonly1me/claude-code-mods/tree/main/plugins/little-harvest"><b>little-harvest</b></a> by theonly1me<br>A garden that grows a little with each Claude turn.</td>
<td width="33%" valign="top"><a href="https://github.com/arasovic/claude-code-mods/tree/main/loop-guard"><img src="https://raw.githubusercontent.com/arasovic/claude-code-mods/main/docs/loop-guard.png" alt="loop-guard" width="260"></a><br><a href="https://github.com/arasovic/claude-code-mods/tree/main/loop-guard"><b>loop-guard</b></a> by arasovic<br>Tells the model silently to stop when the same call fails twice with the same error.</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://github.com/hamzafer/claude-code-mods/tree/main/mods/mission-control"><img src="https://raw.githubusercontent.com/hamzafer/claude-code-mods/main/images/mission-control.gif" alt="mission-control" width="260"></a><br><a href="https://github.com/hamzafer/claude-code-mods/tree/main/mods/mission-control"><b>mission-control</b></a> by hamzafer<br>Opens a live map of the main agent, subagents and every tool call, plus a code map of touched files.</td>
<td width="33%" valign="top"><a href="https://github.com/theonly1me/claude-code-mods/tree/main/plugins/night-feast"><img src="https://raw.githubusercontent.com/theonly1me/claude-code-mods/main/plugins/night-feast/assets/vampire.png" alt="night-feast" width="260"></a><br><a href="https://github.com/theonly1me/claude-code-mods/tree/main/plugins/night-feast"><b>night-feast</b></a> by theonly1me<br>A vampire hunts villagers on screen while Claude works.</td>
<td width="33%" valign="top"><a href="https://github.com/arasovic/claude-code-mods/tree/main/pin-board"><img src="https://raw.githubusercontent.com/arasovic/claude-code-mods/main/docs/pin-board.png" alt="pin-board" width="260"></a><br><a href="https://github.com/arasovic/claude-code-mods/tree/main/pin-board"><b>pin-board</b></a> by arasovic<br>Pins standing notes with /pin that survive /compact and /clear and show in a row above the prompt.</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://github.com/theonly1me/claude-code-mods/tree/main/plugins/pocket-familiar"><img src="https://raw.githubusercontent.com/theonly1me/claude-code-mods/main/plugins/pocket-familiar/assets/preview.png" alt="pocket-familiar" width="260"></a><br><a href="https://github.com/theonly1me/claude-code-mods/tree/main/plugins/pocket-familiar"><b>pocket-familiar</b></a> by theonly1me<br>A growing companion creature that lives alongside your work.</td>
<td width="33%" valign="top"><a href="https://github.com/NahumLitvin/prismantis"><img src="https://raw.githubusercontent.com/NahumLitvin/prismantis/main/docs/screenshot.png" alt="prismantis" width="260"></a><br><a href="https://github.com/NahumLitvin/prismantis"><b>prismantis</b></a> by NahumLitvin<br>Renders replies with colored tables, code, diagrams and charts in 15 themes, with copy buttons.</td>
<td width="33%" valign="top"><a href="https://github.com/BayramAnnakov/claude-reflect/tree/main/mod"><img src="https://raw.githubusercontent.com/BayramAnnakov/claude-reflect/main/assets/reflect-mod-band.png" alt="reflect-mod" width="260"></a><br><a href="https://github.com/BayramAnnakov/claude-reflect/tree/main/mod"><b>reflect-mod</b></a> by BayramAnnakov<br>Finds reusable corrections in your prompts and offers to save them to CLAUDE.md from a band.</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://github.com/viticci/remctl/tree/main/plugins/claude-code"><img src="https://cdn.macstories.net/images/uploads/2026/09/30/15-cli-today-1790776847710-fed98e698d.png" alt="remctl" width="260"></a><br><a href="https://github.com/viticci/remctl/tree/main/plugins/claude-code"><b>remctl</b></a> by viticci<br>A Today band for Apple Reminders above the prompt, part of RemCTL.</td>
<td width="33%" valign="top"><a href="https://github.com/theonly1me/claude-code-mods/tree/main/plugins/samurai-dojo"><img src="https://raw.githubusercontent.com/theonly1me/claude-code-mods/main/plugins/samurai-dojo/assets/preview.png" alt="samurai-dojo" width="260"></a><br><a href="https://github.com/theonly1me/claude-code-mods/tree/main/plugins/samurai-dojo"><b>samurai-dojo</b></a> by theonly1me<br>A samurai trains, meditates and fights on screen while Claude works.</td>
<td width="33%" valign="top"><a href="https://github.com/arasovic/claude-code-mods/tree/main/search-meter"><img src="https://raw.githubusercontent.com/arasovic/claude-code-mods/main/docs/search-meter.png" alt="search-meter" width="260"></a><br><a href="https://github.com/arasovic/claude-code-mods/tree/main/search-meter"><b>search-meter</b></a> by arasovic<br>Counts the model&#x27;s searches and colors each by whether it found the answer first try, late or not at all.</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://github.com/arasovic/claude-code-mods/tree/main/secret-guard"><img src="https://raw.githubusercontent.com/arasovic/claude-code-mods/main/docs/secret-guard.png" alt="secret-guard" width="260"></a><br><a href="https://github.com/arasovic/claude-code-mods/tree/main/secret-guard"><b>secret-guard</b></a> by arasovic<br>Hides API keys and private keys before the model or transcript sees them and blocks credential file reads.</td>
<td width="33%" valign="top"><a href="https://github.com/arasovic/claude-code-mods/tree/main/session-meter"><img src="https://raw.githubusercontent.com/arasovic/claude-code-mods/main/docs/session-meter.png" alt="session-meter" width="260"></a><br><a href="https://github.com/arasovic/claude-code-mods/tree/main/session-meter"><b>session-meter</b></a> by arasovic<br>A live session pane with context breakdown, usage limits and pace, tool calls and model requests.</td>
<td width="33%" valign="top"><a href="https://github.com/arasovic/claude-code-mods/tree/main/show-me"><img src="https://raw.githubusercontent.com/arasovic/claude-code-mods/main/docs/show-me.png" alt="show-me" width="260"></a><br><a href="https://github.com/arasovic/claude-code-mods/tree/main/show-me"><b>show-me</b></a> by arasovic<br>Draws the mermaid diagrams of each answer as images in a pane, using mmdc and a kitty-graphics terminal.</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://github.com/DrumAndCode/terminal-gym"><img src="https://raw.githubusercontent.com/DrumAndCode/terminal-gym/main/docs/band.png" alt="terminal-gym" width="260"></a><br><a href="https://github.com/DrumAndCode/terminal-gym"><b>terminal-gym</b></a> by DrumAndCode<br>Log bodyweight sets from a band above the prompt while Claude works, with a daily goal and streak.</td>
<td width="33%" valign="top"><a href="https://github.com/ugglr/claude-token-monster"><img src="https://raw.githubusercontent.com/ugglr/claude-token-monster/main/media/cast.gif" alt="token-monster" width="260"></a><br><a href="https://github.com/ugglr/claude-token-monster"><b>token-monster</b></a> by ugglr<br>A pixel-art monster in a side pane that eats tokens and shows context, limits and activity.</td>
<td width="33%" valign="top"><a href="https://github.com/augiefra/claude-mods/tree/main/plugins/token-weather-usage"><img src="https://raw.githubusercontent.com/augiefra/claude-mods/main/docs/band.png" alt="token-weather-usage" width="260"></a><br><a href="https://github.com/augiefra/claude-mods/tree/main/plugins/token-weather-usage"><b>token-weather-usage</b></a> by augiefra<br>One line above the prompt showing context weather, token bars and 5-hour and 7-day limits with reset time.</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://github.com/arasovic/claude-code-mods/tree/main/turn-footer"><img src="https://raw.githubusercontent.com/arasovic/claude-code-mods/main/docs/turn-footer.png" alt="turn-footer" width="260"></a><br><a href="https://github.com/arasovic/claude-code-mods/tree/main/turn-footer"><b>turn-footer</b></a> by arasovic<br>Turns the line under each answer into a summary of tools, requests, tokens and cache hits.</td>
<td width="33%" valign="top"><a href="https://github.com/arasovic/claude-code-mods/tree/main/turn-timeline"><img src="https://raw.githubusercontent.com/arasovic/claude-code-mods/main/docs/turn-timeline.png" alt="turn-timeline" width="260"></a><br><a href="https://github.com/arasovic/claude-code-mods/tree/main/turn-timeline"><b>turn-timeline</b></a> by arasovic<br>Draws the current turn as a timeline pane showing where time went and the slowest steps.</td>
<td width="33%" valign="top"><a href="https://github.com/BatuhanCakmakk/wavy-usage"><img src="https://raw.githubusercontent.com/BatuhanCakmakk/wavy-usage/main/docs/band.png" alt="wavy-usage" width="260"></a><br><a href="https://github.com/BatuhanCakmakk/wavy-usage"><b>wavy-usage</b></a> by BatuhanCakmakk<br>Liquid-filled rings for 5-hour and 7-day limits, context fill and cache time, with a jet showing effort.</td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://github.com/tzafrir/whats-agent-doing"><img src="https://raw.githubusercontent.com/tzafrir/whats-agent-doing/main/media/hero.gif" alt="whats-agent-doing" width="260"></a><br><a href="https://github.com/tzafrir/whats-agent-doing"><b>whats-agent-doing</b></a> by tzafrir<br>Names the step Claude is on in plain English above the prompt, with elapsed time and a clickable step history.</td>
</tr>
</table>

## All mods

- [Pets and fun](#pets-and-fun)
- [Usage and limits](#usage-and-limits)
- [Context and sessions](#context-and-sessions)
- [Agents and tasks](#agents-and-tasks)
- [Reading and viewing](#reading-and-viewing)
- [Themes and looks](#themes-and-looks)
- [Sound and alerts](#sound-and-alerts)
- [Productivity](#productivity)

## Pets and fun

- [adlib-lyrics](https://github.com/bixxter/adlib-lyrics) by bixxter - Shows synced lyrics from Apple Music or Spotify above the prompt, with a small dancing mascot.
- [cc-arcade](https://github.com/sezaakgun/cc-arcade) by sezaakgun - A set of terminal games above the prompt plus a pet that grows as Claude tests and commits.
- [chess](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/mods/games/chess) by davila7 - Play chess against Claude in a side pane, with the token cost of each Claude move shown.
- [claude-cat-mod](https://github.com/matthlh/claude-cat-mod) by matthlh - A pixel cat above the prompt that wanders, tracks usage limits and signals when Claude finishes.
- [claudelingo](https://github.com/AI-Experts-LLC/claudelingo) by AI-Experts-LLC - Shows a vocabulary quiz card above the prompt while Claude thinks, so waiting time becomes language practice.
- [clawd-spinner](https://github.com/scoobynko/claude-code-mods/tree/main/plugins/clawd-spinner) by scoobynko - Clawd types on a tiny laptop under the spinner as code floats out and tokens float in.
- [diff-invaders](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/mods/games/diff-invaders) by davila7 - Space Invaders where each wave is built from the lines Claude just added with Edit or Write.
- [emotion-statusline](https://github.com/bencium/bencium-marketplace/tree/main/emotion-statusline) by bencium - Shows Claude's classified emotional state in the status line, with a warning on reward hacking.
- [idle-art](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/idle-art) by KilimcininKorOglu - Draws an ASCII animation above the prompt while the model works, such as matrix rain, fire or a cat.
- [little-harvest](https://github.com/theonly1me/claude-code-mods/tree/main/plugins/little-harvest) by theonly1me - A garden that grows a little with each Claude turn.
- [night-feast](https://github.com/theonly1me/claude-code-mods/tree/main/plugins/night-feast) by theonly1me - A vampire hunts villagers on screen while Claude works.
- [pacman](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/mods/games/pacman) by davila7 - Pac-Man with four ghosts, power pellets and three lives above the prompt.
- [pocket-familiar](https://github.com/theonly1me/claude-code-mods/tree/main/plugins/pocket-familiar) by theonly1me - A growing companion creature that lives alongside your work.
- [reels](https://github.com/hamzafer/claude-code-mods/tree/main/mods/reels) by hamzafer - Plays YouTube Shorts in a terminal pane while Claude works and pauses when it finishes.
- [ricky-pixel-mod](https://github.com/muxia23/ricky-pixel-mod) by muxia23 - An animated starry-sky mascot that changes expression with Claude's state, plus a board of tasks, subagents and edited files.
- [samurai-dojo](https://github.com/theonly1me/claude-code-mods/tree/main/plugins/samurai-dojo) by theonly1me - A samurai trains, meditates and fights on screen while Claude works.
- [snake](https://github.com/hamzafer/claude-code-mods/tree/main/mods/snake) by hamzafer - Snake in a pane while Claude works, paused when it finishes, opened only with /snake.
- [terminal-gym](https://github.com/DrumAndCode/terminal-gym) by DrumAndCode - Log bodyweight sets from a band above the prompt while Claude works, with a daily goal and streak.
- [token-monster](https://github.com/ugglr/claude-token-monster) by ugglr - A pixel-art monster in a side pane that eats tokens and shows context, limits and activity.
- [tool-defense](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/mods/games/tool-defense) by davila7 - A tower defense where each enemy is one of Claude's real tool calls, such as Bash runners.

## Usage and limits

- [bash-diet](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/bash-diet) by KilimcininKorOglu - Shrinks each Bash result with per-command filters before the model reads it, keeping the full output available.
- [cache-meter](https://github.com/DarioFontanel/claude-code-mods/tree/main/cache-meter) by DarioFontanel - A bar above the prompt that drains as the hour of prompt cache runs out.
- [cache-timer](https://github.com/arasovic/claude-code-mods/tree/main/cache-timer) by arasovic - Counts down to when the prompt cache expires so you can send before it goes cold.
- [cache-timer](https://github.com/EricJamie/claude-code-mods/tree/main/plugins/cache-timer) by EricJamie - A countdown to prompt cache expiry, shown in the prompt footer before the model name.
- [context-band](https://github.com/EricJamie/claude-code-mods/tree/main/plugins/context-band) by EricJamie - A band above the prompt with rate limits, tokens, speed, cache, cost and context fill.
- [context-level](https://github.com/tobihagemann/turbo/tree/main/claude/skills/context-level) by tobihagemann - Gives Claude a tool that reads how much of the context window remains.
- [context-tokens](https://github.com/0xBADC0FFEE/claude-code-mods/tree/main/context-tokens) by 0xBADC0FFEE - Shows context tokens in use beside the desktop app's prompt footer, colored green, yellow or red.
- [cost-git](https://github.com/juulsverne/claude-code-mods/tree/main/cost-git) by juulsverne - A band above the prompt with session cost, git branch and status, CI, and pull and push buttons.
- [effort-auto](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/effort-auto) by KilimcininKorOglu - Has a small model rate each prompt's difficulty and runs that turn and its subagents at a matching effort.
- [gemini-compact](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/gemini-compact) by KilimcininKorOglu - Hands context compaction to Gemini so the summary does not count against your Claude usage.
- [jev-model-router](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/mods/productivity/jev-model-router) by davila7 - Chooses the model and reasoning effort for each task using TypeSafe's Jev decision model.
- [jev-pruner](https://github.com/tamaratran/jev-pruner) by tamaratran - Uses Jev to trim noisy Bash output after the command runs and before the model sees it.
- [jev-skill-suggestion](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/mods/productivity/jev-skill-suggestion) by davila7 - Removes the skill listing from context and lets Jev pick at most one skill per prompt.
- [lean-ctx](https://github.com/yvgude/lean-ctx/tree/main/integrations/claude-code-mod) by yvgude - Wakes on background job completion, trims redundant hook context, shapes Bash output and shows per-session usage.
- [limit-watch](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/limit-watch) by KilimcininKorOglu - Shows subscription usage limits under the prompt with a reset countdown, projection and a detail pane.
- [output-flood](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/output-flood) by KilimcininKorOglu - Measures context spent per Bash command and suggests a narrower command when output is too large.
- [prompt-cache-control](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/mods/observability/prompt-cache-control) by davila7 - A prompt cache meter above the prompt showing read, written and uncached tokens and when the cache lapses.
- [prompt-offload](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/prompt-offload) by KilimcininKorOglu - Writes an over-long prompt to a temp file and sends the model its start and the path.
- [reminder-log](https://github.com/schreibse/claude-code-mods/tree/main/reminder-log) by schreibse - Tallies reminders Claude Code injects per session and drops the token counter and repeated attribution blocks.
- [run-breakdown](https://github.com/wickedhardflip/claude-code-mods/tree/main/run-breakdown) by wickedhardflip - After a long run, shows which model and effort the main session and each subagent used.
- [session-meter](https://github.com/arasovic/claude-code-mods/tree/main/session-meter) by arasovic - A live session pane with context breakdown, usage limits and pace, tool calls and model requests.
- [session-watch](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/session-watch) by KilimcininKorOglu - Shows context fill, token totals, cost, model, effort and other local sessions in a sidebar.
- [shunt](https://github.com/pleaseai/shunt/tree/main/plugins/shunt) by pleaseai - Shows the shared account pool's remaining headroom and reset times through /shunt:usage.
- [token-optimizer](https://github.com/alexgreensh/token-optimizer) by alexgreensh - Token Optimizer status bar showing context and token savings, shipped inside the token-optimizer plugin.
- [token-weather](https://github.com/hamzafer/claude-code-mods/tree/main/mods/token-weather) by hamzafer - A live forecast of the context window with a prompt cache countdown, drawn above the prompt.
- [token-weather](https://github.com/cskwork/claude-code-mods/tree/main/token-weather) by cskwork - A live forecast of the context window drawn above the prompt.
- [token-weather-usage](https://github.com/augiefra/claude-mods/tree/main/plugins/token-weather-usage) by augiefra - One line above the prompt showing context weather, token bars and 5-hour and 7-day limits with reset time.
- [usage-band](https://github.com/pawandeepdhall/claude-mods/tree/main/plugins/usage-band) by pawandeepdhall - Always-visible 5-hour and weekly usage with reset countdown, plus one-click new chat and push buttons.
- [usage-bars](https://github.com/AndreasOA/claude-code-mods/tree/main/plugins/usage-bars) by AndreasOA - Sparklines of context-window fill and tokens added per turn under the prompt.
- [usage-meter](https://github.com/hamzafer/claude-code-mods/tree/main/mods/usage-meter) by hamzafer - Small bars above the prompt for 5-hour and 7-day plan usage, reset countdown and session cost.
- [usage-meter](https://github.com/LeeHigma0201/claude-code-mods/tree/main/mods/usage-meter) by LeeHigma0201 - Status line meter for context fill, 5-hour and weekly plan limits and session cost.
- [usage-percent](https://github.com/schreibse/claude-code-mods/tree/main/usage-percent) by schreibse - Usage percentages under the prompt for context, 5-hour and weekly limits.
- [wavy-usage](https://github.com/BatuhanCakmakk/wavy-usage) by BatuhanCakmakk - Liquid-filled rings for 5-hour and 7-day limits, context fill and cache time, with a jet showing effort.
- [webfetch-cache](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/mods/productivity/webfetch-cache) by davila7 - Answers repeated WebFetch calls for the same URL and prompt from a session cache.
- [winnow](https://github.com/GhalebDweikat/winnow) by GhalebDweikat - Judges large Read, Bash and Grep results before they enter context and replaces blocks you do not need.

## Context and sessions

- [cache-keepalive](https://github.com/RichardJSun/claude-code-mods/tree/main/plugins/cache-keepalive) by RichardJSun - Keeps the prompt cache warm while background tasks run.
- [cache-keeper](https://github.com/nateherkai/claude-code-mods/tree/main/cache-keeper) by nateherkai - Keeps a big chat's prompt cache warm, warns before cold restarts and shows all local chats on a board.
- [cache-warm](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/cache-warm) by KilimcininKorOglu - Keeps the one-hour prompt cache warm for a chosen window with one cache-sharing fork per idle stretch.
- [caliber-jev-compaction](https://github.com/caliber-ai-org/ai-setup/tree/master/plugin/caliber-jev-compaction) by caliber-ai-org - Compacts context with Jev judging which tool calls to drop, for the Caliber context layer.
- [claude-fleet](https://github.com/Dubbus/claude-fleet) by Dubbus - Lists every Claude session on your machine with what it is doing, its code state and context size.
- [compact-keeper](https://github.com/arasovic/claude-code-mods/tree/main/compact-keeper) by arasovic - Saves each compaction summary and the edited files to a handoffs folder so pre-compact context can be recovered.
- [context-restore](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/context-restore) by KilimcininKorOglu - Gives a skill or command the current text of its file when it changed on disk after session start.
- [ctx-handoff-mod](https://github.com/cablate/ctx-handoff-mod) by cablate - Hands a long conversation to a fresh one at a context threshold and keeps the prompt cache warm meanwhile.
- [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) by tamaratran - Replaces compaction with the original messages minus the tool calls Jev judged no longer needed.
- [jev-auto-compact](https://github.com/notque/vexjoy-agent/tree/main/plugins/jev-auto-compact) by notque - At 60 percent context, prunes stale tool calls with Jev and zero generation, never using the LLM summarizer.
- [memory-lens](https://github.com/yonatangross/orchestkit/tree/main/mods/memory-lens) by yonatangross - Recalls the few memories related to each prompt, one line for you and one entry for the model.
- [memory-save](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/memory-save) by KilimcininKorOglu - Loads MEMORY.md into the session and saves project learnings to it after each turn in the background.
- [navigator](https://github.com/qf-studio/navigator) by qf-studio - Context engineering plugin that loads documentation on demand to keep most of the context window free.
- [obsidian-mind](https://github.com/breferrari/obsidian-mind/tree/main/.claude/skills/obsidian-mind) by breferrari - Delivers an Obsidian vault's session context as an instruction file that survives compaction.
- [pin-board](https://github.com/arasovic/claude-code-mods/tree/main/pin-board) by arasovic - Pins standing notes with /pin that survive /compact and /clear and show in a row above the prompt.
- [pin-note](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/pin-note) by KilimcininKorOglu - Keeps notes you pin and resends them word for word after each compaction and /clear.
- [reflect-mod](https://github.com/BayramAnnakov/claude-reflect/tree/main/mod) by BayramAnnakov - Finds reusable corrections in your prompts and offers to save them to CLAUDE.md from a band.
- [repowise](https://github.com/repowise-dev/repowise/tree/main/plugins/claude-code) by repowise-dev - Gives Claude codebase context such as architecture, ownership, hotspots and a code-health score.
- [resume-nudge](https://github.com/LeeHigma0201/claude-code-mods/tree/main/mods/resume-nudge) by LeeHigma0201 - Detects a session cut off mid-turn and drafts the pick-up prompt, sent with /resume-here.
- [sage-memory](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/sage-memory) by KilimcininKorOglu - Keeps project and global memories in SQLite through a local daemon and hands the model matching entries.
- [session-recap](https://github.com/wickedhardflip/claude-code-mods/tree/main/session-recap) by wickedhardflip - A band above the prompt with open questions Claude asked and bullets of what the last prompt did.
- [session-saver](https://github.com/hamzafer/claude-code-mods/tree/main/mods/session-saver) by hamzafer - Names untitled sessions, saves where you left off with /park and shows it again on resume.
- [session-time-machine](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/mods/productivity/session-time-machine) by davila7 - Draws the session as a timeline and writes a copy cut at any point you choose for a fresh start.
- [storybloq](https://github.com/Storybloq/storybloq/tree/main/plugins/storybloq) by Storybloq - Keeps stories, plans, handovers and review evidence beside your code so work continues across sessions.
- [supermemory](https://github.com/supermemoryai/claude-supermemory/tree/main/plugin) by supermemoryai - Persistent memory across Claude Code sessions using Supermemory.
- [where-am-i](https://github.com/hamzafer/claude-code-mods/tree/main/mods/where-am-i) by hamzafer - A live recap above the prompt of the goal, current work, what waits on you and what is next.

## Agents and tasks

- [agent-flow](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/mods/ui/agent-flow) by davila7 - A side pane drawing the main loop's context and every subagent as a tree, live.
- [agent-radar](https://github.com/hamzafer/claude-code-mods/tree/main/mods/agent-radar) by hamzafer - One live line above the prompt per running subagent with time, tool count and current action.
- [agent-watch](https://github.com/AndreasOA/claude-code-mods/tree/main/plugins/agent-watch) by AndreasOA - Docks a narrow pane beside the transcript that follows each running subagent live.
- [amp-inbox-band](https://github.com/23blocks-OS/ai-maestro/tree/main/mods/amp-inbox-band) by 23blocks-OS - Shows unread AMP messages above the prompt and can wake an idle session to read them.
- [ask-autopick](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/ask-autopick) by KilimcininKorOglu - Picks the recommended answer to a question left unanswered for a set time so a deserted session keeps going.
- [bg-tasks](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/bg-tasks) by KilimcininKorOglu - Shows the session's background shell tasks with the oldest one's age and lets you stop one from a pane.
- [browser-lanes](https://github.com/hamzafer/claude-code-mods/tree/main/mods/browser-lanes) by hamzafer - Shows whether the session holds a Playwright browser and makes subagents wait for it instead of clashing.
- [bughunt](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/bughunt) by KilimcininKorOglu - Runs bug hunt rounds where each round proves a bug with a failing command, fixes it and proves the fix.
- [cc-persistent-monitor](https://github.com/ruihe774/cc-persistent-monitor) by ruihe774 - Restores watches without a deadline, working around the 30 minute cap on the built-in Monitor tool.
- [claude-agentpane](https://github.com/xuanji86/claude-agentpane) by xuanji86 - A pane beside the chat showing each subagent's current activity, token cost and full conversation.
- [claude-council](https://github.com/hex/claude-council) by hex - Consults several AI coding agents in parallel and shows their answers side by side.
- [claude-flightdeck](https://github.com/scasella/claude-flightdeck) by scasella - A terminal dashboard of context, cost, advisor timeline, permission checks and subagents as cards or swimlanes.
- [collision-guard](https://github.com/nateherkai/claude-code-mods/tree/main/collision-guard) by nateherkai - Asks before Claude edits a file that another open chat changed in the last 30 minutes.
- [council](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/council) by KilimcininKorOglu - Asks a council of Claude and Gemini models about a hard problem, from a tool call or /council.
- [edit-loop](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/edit-loop) by KilimcininKorOglu - Adds a note on the fifth edit of one file in a turn so the model states the root cause.
- [error-poke](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/error-poke) by KilimcininKorOglu - Sends a continue prompt after a turn killed by an API error so half-done work carries on.
- [fable-pin](https://github.com/karanb192/claude-code-mods/tree/main/plugins/fable-pin) by karanb192 - Pins every subagent to the fable model by rewriting the model on spawn, toggled with /fable-pin.
- [gemini-advisor](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/gemini-advisor) by KilimcininKorOglu - Gives the model a tool that asks Gemini for a second opinion on the whole conversation.
- [gemini-plan-review](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/gemini-plan-review) by KilimcininKorOglu - Has Gemini review each plan before the approval dialog and sends back plans with blocking findings.
- [goal-meter](https://github.com/nateherkai/claude-code-mods/tree/main/goal-meter) by nateherkai - A progress bar for /goal built from Claude's task plan, with elapsed time and an estimated finish.
- [gsd-status-mod](https://github.com/helenkwok/gsd-status-mod) by helenkwok - A live dashboard for GSD projects showing the roadmap, current phase and an agent tree with live clocks.
- [loop-guard](https://github.com/arasovic/claude-code-mods/tree/main/loop-guard) by arasovic - Tells the model silently to stop when the same call fails twice with the same error.
- [mission-control](https://github.com/hamzafer/claude-code-mods/tree/main/mods/mission-control) by hamzafer - Opens a live map of the main agent, subagents and every tool call, plus a code map of touched files.
- [multi-core](https://github.com/greenpolo/cc-multi-cli-plugin/tree/main/plugins/multi-core) by greenpolo - Brings OpenAI, Cursor, OpenCode and other external models into a session through the model picker.
- [pi-agent-for-claude](https://github.com/FazalAAli/pi-agent-for-claude) by FazalAAli - Adds a pi subagent type whose steps run the pi CLI inside Claude Code's own agent UI.
- [ruflo-mods](https://github.com/ruvnet/ruflo/tree/main/plugins/ruflo-mods) by ruvnet - Runs ruflo as a Claude Code mod, on by default in newer versions.
- [search-meter](https://github.com/arasovic/claude-code-mods/tree/main/search-meter) by arasovic - Counts the model's searches and colors each by whether it found the answer first try, late or not at all.
- [subagent-ledger](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/subagent-ledger) by KilimcininKorOglu - Lists each subagent with turns, time, model and tokens, costliest first, colored by state.
- [subagent-models](https://github.com/wickedhardflip/claude-code-mods/tree/main/subagent-models) by wickedhardflip - Status line showing which model each running subagent uses.
- [task-poke](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/task-poke) by KilimcininKorOglu - Submits a continue prompt while the task list has unfinished tasks, up to a set limit.
- [tool-coach](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/tool-coach) by KilimcininKorOglu - Stops the model from repeating a tool call that just failed with the same input.
- [tripwire](https://github.com/oaustegard/claude-code-mods/tree/main/tripwire) by oaustegard - Catches recurring agent mistakes from past transcripts, such as whole-disk find and masked errors.
- [turn-timeline](https://github.com/arasovic/claude-code-mods/tree/main/turn-timeline) by arasovic - Draws the current turn as a timeline pane showing where time went and the slowest steps.
- [whats-agent-doing](https://github.com/tzafrir/whats-agent-doing) by tzafrir - Names the step Claude is on in plain English above the prompt, with elapsed time and a clickable step history.

## Reading and viewing

- [behavior-map](https://github.com/theonly1me/claude-code-mods/tree/main/plugins/behavior-map) by theonly1me - Shows before and after behavior flows for a change, backed by evidence.
- [change-journal](https://github.com/theonly1me/claude-code-mods/tree/main/plugins/change-journal) by theonly1me - Live explanations of edits with supporting code and checks.
- [change-ledger](https://github.com/arasovic/claude-code-mods/tree/main/change-ledger) by arasovic - Lists files edited this session in a pane with line counts and who edited them.
- [claude-mdview](https://github.com/xuanji86/claude-mdview) by xuanji86 - Click a Markdown path Claude mentions to read the rendered file in a pane beside the chat.
- [crit-tui](https://github.com/tomasz-tomczyk/crit/tree/main/integrations/claude-code-tui) by tomasz-tomczyk - Early crit integration: comment on the conversation, diff or a file in a pane and send the review to Claude.
- [diagram-render](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/diagram-render) by KilimcininKorOglu - Renders mermaid blocks in replies with mmdc after each turn and draws the picture under the reply.
- [diff](https://github.com/anthropics/claude-code/tree/main/mods/diff) by anthropics - Opens the session's uncommitted changes beside the transcript, file by file, refreshed as Claude edits.
- [image-peek](https://github.com/karanb192/claude-code-mods/tree/main/plugins/image-peek) by karanb192 - Previews pasted images at their prompt markers on macOS in Ghostty, with experimental iTerm2 support.
- [image-peek](https://github.com/arasovic/claude-code-mods/tree/main/image-peek) by arasovic - Shows pasted images as thumbnails above the prompt and larger under each sent message in kitty-graphics terminals.
- [image-preview](https://github.com/scoobynko/claude-code-mods/tree/main/plugins/image-preview) by scoobynko - Opens a pane listing every image in the session and shows the one you pick.
- [md-preview](https://github.com/hamzafer/claude-code-mods/tree/main/mods/md-preview) by hamzafer - Shows Markdown files Claude edits rendered like GitHub in a side pane, with before and after views.
- [md-view](https://github.com/scoobynko/claude-code-mods/tree/main/plugins/md-view) by scoobynko - Click a Markdown file in Claude's reply to read it rendered in a side pane.
- [replay-theater](https://github.com/hamzafer/claude-code-mods/tree/main/mods/replay-theater) by hamzafer - Steps through the last turn's file edits one diff at a time.
- [replay-theater](https://github.com/DarioFontanel/claude-code-mods/tree/main/replay-theater) by DarioFontanel - Steps through the file edits Claude made in the last turn, one diff at a time.
- [shot-inline](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/shot-inline) by KilimcininKorOglu - Draws each PNG or JPG the model saves or reads under its tool row.
- [show-me](https://github.com/arasovic/claude-code-mods/tree/main/show-me) by arasovic - Draws the mermaid diagrams of each answer as images in a pane, using mmdc and a kitty-graphics terminal.
- [terminal-browser](https://github.com/zenbu-labs/terminal-browser/tree/main/claude-code-plugin) by zenbu-labs - A browser inside Claude Code to preview sites and HTML files that the agent can also control.
- [touched](https://github.com/sverma24/claude-code-mods/tree/main/touched) by sverma24 - Opens a pane listing every file Claude read or edited this session, with counts.

## Themes and looks

- [firstmate-calm](https://github.com/kunchenguid/firstmate/tree/main/.claude/mods/firstmate-calm) by kunchenguid - A sailboat working animation and a conversation-only transcript view.
- [prismantis](https://github.com/NahumLitvin/prismantis) by NahumLitvin - Renders replies with colored tables, code, diagrams and charts in 15 themes, with copy buttons.
- [prompt-box](https://github.com/ekinertac/claude-code-mods/tree/master/prompt-box) by ekinertac - Draws your prompts in the scrollback inside a thick colored box so they are easy to find.
- [prompt-time](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/prompt-time) by KilimcininKorOglu - Draws the time under each of your messages and each reply block.
- [quiet-bash](https://github.com/schreibse/claude-code-mods/tree/main/quiet-bash) by schreibse - One-line transcript rows for Bash calls and plan-file edits, with /quiet to show full rows.
- [quiet-spinner](https://github.com/schreibse/claude-code-mods/tree/main/quiet-spinner) by schreibse - Plain words for the turn spinner and the turn-duration line.
- [sidebar](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/sidebar) by KilimcininKorOglu - Opens one shared pane beside the transcript that other mods write sections and buttons into.
- [tool-oneline](https://github.com/ekinertac/claude-code-mods/tree/master/tool-oneline) by ekinertac - Folds tool calls in the scrollback into one line per call or per run of calls.
- [tool-timing-badge](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/mods/ui/tool-timing-badge) by davila7 - Times every tool call and shows a colored duration badge on each tool row.
- [turn-footer](https://github.com/arasovic/claude-code-mods/tree/main/turn-footer) by arasovic - Turns the line under each answer into a summary of tools, requests, tokens and cache hits.

## Sound and alerts

- [cuelume](https://github.com/danielwh2/cuelume/tree/main/claude-code) by danielwh2 - Plays one sound when a long turn ends and another when a permission prompt waits.
- [desk-notify](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/desk-notify) by KilimcininKorOglu - Sends a desktop notification when a question or plan waits for you, and when a turn ends or fails.
- [red-alert](https://github.com/dukechain2333/red-alert/tree/main/plugin) by dukechain2333 - Claude sounds an alert through your speakers when its work deserves attention, from a chirp to a red alert.

## Productivity

- [action-pin](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/action-pin) by KilimcininKorOglu - After an edit adds a tag-pinned GitHub Actions step, names the commit SHA to use instead.
- [admin-capability-lockdown](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/mods/enterprise/admin-capability-lockdown) by davila7 - Organization mod that withholds network and process access from plugins and restricts them by allowlist.
- [agents-md](https://github.com/anthropics/claude-code/tree/main/mods/agents-md) by anthropics - Loads AGENTS.md files the way CLAUDE.md is loaded when a project has no instruction files of its own.
- [aitmpl](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/mods/productivity/aitmpl) by davila7 - Opens a side pane for the aitmpl.com catalog with search, browse menu and an installed section.
- [blast-radius](https://github.com/hamzafer/claude-code-mods/tree/main/mods/blast-radius) by hamzafer - Holds risky Bash commands and shows what they would change before they run.
- [blast-radius](https://github.com/cskwork/claude-code-mods/tree/main/blast-radius) by cskwork - Dry-runs risky Bash commands such as recursive deletes and destructive git, then asks Proceed or Cancel.
- [block-destructive-commands](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/mods/security/block-destructive-commands) by davila7 - Denies Bash commands matching destructive patterns such as recursive root rm, force push and hard reset.
- [check-ledger](https://github.com/LeeHigma0201/claude-code-mods/tree/main/mods/check-ledger) by LeeHigma0201 - Records which real checks ran and which files changed afterwards, so Claude can cite evidence before claiming tested.
- [checkpoint](https://github.com/sverma24/claude-code-mods/tree/main/checkpoint) by sverma24 - Commits files Claude edited as a git checkpoint after each turn and adds /rollback to undo.
- [ci-watch](https://github.com/arasovic/claude-code-mods/tree/main/ci-watch) by arasovic - Watches GitHub Actions in a band above the prompt after a push, PR or tag, with progress bars.
- [claude-code-effort-cycle](https://github.com/Anerco/claude-code-effort-cycle) by Anerco - Cycles reasoning effort levels with Alt+E and Alt+Shift+E, leaving nothing in the transcript.
- [coderabbit-band](https://github.com/schreibse/claude-code-mods/tree/main/coderabbit-band) by schreibse - A band above the prompt with the open CodeRabbit threads and nitpicks of the branch's MR.
- [commit-cadence](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/commit-cadence) by KilimcininKorOglu - Names uncommitted files at the end of each turn and tells the model to commit finished pieces.
- [config-parse](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/config-parse) by KilimcininKorOglu - Parses each JSON, YAML, TOML or .env file Claude edits and reports parse errors at once.
- [contract-watch](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/contract-watch) by KilimcininKorOglu - After a function signature changes, adds the callers that need updating to the edit result.
- [dep-sentinel](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/dep-sentinel) by KilimcininKorOglu - Checks each installed package against its registry and OSV.dev and stops missing, brand-new, look-alike or vulnerable ones.
- [deskbar](https://github.com/0NE-C0DEMAN/deskbar) by 0NE-C0DEMAN - A row of widgets above the prompt for context weather, Gmail, calendar and more, each opening a dropdown.
- [disk-janitor](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/disk-janitor) by KilimcininKorOglu - Measures build artifacts in the repository, shows them on the status line and deletes the ones you pick.
- [doc-drift-watch](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/doc-drift-watch) by KilimcininKorOglu - After each commit, lists the doc lines the commit made stale, such as file references and symbol names.
- [env-sync](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/env-sync) by KilimcininKorOglu - After each commit, names env variables the new lines read that .env.example lacks.
- [first-mod](https://github.com/wickedhardflip/claude-code-mods/tree/main/first-mod) by wickedhardflip - Starter mod that shows a toast on start and counts tool calls in the status line.
- [flaky-memory](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/flaky-memory) by KilimcininKorOglu - Remembers which tests failed on which code and tells the model when a test is flaky on the same code.
- [gemini-core](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/gemini-core) by KilimcininKorOglu - Keeps Gemini keys, tier and per-mod model settings in one place for every Gemini mod.
- [gemini-review](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/gemini-review) by KilimcininKorOglu - Has Gemini review every git commit the model runs and stops commits with a blocking finding.
- [git-commit](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/git-commit) by KilimcininKorOglu - Ships a commit skill and holds every Bash git commit to it, blocking blanket adds, secrets and ignored paths.
- [git-sidebar](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/mods/ui/git-sidebar) by davila7 - A lazygit-style pane listing worktrees and branches as clickable rows that move the session.
- [glance](https://github.com/hamzafer/claude-code-mods/tree/main/mods/glance) by hamzafer - One line above the prompt showing next meeting, pull requests, Linear issues and Slack DMs that need you.
- [guardrails](https://github.com/arasovic/claude-code-mods/tree/main/guardrails) by arasovic - Blocks Cloudflare write commands, attribution lines in commits and PRs, and claude/ branch names.
- [hal-grammar-check](https://github.com/vinta/hal-9000/tree/main/plugins/hal-grammar-check) by vinta - Grammar-checks your prompt as you type, shown above the prompt box.
- [i18n-watch](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/i18n-watch) by KilimcininKorOglu - After an edit that uses translation keys, names the keys and languages the locale files lack.
- [jev-auto-mode](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/mods/security/jev-auto-mode) by davila7 - A JSON-policy permission layer that decides tool calls and slash commands, sending uncovered cases to Jev.
- [jev-guardrails](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/mods/security/jev-guardrails) by davila7 - Screens every prompt and reply with Jev using yes or no hazard questions and a harm score.
- [jev-vercel-sandbox](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/mods/security/jev-vercel-sandbox) by davila7 - Lets Claude send long or untrusted work to an isolated Vercel Sandbox microVM.
- [large-edit-confirmation](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/mods/security/large-edit-confirmation) by davila7 - Asks before Claude edits or overwrites a file larger than a set line count.
- [lesson-cards](https://github.com/yonatangross/orchestkit/tree/main/mods/lesson-cards) by yonatangross - Displays lesson hint cards when tool calls match known patterns.
- [linear-tickets](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/mods/integrations/linear-tickets) by davila7 - Shows your Linear tickets in a side pane with status and a chart of your progress.
- [lockfile-sync](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/lockfile-sync) by KilimcininKorOglu - After each commit, names manifests whose dependencies changed without a matching lockfile update.
- [mcp-doctor](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/mcp-doctor) by KilimcininKorOglu - Tells you when an MCP server fails or drops, with the reason and a reconnect button.
- [merge-gate](https://github.com/hamzafer/claude-code-mods/tree/main/mods/merge-gate) by hamzafer - Holds gh pr merge until CI passes and a Codex review has run, with a PR status line.
- [mobile-mcp](https://github.com/mobile-next/mobile-mcp/tree/main/plugin) by mobile-next - Mobile device automation server plus a live, clickable device screen in a pane.
- [mod-doctor](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/mod-doctor) by KilimcininKorOglu - Names installed plugins whose local clone offers a newer version, with the update command.
- [mod-scout](https://github.com/LeeHigma0201/claude-code-mods/tree/main/mods/mod-scout) by LeeHigma0201 - Scans recent sessions and ranks the mods you would use most, with a skill that builds them.
- [modscope](https://github.com/CommunityPokeOrg/claude-code-modscope/tree/main/plugins/modscope) by CommunityPokeOrg - Inspects loaded mods and attributes hook failures and slow handlers to the mod that caused them.
- [mr-banner](https://github.com/schreibse/claude-code-mods/tree/main/mr-banner) by schreibse - A colored card with a link under each MR or PR created, merged, approved or reviewed.
- [neon-branch-per-session](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/mods/integrations/neon-branch-per-session) by davila7 - Gives each session its own Neon database branch and DATABASE_URL, so Claude can migrate and seed without touching production data.
- [next-steps](https://github.com/hamzafer/claude-code-mods/tree/main/mods/next-steps) by hamzafer - Suggests two or three likely next prompts above the prompt after each turn, drafted with a keypress.
- [next-steps](https://github.com/pawandeepdhall/claude-mods/tree/main/plugins/next-steps) by pawandeepdhall - Suggests up to three next steps as one-click buttons above the prompt after each reply.
- [next-steps](https://github.com/DarioFontanel/claude-code-mods/tree/main/next-steps) by DarioFontanel - Three buttons above the prompt after each turn: the next two likely steps and Replay.
- [next-steps](https://github.com/anthropics/claude-plugins-community/tree/main/next-steps) by anthropics - Suggests up to three next prompts above the input, put in the prompt box as an editable draft.
- [npm-to-pnpm-rewriter](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/mods/productivity/npm-to-pnpm-rewriter) by davila7 - Rewrites npm and npx commands to pnpm, yarn or bun before the Bash tool runs them.
- [orphan-server](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/orphan-server) by KilimcininKorOglu - Lists servers Claude started that still listen on a port and stops one on request.
- [plannotator](https://github.com/backnotprop/plannotator/tree/main/apps/hook) by backnotprop - Opens plans in a visual UI for markup and team sharing, hooking into plan mode.
- [probe-runner](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/probe-runner) by KilimcininKorOglu - For mod authors: runs a live check of plugins in a fresh tmux session and collects the results.
- [promote-lights](https://github.com/yonatangross/orchestkit/tree/main/mods/promote-lights) by yonatangross - CI status lights above the prompt while a promote PR against main is open.
- [prompt-deck](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/prompt-deck) by KilimcininKorOglu - Learns short prompts you send often and shows them above the prompt, selectable with a digit key.
- [prompt-optimizer](https://github.com/bai-collab/claude_code_mod/tree/claude/stoic-carson-pqpwmt/plugins/prompt-optimizer) by bai-collab - Attaches hidden clarify-or-proceed guidance to short or vague prompts.
- [protect-env-files](https://github.com/cprussin/claude-code-mods/tree/main/packages/protect-env-files) by cprussin - Sample mod that denies edits to .env files.
- [protected-paths-guard](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/mods/security/protected-paths-guard) by davila7 - Denies edits to sensitive paths such as .env files, lockfiles, CI workflows and private keys.
- [quick-buttons](https://github.com/DarioFontanel/claude-code-mods/tree/main/quick-buttons) by DarioFontanel - A panel of buttons for skills and commands you choose at first launch, run with one click.
- [recording-mode](https://github.com/nateherkai/claude-code-mods/tree/main/recording-mode) by nateherkai - Masks keys, personal details and business figures on screen and keeps private files closed while you record.
- [redact](https://github.com/schreibse/claude-code-mods/tree/main/redact) by schreibse - Replaces secrets found by betterleaks with tokens the model sees, restored on Write and Edit.
- [remctl](https://github.com/viticci/remctl/tree/main/plugins/claude-code) by viticci - A Today band for Apple Reminders above the prompt, part of RemCTL.
- [rewrite-prompt](https://github.com/ekinertac/claude-code-mods/tree/master/rewrite-prompt) by ekinertac - Ctrl+P rewrites the draft in the prompt box before you send it.
- [rulebook-guard](https://github.com/hamzafer/claude-code-mods/tree/main/mods/rulebook-guard) by hamzafer - Enforces writing and git rules: replaces em dashes and asks before amends, unformatted pushes or personal data.
- [sec-default](https://github.com/anthropics/claude-code/tree/main/mods/sec-default) by anthropics - Organization security default that keeps classic hooks, prompt content, settings and tool policy out of plugin reach.
- [secret-guard](https://github.com/arasovic/claude-code-mods/tree/main/secret-guard) by arasovic - Hides API keys and private keys before the model or transcript sees them and blocks credential file reads.
- [secret-guard](https://github.com/sverma24/claude-code-mods/tree/main/secret-guard) by sverma24 - Blocks reads of .env files and printing of API keys, with a red warning above the prompt.
- [secret-redactor](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/mods/security/secret-redactor) by davila7 - Redacts API keys, tokens, JWTs and connection strings from tool results before the model reads them.
- [secrets-veil](https://github.com/yonatangross/orchestkit/tree/main/mods/secrets-veil) by yonatangross - Masks secret values in tool results before the model reads them, with no way to reveal them.
- [self-command](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/self-command) by KilimcininKorOglu - For mod authors: lets the model run a slash command in its own session and read the output.
- [slash-chain](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/slash-chain) by KilimcininKorOglu - Runs slash commands joined with && in order and stops the chain at the first failure.
- [sql-concat-watch](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/sql-concat-watch) by KilimcininKorOglu - After an edit that builds SQL from strings, names each line so the model uses query parameters.
- [storage-guard](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/storage-guard) by KilimcininKorOglu - After an edit that stores browser data in localStorage or sessionStorage, names each line.
- [telemetry](https://github.com/anthropics/claude-code/tree/main/mods/telemetry) by anthropics - Lets plugins log events and mark feature use as first-party analytics rows sent in batches.
- [ua-fallback](https://github.com/KilimcininKorOglu/claude-code-mods/tree/main/plugins/ua-fallback) by KilimcininKorOglu - After a curl or wget blocked with 403 or 429, gives the model a browser User-Agent to retry with.
- [universal-audit-log](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/mods/observability/universal-audit-log) by davila7 - Records every tool call, prompt and turn event as JSON lines with origin plugin and timing.
- [vercel-deploys](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/mods/integrations/vercel-deploys) by davila7 - Shows your Vercel projects in a side pane with latest deployment state, domain, commit and live status.
- [websearch-to-exa](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/mods/integrations/websearch-to-exa) by davila7 - Routes the built-in WebSearch tool to the Exa search API while keeping the same result shape.
- [write-for-me](https://github.com/ekinertac/claude-code-mods/tree/master/write-for-me) by ekinertac - Ctrl+N writes your next prompt from the conversation so far, using a draft as a hint.

## Add a mod

Add an entry to `mods.json`, run `python3 build.py` and open a pull request. A mod qualifies when its repository is public, its `hooks/hooks.json` lists `modules`, and its README says how to install it. Describe what it does in one plain sentence, and pick a category: pets and fun, usage and limits, context and sessions, agents and tasks, reading and viewing, themes and looks, sound and alerts, productivity.

## Related

- [Mods documentation](https://code.claude.com/docs/en/plugins/mods/overview)
- [karanb192/awesome-claude-code-mods](https://github.com/karanb192/awesome-claude-code-mods): a scanned catalogue showing what each mod can read, write, run or send
- [lycfyi/awesome-claude-code-mods](https://github.com/lycfyi/awesome-claude-code-mods): a short list, each entry validated

List content: [CC0](license). Each mod belongs to its author under its own license.
