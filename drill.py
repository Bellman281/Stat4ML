#!/usr/bin/env python3
"""
drill.py -- a rustlings-style driller for the Stat4ML course.

Work the course one exercise at a time: run the next unfinished exercise,
read the first failing check, fix it in place, and watch it pass before
moving on. You meet every idea twice -- once building it, once debugging it.

No dependencies. Python exercises run on python3 (standard library only);
R exercises run on Rscript when it is installed. Nothing else is needed.

An exercise counts as "ready to drill" only when its reference solution
actually runs clean; chapters that are still just scaffolding are shown as
[~] not-authored and skipped, so you only ever drill real material.

Usage:
    python3 drill.py                 run the next unfinished exercise
    python3 drill.py next            same as above
    python3 drill.py watch           auto-rerun on save, advance on pass
    python3 drill.py list            show every exercise and its status
    python3 drill.py verify          integrity check (use this in CI)
    python3 drill.py reset           forget progress

Options:
    --lang {python,r,both}      default: python (adds r in 'both' if installed)
    --track {debug,build,both}  default: debug  (debug = fix the broken copy;
                                build = fill in the TODO version from scratch)
    --timeout SECONDS           default: 60
    --hint                      reveal the planted BUG/TODO notes for the item
    --strict                    (verify) also fail if any chapter is unauthored
    --no-color
"""
import argparse, json, os, re, shutil, subprocess, sys, time

ROOT = os.path.dirname(os.path.abspath(__file__))
STATE_PATH = os.path.join(ROOT, "drill_state.json")
PART_RE = re.compile(r"^part(\d+)_")
CH_RE = re.compile(r"ch(\d+)")
NUM_RE = re.compile(r"exercise0*(\d+)")

LANGS = {
    "python": dict(subdir="python", ext="py", cmd=["python3"], probe="python3"),
    "r":      dict(subdir="r",      ext="R",  cmd=["Rscript"],  probe="Rscript"),
}

LEVEL_SETS = {
    "bachelor": {"core"},
    "master": {"core", "proof"},
    "phd": {"core", "proof", "research"},
    "all": {"core", "proof", "research"},
}
LEVEL_RE = re.compile(r"level:\s*(core|proof|research)", re.I)

def read_level(path):
    try:
        with open(path) as f:
            m = LEVEL_RE.search(f.read())
        return m.group(1).lower() if m else "core"
    except Exception:
        return "core"

USE_COLOR = sys.stdout.isatty()
def _c(code, s):
    return s if not USE_COLOR else "\033[%sm%s\033[0m" % (code, s)
def green(s):  return _c("32", s)
def red(s):    return _c("31", s)
def yellow(s): return _c("33", s)
def bold(s):   return _c("1", s)
def dim(s):    return _c("2", s)

# ----- state -----
def load_state():
    try:
        with open(STATE_PATH) as f:
            return json.load(f)
    except Exception:
        return {"done": {}, "liveness": {}}
def save_state(st):
    try:
        with open(STATE_PATH, "w") as f:
            json.dump(st, f, indent=2)
    except Exception:
        pass

# ----- discovery -----
def lang_available(lang):
    return shutil.which(LANGS[lang]["probe"]) is not None

def iter_chapters():
    parts = []
    for d in os.listdir(ROOT):
        m = PART_RE.match(d)
        if m and os.path.isdir(os.path.join(ROOT, d)):
            parts.append((int(m.group(1)), d))
    parts.sort()
    for pnum, part in parts:
        pdir = os.path.join(ROOT, part)
        chs = []
        for d in os.listdir(pdir):
            m = CH_RE.search(d)
            if m and os.path.isdir(os.path.join(pdir, d)):
                chs.append((int(m.group(1)), d))
        chs.sort()
        for cnum, ch in chs:
            yield (pnum, cnum), part, ch, "P%d %s" % (pnum, ch)

def find_exercises(chpath, lang):
    conf = LANGS[lang]
    d = os.path.join(chpath, "exercises", conf["subdir"])
    if not os.path.isdir(d):
        return []
    ext = "." + conf["ext"]
    out = {}
    for fn in os.listdir(d):
        if not fn.endswith(ext):
            continue
        m = NUM_RE.search(fn)
        if not m:
            continue
        num = m.group(1)
        if "_buggy" + ext in fn:
            out.setdefault(num, {})["buggy"] = os.path.join(d, fn)
        elif fn.startswith("exercise"):
            out.setdefault(num, {})["main"] = os.path.join(d, fn)
    sold = os.path.join(d, "solutions")
    if os.path.isdir(sold):
        for fn in os.listdir(sold):
            if fn.endswith(ext):
                m = NUM_RE.search(fn)
                if m:
                    out.setdefault(m.group(1), {})["solution"] = os.path.join(sold, fn)
    res = []
    for num in sorted(out, key=lambda x: int(x)):
        rec = out[num]
        rec["num"] = num
        for k in ("main", "buggy", "solution"):
            rec.setdefault(k, None)
        res.append(rec)
    return res

# ----- running -----
def run_file(path, lang, timeout):
    cmd = LANGS[lang]["cmd"] + [path]
    try:
        p = subprocess.run(cmd, cwd=os.path.dirname(path),
                           capture_output=True, text=True, timeout=timeout)
        return p.returncode, (p.stdout or "") + (p.stderr or "")
    except subprocess.TimeoutExpired:
        return 124, "(timed out after %ss)" % timeout
    except FileNotFoundError:
        return 127, "(interpreter not found)"

def tail(out, n=16, cap=4000):
    out = out[-cap:]
    lines = out.strip("\n").splitlines()
    return "\n".join(lines[-n:])

def is_live(sol, lang, timeout, state):
    if not sol or not os.path.exists(sol):
        return False
    key = os.path.relpath(sol, ROOT)
    mt = os.path.getmtime(sol)
    cache = state.setdefault("liveness", {})
    rec = cache.get(key)
    if rec and abs(rec.get("mtime", -1) - mt) < 1e-6 and rec.get("lang") == lang:
        return rec["live"]
    rc, _ = run_file(sol, lang, timeout)
    live = (rc == 0)
    cache[key] = dict(mtime=mt, live=live, lang=lang)
    return live

def selected_langs(arg):
    want = {"both": ["python", "r"]}.get(arg, [arg] if arg else ["python"])
    avail = [l for l in want if lang_available(l)]
    missing = [l for l in want if l not in avail]
    if missing:
        print(dim("note: %s not available on this machine; skipping" %
                  ", ".join(missing)))
    return avail

def build_items(langs, tracks, timeout, state, level_set=None):
    items = []
    for _, part, ch, label in iter_chapters():
        chpath = os.path.join(ROOT, part, ch)
        for lang in langs:
            for ex in find_exercises(chpath, lang):
                live = is_live(ex["solution"], lang, timeout, state)
                for track in tracks:
                    edited = ex["buggy"] if track == "debug" else ex["main"]
                    if not edited or not os.path.exists(edited):
                        continue
                    lvl = read_level(edited)
                    if level_set is not None and lvl not in level_set:
                        continue
                    items.append(dict(
                        rel=os.path.relpath(edited, ROOT), path=edited,
                        kind=track, lang=lang, chapter=label,
                        num=ex["num"], live=live, level=lvl))
    return items

def first_pending(items, state):
    done = state.get("done", {})
    for it in items:
        if it["live"] and not done.get(it["rel"]):
            return it
    return None

# ----- hint -----
def show_hint(path):
    try:
        with open(path) as f:
            lines = f.readlines()
    except Exception:
        return
    hints = [ln.rstrip() for ln in lines
             if re.search(r"\b(BUG|TODO|HINT|FIXME)\b", ln)]
    if hints:
        print(yellow("hints from the file:"))
        for h in hints[:12]:
            print("   " + h.strip())

# ----- commands -----
def cmd_list(args, state):
    langs = selected_langs(args.lang)
    if not langs:
        print(red("no runnable language available")); return 1
    items = build_items(langs, _tracks(args.track), args.timeout, state, LEVEL_SETS[args.level])
    print(dim("  level filter: %s" % args.level))
    done = state.get("done", {})
    cur = {}
    for it in items:
        cur.setdefault(it["chapter"], []).append(it)
    ndone = nlive = npend = 0
    for chap, its in cur.items():
        marks = []
        for it in its:
            if not it["live"]:
                marks.append(dim("[~]")); npend += 1
            elif done.get(it["rel"]):
                marks.append(green("[x]")); ndone += 1; nlive += 1
            else:
                marks.append(yellow("[ ]")); nlive += 1
        tag = "%s%s" % (it["lang"][0], "")  # noqa
        print("  %-26s %s" % (chap, " ".join(marks)))
    print()
    print("  %s  %s  %s" % (
        green("[x] done=%d" % ndone),
        yellow("[ ] to do=%d" % (nlive - ndone)),
        dim("[~] not authored yet=%d" % npend)))
    print(dim("  legend: debug track fixes *_buggy files; build track fills TODO stubs"))
    return 0

def _run_and_report(it, timeout):
    print(bold("%s  %s  exercise %s  [%s/%s/%s]" %
               (it["chapter"], os.path.basename(it["path"]), it["num"],
                it["lang"], it["kind"], it.get("level", "core"))))
    print(dim("  file: " + it["rel"]))
    rc, out = run_file(it["path"], it["lang"], timeout)
    if rc == 0:
        print(green("  PASS"))
        return True
    print(red("  not yet -- first output below:"))
    t = tail(out)
    for ln in t.splitlines():
        print("    " + ln)
    return False

def cmd_next(args, state):
    langs = selected_langs(args.lang)
    if not langs:
        print(red("no runnable language available")); return 1
    items = build_items(langs, _tracks(args.track), args.timeout, state, LEVEL_SETS[args.level])
    it = first_pending(items, state)
    if it is None:
        done = sum(1 for i in items if state.get("done", {}).get(i["rel"]))
        pend = sum(1 for i in items if not i["live"])
        print(green("All ready exercises done! (%d cleared)" % done))
        if pend:
            print(dim("%d exercise(s) not authored yet -- nothing to drill there." % pend))
        return 0
    ok = _run_and_report(it, args.timeout)
    if args.hint and not ok:
        show_hint(it["path"])
    if ok:
        state.setdefault("done", {})[it["rel"]] = True
        save_state(state)
        nxt = first_pending(items, state)
        print(dim("  next: " + (nxt["rel"] if nxt else "none -- you're done")))
    return 0

def cmd_watch(args, state):
    langs = selected_langs(args.lang)
    if not langs:
        print(red("no runnable language available")); return 1
    tracks = _tracks(args.track)
    print(dim("watch mode -- edit the file, save, and it reruns. Ctrl-C to stop."))
    try:
        while True:
            items = build_items(langs, tracks, args.timeout, state, LEVEL_SETS[args.level])
            it = first_pending(items, state)
            if it is None:
                print(green("All ready exercises done!"))
                return 0
            print()
            ok = _run_and_report(it, args.timeout)
            if ok:
                state.setdefault("done", {})[it["rel"]] = True
                save_state(state)
                continue
            if args.hint:
                show_hint(it["path"])
            last = os.path.getmtime(it["path"])
            print(dim("  waiting for you to save %s ..." % os.path.basename(it["path"])))
            while True:
                time.sleep(0.5)
                try:
                    mt = os.path.getmtime(it["path"])
                except OSError:
                    continue
                if mt != last:
                    break
    except KeyboardInterrupt:
        print("\n" + dim("bye"))
        return 0

def cmd_verify(args, state):
    langs = selected_langs(args.lang)
    if not langs:
        print(red("no runnable language available")); return 1
    live = pending = 0
    violations = []
    for _, part, ch, label in iter_chapters():
        chpath = os.path.join(ROOT, part, ch)
        for lang in langs:
            for ex in find_exercises(chpath, lang):
                sol = ex["solution"]
                if not sol:
                    violations.append("%s [%s] ex%s: no solution file" %
                                      (label, lang, ex["num"]))
                    continue
                rc, _ = run_file(sol, lang, args.timeout)
                if rc != 0:
                    pending += 1
                    continue
                live += 1
                if ex["buggy"]:
                    brc, _ = run_file(ex["buggy"], lang, args.timeout)
                    if brc == 0:
                        violations.append("%s [%s] ex%s: buggy copy PASSES (no real bug)" %
                                          (label, lang, ex["num"]))
                if ex["main"]:
                    mrc, _ = run_file(ex["main"], lang, args.timeout)
                    if mrc == 0:
                        violations.append("%s [%s] ex%s: TODO version passes unedited" %
                                          (label, lang, ex["num"]))
    print(bold("verify: %d live exercise(s) checked, %d not authored yet" %
               (live, pending)))
    if violations:
        print(red("  %d integrity problem(s):" % len(violations)))
        for v in violations:
            print("    - " + v)
    else:
        print(green("  all live exercises pass their integrity checks"))
    bad = bool(violations) or (args.strict and pending)
    return 1 if bad else 0

def cmd_reset(args, state):
    state["done"] = {}
    save_state(state)
    print("progress reset.")
    return 0

def _tracks(arg):
    return {"both": ["debug", "build"]}.get(arg, [arg])

def main():
    global USE_COLOR
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("command", nargs="?", default="next",
                    choices=["next", "watch", "list", "verify", "reset"])
    ap.add_argument("--lang", default="python", choices=["python", "r", "both"])
    ap.add_argument("--track", default="debug", choices=["debug", "build", "both"])
    ap.add_argument("--level", default="all", choices=["bachelor", "master", "phd", "all"])
    ap.add_argument("--timeout", type=int, default=60)
    ap.add_argument("--hint", action="store_true")
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--no-color", action="store_true")
    args = ap.parse_args()
    if args.no_color:
        USE_COLOR = False
    state = load_state()
    fn = {"next": cmd_next, "watch": cmd_watch, "list": cmd_list,
          "verify": cmd_verify, "reset": cmd_reset}[args.command]
    rc = fn(args, state)
    save_state(state)
    sys.exit(rc or 0)

if __name__ == "__main__":
    main()
