"""Keep the Claude Code copy of the repo's skills identical to the Codex copy.

Codex loads skills from .agents/skills/ and Claude Code from .claude/skills/.
Neither reads the other's folder, and symlinks are unreliable in Windows
checkouts, so both folders hold real files. .agents/skills/ is the source.

    python scripts/sync_skills.py          copy .agents/skills/ over .claude/skills/
    python scripts/sync_skills.py --check  exit 1 if the copies differ or a skill is invalid

Standard library only.
"""
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / ".agents" / "skills"
TARGET = ROOT / ".claude" / "skills"
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)


def files(base):
    return {p.relative_to(base).as_posix(): p.read_bytes()
            for p in sorted(base.rglob("*")) if p.is_file()}


def validate(source_files):
    errors = []
    skills = {path.split("/")[0] for path in source_files}
    for skill in sorted(skills):
        body = source_files.get(skill + "/SKILL.md")
        if body is None:
            errors.append(skill + ": missing SKILL.md")
            continue
        text = body.decode("utf-8")
        match = FRONTMATTER.match(text)
        if not match:
            errors.append(skill + ": SKILL.md must start with --- frontmatter (LF endings)")
            continue
        fields = dict(line.split(": ", 1) for line in match.group(1).splitlines()
                      if ": " in line and not line.startswith(" "))
        if fields.get("name") != skill:
            errors.append(skill + ": frontmatter name must equal the folder name")
        if not fields.get("description"):
            errors.append(skill + ": frontmatter needs a description")
        manual_claude = fields.get("disable-model-invocation") == "true"
        yaml = source_files.get(skill + "/agents/openai.yaml", b"").decode("utf-8")
        manual_codex = "allow_implicit_invocation: false" in yaml
        if manual_claude != manual_codex:
            errors.append(skill + ": disable-model-invocation and agents/openai.yaml "
                          "allow_implicit_invocation must agree so Claude and Codex match")
    return errors


def main():
    check = "--check" in sys.argv[1:]
    source_files = files(SOURCE)
    errors = validate(source_files)
    if check:
        target_files = files(TARGET) if TARGET.exists() else {}
        for path in sorted(set(source_files) | set(target_files)):
            if source_files.get(path) != target_files.get(path):
                errors.append(".claude/skills/" + path + " differs from .agents/skills/; "
                              "run python scripts/sync_skills.py")
    if errors:
        print("\n".join(errors))
        return 1
    if not check:
        if TARGET.exists():
            shutil.rmtree(TARGET)
        shutil.copytree(SOURCE, TARGET)
        print("copied %d files to %s" % (len(source_files), TARGET.relative_to(ROOT)))
    else:
        print("skills OK: %d skills, Claude and Codex copies identical"
              % len({p.split("/")[0] for p in source_files}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
