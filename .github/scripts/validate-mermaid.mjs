import { execFileSync } from 'node:child_process';
import { readFileSync } from 'node:fs';
import { JSDOM } from 'jsdom';

const window = new JSDOM('').window;
globalThis.window = window;
globalThis.document = window.document;
const { default: mermaid } = await import('mermaid');
mermaid.initialize({ startOnLoad: false, securityLevel: 'strict' });
const files = execFileSync('git', ['ls-files', '-z', '--', '*.md'], { encoding: 'utf8' })
  .split('\0').filter(Boolean);
let diagrams = 0;
let failures = 0;
for (const file of files) {
  const content = readFileSync(file, 'utf8');
  for (const match of content.matchAll(/^```mermaid[^\S\n]*\n([\s\S]*?)^```[^\S\n]*$/gm)) {
    const line = content.slice(0, match.index).split('\n').length;
    diagrams++;
    try {
      await mermaid.parse(match[1]);
    } catch (error) {
      failures++;
      console.error(`${file}:${line}: ${error.message}`);
    }
  }
}
window.close();
console.log(`Mermaid: ${diagrams} diagrams checked; ${failures} failures`);
process.exitCode = failures ? 1 : 0;
