# remove_null_bytes.py

input_file = 'models.py'
output_file = 'models_clean.py'

with open(input_file, 'rb') as f:
    content = f.read()

if b'\x00' in content:
    print("Null bytes found! Cleaning...")

clean_content = content.replace(b'\x00', b'')

with open(output_file, 'wb') as f:
    f.write(clean_content)

print(f"Cleaned file saved to {output_file}")
