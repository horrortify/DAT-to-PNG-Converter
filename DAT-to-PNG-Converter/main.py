import os
from datetime import datetime

def extract_png(data):
    png_header = b'\x89PNG\r\n\x1a\n'
    png_footer = b'IEND\xaeB`\x82'

    start = data.find(png_header)
    if start == -1:
        return None

    end = data.find(png_footer, start)
    if end == -1:
        end = start + 300000
    else:
        end += len(png_footer)

    return data[start:end]


def process_folder(folder_path):
    files = [f for f in os.listdir(folder_path) if f.lower().endswith(".dat")]

    if not files:
        print("No .dat files found.")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    count = 0

    for file in files:
        full_path = os.path.join(folder_path, file)

        with open(full_path, "rb") as f:
            data = f.read()

        png_data = extract_png(data)

        if png_data is None:
            print(f"Skipped (no PNG): {file}")
            continue

        output_file = f"avatar_{timestamp}_{count}.png"

        with open(output_file, "wb") as out:
            out.write(png_data)

        print(f"Saved: {output_file}")
        count += 1

    print(f"Done. Converted {count} file(s).")


def main():
    print("DAT Batch to PNG Converter")

    folder = input("Enter folder path: ").strip()

    if not os.path.exists(folder):
        print("Folder does not exist.")
        return

    process_folder(folder)


if __name__ == "__main__":
    main()