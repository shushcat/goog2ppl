# goog2ppl

A Python script to convert Google Contacts to a format readable by [ppl](http://ppladdressbook.org/).

Takes a vcf file and splits it into separate cards named after the camelcase contents of their `N:` (name) lines.

## Caveats

- Hardly tested, but works for me. So backup first!
- Outputs bunches of vcf files to the directory from which it's run.

## Usage

From an initialized ppl directory:

1. Backup your contacts file: `cp <contacts file> <contacts file>.bak`;

2. Make vcards: `./goog2ppl.py <contacts file>`; and

3. Import your contacts to ppl: `git add *.vcf && git commit -a`.
