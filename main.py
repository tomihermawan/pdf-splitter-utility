import os
from pypdf import PdfReader, PdfWriter


def split_pdf_by_pages(input_pdf_path, output_dir="output_pdfs"):
  """Memecah setiap halaman dari file PDF menjadi file-file PDF terpisah."""
  if not os.path.exists(input_pdf_path):
    print(f"Error: File '{input_pdf_path}' tidak ditemukan.")
    return

  # Membuat folder output jika belum ada
  os.makedirs(output_dir, exist_ok=True)

  reader = PdfReader(input_pdf_path)
  total_pages = len(reader.pages)

  print(
      f"Memproses file '{input_pdf_path}' dengan total {total_pages}"
      " halaman..."
  )

  for index, page in enumerate(reader.pages):
    writer = PdfWriter()
    writer.add_page(page)

    output_filename = os.path.join(
        output_dir, f"page_{index + 1}_extracted.pdf"
    )

    with open(output_filename, "wb") as output_file:
      writer.write(output_file)

    print(f"Berhasil menyimpan: {output_filename}")

  print(
      f"Selesai! Semua halaman berhasil dipisah di dalam folder '{output_dir}'."
  )


def extract_page_range(input_pdf_path, start_page, end_page, output_filename):
  """Mengekstrak rentang halaman tertentu dari PDF menjadi satu file PDF baru."""
  if not os.path.exists(input_pdf_path):
    print(f"Error: File '{input_pdf_path}' tidak ditemukan.")
    return

  reader = PdfReader(input_pdf_path)
  total_pages = len(reader.pages)

  # Validasi rentang halaman
  if start_page < 1 or end_page > total_pages or start_page > end_page:
    print(f"Error: Rentang halaman tidak valid (Total halaman: {total_pages}).")
    return

  writer = PdfWriter()

  # pypdf menggunakan indeks berbasis 0 (0-indexed)
  for page_num in range(start_page - 1, end_page):
    writer.add_page(reader.pages[page_num])

  with open(output_filename, "wb") as output_file:
    writer.write(output_file)

  print(
      f"Berhasil mengekstrak halaman {start_page}-{end_page} ke"
      f" '{output_filename}'."
  )


if __name__ == "__main__":
  # Contoh Penggunaan:
  # Ganti 'sample.pdf' dengan nama file PDF Anda yang sebenarnya
  target_pdf = "sample.pdf"

  print("=== PILIHAN MENU PDF SPLITTER ===")
  print("1. Pisah setiap halaman menjadi file terpisah")
  print("2. Ekstrak rentang halaman tertentu")

  choice = input("Pilih menu (1/2): ")

  if choice == "1":
    split_pdf_by_pages(target_pdf)
  elif choice == "2":
    start = int(input("Masukkan halaman awal: "))
    end = int(input("Masukkan halaman akhir: "))
    out_name = input("Nama file output (contoh: hasil.pdf): ")
    extract_page_range(target_pdf, start, end, out_name)
  else:
    print("Pilihan tidak valid.")
    
