from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"


class AssetCollector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.references = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        href = attributes.get("href")

        if href == "#":
            self.errors.append(f"placeholder href found on <{tag}>")

        for attribute in ("src", "href"):
            value = attributes.get(attribute)
            if not value:
                continue

            if value.startswith(("#", "http://", "https://", "mailto:", "tel:", "data:", "javascript:")):
                continue

            clean_value = unquote(value.split("?", 1)[0].split("#", 1)[0])
            if clean_value:
                self.references.append((tag, attribute, clean_value))


def local_path(reference):
    relative = reference.lstrip("/")
    if relative.startswith("./"):
        relative = relative[2:]
    return (ROOT / relative).resolve()


def main():
    parser = AssetCollector()
    parser.feed(INDEX.read_text(encoding="utf-8"))

    errors = list(parser.errors)
    root_resolved = ROOT.resolve()

    for tag, attribute, reference in parser.references:
        target = local_path(reference)
        try:
            target.relative_to(root_resolved)
        except ValueError:
            errors.append(f"{tag}[{attribute}] escapes repository root: {reference}")
            continue

        if not target.exists():
            errors.append(f"missing local asset referenced by {tag}[{attribute}]: {reference}")

    if errors:
        print("Static checks failed:")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    print(f"Static checks passed: {len(parser.references)} local references verified.")


if __name__ == "__main__":
    main()
