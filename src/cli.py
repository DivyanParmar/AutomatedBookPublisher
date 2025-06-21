import os
from src.scraper import fetch_chapter
from src.ai_agents import ai_spin, ai_review
from src.versioning import save_version

def pause_for_edit(stage: str):
    print(f"✏️ Edit 'output/{stage}.txt'. Press Enter when done.")
    input()

def run(chapter_id: str, url: str):
    os.makedirs("output", exist_ok=True)

    # Step 1: Scrape
    original = fetch_chapter(url)
    with open("output/original.txt", "w", encoding="utf-8") as f:
        f.write(original)
    save_version(chapter_id, "original", original)

    # Step 2: Spin
    spun = ai_spin(original)
    with open("output/spun.txt", "w", encoding="utf-8") as f:
        f.write(spun)
    save_version(chapter_id, "spun", spun)
    pause_for_edit("spun")

    # Step 3: Human Edit (Spun)
    with open("output/spun.txt", "r", encoding="utf-8") as f:
        spun_human = f.read()
    save_version(chapter_id, "spun_human", spun_human)

    # Step 4: Review
    reviewed = ai_review(spun_human)
    with open("output/reviewed.txt", "w", encoding="utf-8") as f:
        f.write(reviewed)
    save_version(chapter_id, "reviewed", reviewed)
    pause_for_edit("reviewed")

    # Step 5: Final
    with open("output/reviewed.txt", "r", encoding="utf-8") as f:
        final = f.read()
    with open("output/final.txt", "w", encoding="utf-8") as f:
        f.write(final)
    save_version(chapter_id, "final", final)
    print("✅ Final version saved in output/final.txt")

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("chapter_id")
    parser.add_argument("url")
    args = parser.parse_args()
    run(args.chapter_id, args.url)

if __name__ == "__main__":
    main()
