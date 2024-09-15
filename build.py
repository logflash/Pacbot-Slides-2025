import os
from pathlib import Path
from pypdf import PdfReader, PdfWriter

# Get the current script directory
script_dir = Path(__file__).parent

# Get a list of child directories and print them
child_dirs = [
    p.name for p in script_dir.joinpath('design').iterdir()
    if p.is_dir() and not p.name.startswith('.')
]

# Build each child directory
for child_dir in child_dirs:

    child_dir = Path('design') / child_dir
    print(f'Child directory: {child_dir}')

    # Create a PDF Writer
    writer = PdfWriter()

    # Loop through all files in the directory
    for root, _, files in os.walk(child_dir):
        for filename in sorted(files):
            if filename.endswith('.pdf'):
                filepath = os.path.join(root, filename)

                # Add the pages from each PDF file
                print(f'Adding: {filepath}')
                reader = PdfReader(filepath)
                for page_num in range(len(reader.pages)):
                    writer.add_page(reader.pages[page_num])

    # Specify the output file name
    output_file_name = 'pacbot_sw_' + Path(child_dir).name + '.pdf'
    output_file = script_dir / "out" / output_file_name
    Path(output_file).parent.mkdir(parents=True, exist_ok=True)

    # Write the merged PDF to the output file
    if len(writer.pages):
        with open(output_file, 'wb') as f_out:
            writer.write(f_out)
            print(f'Merged PDF saved as {output_file}')
    else:
        print('Skipped, no PDF files found')

    # Close the PDF Writer
    writer.close()

    # New line for spacing
    print()
