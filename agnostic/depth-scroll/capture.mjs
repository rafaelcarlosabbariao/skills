// Real-time capture of a depth-scroll page over the DevTools protocol.
//
//   node capture.mjs <url> <out.png> <at> [width] [height] [flags]
//
// <at> is a station index; a fraction (2.45) lands between two stations with snapping off, to
// see a transit, and "-" leaves the scroll where the page put it (a #stop in the url). Flags: --wait=ms (after the scroll, default 2500), --reduce (prefers-reduced-
// motion), --light (click the header's appearance toggle), --nav (press the arrow keys, follow
// the last contents link and a rail button, and report where each lands).
//
// Why not `chrome --headless --screenshot`: under --virtual-time-budget animation frames barely
// advance, so the eased camera never arrives, and a screenshot of a scrolled window can come back
// blank. Driving a real-time headless Chrome over the protocol runs frames at their real rate.
import { spawn } from 'node:child_process';
import { writeFileSync, rmSync } from 'node:fs';

const args = process.argv.slice(2);
const flags = Object.fromEntries(args.filter((a) => a.startsWith('--')).map((a) => { const [k, v] = a.slice(2).split('='); return [k, v ?? true]; }));
const [url, out, at = '0', w = '1280', h = '860'] = args.filter((a) => !a.startsWith('--'));
if (!url || !out) { console.error('usage: node capture.mjs <url> <out.png> <at> [width] [height] [--wait=ms] [--reduce] [--light] [--nav]'); process.exit(2); }

const CHROME = process.env.CHROME || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const port = 9300 + Math.floor(Math.random() * 500), dir = `/tmp/depth-scroll-cdp-${port}`;
const chrome = spawn(CHROME, ['--headless=new', '--disable-gpu', '--hide-scrollbars', '--allow-file-access-from-files',
  `--remote-debugging-port=${port}`, `--window-size=${w},${h}`, `--user-data-dir=${dir}`, 'about:blank'], { stdio: 'ignore' });
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

let ws;
for (let i = 0; i < 60 && !ws; i++) {
  try { const p = (await (await fetch(`http://127.0.0.1:${port}/json`)).json()).find((t) => t.type === 'page'); if (p) ws = new WebSocket(p.webSocketDebuggerUrl); } catch {}
  if (!ws) await sleep(100);
}
await new Promise((r) => ws.addEventListener('open', r));
let id = 0; const pending = new Map();
ws.addEventListener('message', (m) => { const d = JSON.parse(m.data); if (d.id && pending.has(d.id)) { pending.get(d.id)(d.result); pending.delete(d.id); } });
const send = (method, params = {}) => new Promise((r) => { const i = ++id; pending.set(i, r); ws.send(JSON.stringify({ id: i, method, params })); });
const ev = (expression) => send('Runtime.evaluate', { expression, returnByValue: true }).then((r) => r.result.value);

await send('Emulation.setDeviceMetricsOverride', { width: +w, height: +h, deviceScaleFactor: 1, mobile: +w < 500 });
if (flags.reduce) await send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: 'reduce' }] });
await send('Page.navigate', { url });
for (let i = 0; i < 100 && (await ev('document.readyState')) !== 'complete'; i++) await sleep(100);   // fonts and images in
await sleep(800);
if (flags.light) { await ev(`(document.querySelector('header.pin .pin-toggle')||{click(){}}).click()`); await sleep(300); }

const TOPS = `[...document.querySelectorAll('.stop')].map(s=>Math.round(s.getBoundingClientRect().top+scrollY))`;
const STATE = `(()=>{const sl=[...document.querySelectorAll('.slot')],ch=[...document.querySelectorAll('.ch')];
  return {y:Math.round(scrollY),front:sl.findIndex(s=>s.classList.contains('on')),
    rail:[...document.querySelectorAll('.rail button')].findIndex(b=>b.getAttribute('aria-current')==='true'),
    cardsShown:ch.filter(c=>+c.style.opacity>0.2).length,cardsLit:ch.filter(c=>c.classList.contains('lit')).length,
    deep:document.documentElement.classList.contains('deep'),pageWidth:document.documentElement.scrollWidth+'/'+innerWidth}})()`;

console.log('stops', JSON.stringify(await ev(TOPS)));
// <at> of "-" leaves the scroll where the page put it (a #stop in the url, or the top)
if (at !== '-') await ev(`(()=>{const st=${TOPS},a=${+at},i=Math.floor(a),f=a-i;if(f)document.documentElement.style.scrollSnapType='none';
  scrollTo(0,st[i]+(st[i+1]!==undefined?(st[i+1]-st[i])*f:0))})()`);
await sleep(+flags.wait || 2500);
console.log('at', at, JSON.stringify(await ev(STATE)));

if (flags.nav) {
  const key = async (k) => { const c = { ArrowDown: 40, ArrowUp: 38 }[k];
    await send('Input.dispatchKeyEvent', { type: 'keyDown', key: k, code: k, windowsVirtualKeyCode: c });
    await send('Input.dispatchKeyEvent', { type: 'keyUp', key: k, code: k, windowsVirtualKeyCode: c }); };
  await key('ArrowDown'); await sleep(1400); console.log('ArrowDown', JSON.stringify(await ev(STATE)));
  await key('ArrowUp'); await sleep(1400); console.log('ArrowUp', JSON.stringify(await ev(STATE)));
  await ev(`(()=>{const a=[...document.querySelectorAll('nav.pin-toc a')];a.length&&a[a.length-1].click()})()`); await sleep(1800);
  console.log('last contents link', JSON.stringify(await ev(STATE)));
  await ev(`(document.querySelectorAll('.rail button')[1]||{click(){}}).click()`); await sleep(1800);
  console.log('rail 1', JSON.stringify(await ev(STATE)));
}

const shot = await send('Page.captureScreenshot', { format: 'png' });
writeFileSync(out, Buffer.from(shot.data, 'base64'));
ws.close(); chrome.kill();
await sleep(200);
try { rmSync(dir, { recursive: true, force: true }); } catch {}
