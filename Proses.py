import csv

def csv_to_txt(csv_file, txt_file, format_type=1):
    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        with open(txt_file, mode='w', encoding='utf-8') as output:
            for row in reader:
                if format_type == 1:
                    # Format 1: Structured Text with Key-Value Pairs
                    output.write(f"Player: {row['Players']}\n")
                    output.write(f"Team: {row['Teams']}\n")
                    output.write(f"Season: {row['Seasons']}\n")
                    output.write(f"Goals: {row['Goals']}\n")
                    output.write(f"Assists: {row['Assists']}\n")
                    output.write("---\n")
                elif format_type == 2:
                    # Format 2: Concise Structured Text
                    output.write(f"[{row['Players']}] | [{row['Teams']}] | [{row['Seasons']}] | Goals: {row['Goals']} | Assists: {row['Assists']}\n")

# Contoh penggunaan
csv_file = 'dataset\Data pemain bola.csv'  # Ganti dengan nama file CSV Anda
txt_file = 'dataset\Data2.txt'  # Nama file TXT yang akan dihasilkan
csv_to_txt(csv_file, txt_file, format_type=2)  # Ganti format_type ke 2 untuk menggunakan Format 2
