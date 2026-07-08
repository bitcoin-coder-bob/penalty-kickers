# Penalty Kickers

A single page for triaging World Cup penalty takers into buckets, then seeing how
the buckets compare on scoring rate.

At the start you choose **2 or 3 buckets** and optionally **name** them; the names
then show on the sorting buttons, the results page, and the shared image.

For each player it pulls a couple of photos plus their name and country, and you
sort with:

- **swipe** left → A, right → B, down → C (3-bucket mode; touch or mouse drag), or
- the **← / → / ↓ arrow keys**, or
- the on-screen **buttons** (two or three, matching your choice).

**↑ Back** (header button, `↑` or Backspace) steps to the previous player so you
can revise a pick. After the last player it shows a **stats breakdown by bucket**:
overall conversion rate, each bucket's rate, and which bucket is most likely to
score. From there you can:

- **Share an image of the results** (uses the device share sheet on mobile, or
  downloads a PNG on desktop),
- download each bucket as `bucketA.txt` / `bucketB.txt` / `bucketC.txt`, or
- start over.

Picks are stored in the browser (localStorage), so you resume where you left off.

Photos and names are fetched live in the browser from Wikipedia, Wikimedia
Commons, and Wikidata (their APIs allow cross-origin requests), so there is no
server or API key. The whole thing is one static `index.html`, hosted on GitHub
Pages.

## Develop / rebuild

```sh
python3 build.py                 # regenerate index.html from template.html + players.txt
python3 -m http.server 8000      # then open http://localhost:8000
```

## Files

| File | Purpose |
|------|---------|
| `index.html` | The built static site (this is what GitHub Pages serves). |
| `template.html` | Source template with a `/*PLAYERS*/` token. |
| `build.py` | Injects the player data into `index.html`. |
| `players.txt` | Raw penalty-kick data (deduped to unique players at build time). |
