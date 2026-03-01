# github codespaces masscan+ingram autorunner
# by @notos0

# python q.py ranges.txt
import subprocess, math, sys, os, re, signal, random
words = ["banana","mango","grape","peach","lemon","apple","cherry","melon","plum","kiwi","olive","cedar","maple","hazel","coral","amber","ivory","jade","ruby","opal"]
def rw():
    return random.choice(words)+str(random.randint(1,999))
def split(f, n):
    lines = [l.strip() for l in open(f) if l.strip()]
    size = math.ceil(len(lines)/n)
    chunks = []
    for i in range(n):
        name = f"chunk_{i}.txt"
        open(name,"w").write("\n".join(lines[i*size:(i+1)*size])+"\n")
        chunks.append(name)
    return chunks
def main():
    inp = sys.argv[1]
    n = 4
    scanword = rw()
    chunks = split(inp, n)
    procs = []
    outs = []

    for i,chunk in enumerate(chunks):
        out = f"{scanword}_{i}.txt"
        outs.append(out)
        cmd = f"sudo masscan -iL {chunk} -p 8080,8000,37777 -oG {out} --rate 70000"
        print(f"[*] chunk {i} -> {out}")
        procs.append(subprocess.Popen(cmd, shell=True))

    try:
        for p in procs:
            p.wait()
    except KeyboardInterrupt:
        for p in procs:
            p.send_signal(signal.SIGTERM)
        for p in procs:
            p.wait()
        print("\n[!] interrupted")

    ips = set()
    for out in outs:
        if os.path.exists(out):
            for l in open(out):
                m = re.search(r"(\d+\.\d+\.\d+\.\d+)", l)
                if m:
                    ips.add(m.group(1))

    for chunk in chunks:
        if os.path.exists(chunk):
            os.remove(chunk)
    for out in outs:
        if os.path.exists(out):
            os.remove(out)
    final = scanword+".txt"
    open(final,"w").write("\n".join(sorted(ips))+"\n")
    print(f"[+] {len(ips)} ips -> {final}")
    outword = rw()
    os.system(f"cd Ingram-master && python run_with_mods.py -i ../{final} -o {outword} -t 2000")
if __name__=="__main__":
    main()