import tkinter as tk
from tkinter import filedialog, messagebox
import zipfile
import os

class FileCompressorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Compressor")

        # Input File Label and Entry
        self.input_label = tk.Label(root, text="Select File to Compress:")
        self.input_label.pack(pady=(20, 5))
        self.input_entry = tk.Entry(root, width=50)
        self.input_entry.pack(pady=5)
        self.input_button = tk.Button(root, text="Browse", command=self.browse_input_file)
        self.input_button.pack(pady=5)

        # Output Zip Label and Entry
        self.output_label = tk.Label(root, text="Save Compressed File As:")
        self.output_label.pack(pady=(20, 5))
        self.output_entry = tk.Entry(root, width=50)
        self.output_entry.pack(pady=5)
        self.output_button = tk.Button(root, text="Browse", command=self.browse_output_path)
        self.output_button.pack(pady=5)

        # Compress Button
        self.compress_button = tk.Button(root, text="Compress", command=self.compress_file)
        self.compress_button.pack(pady=20)

    def browse_input_file(self):
        input_file_path = filedialog.askopenfilename(filetypes=[("All Files", "*.*")])
        if input_file_path:
            self.input_entry.delete(0, tk.END)
            self.input_entry.insert(0, input_file_path)

    def browse_output_path(self):
        output_file_path = filedialog.asksaveasfilename(defaultextension=".zip", filetypes=[("ZIP Files", "*.zip")])
        if output_file_path:
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, output_file_path)

    def compress_file(self):
        input_file_path = self.input_entry.get().strip()
        output_zip_path = self.output_entry.get().strip()

        if not input_file_path:
            messagebox.showerror("Error", "Please select a file to compress.")
            return

        if not output_zip_path:
            messagebox.showerror("Error", "Please specify the output ZIP file path.")
            return

        try:
            # Extract the filename from the full path
            file_name = os.path.basename(input_file_path)

            # Open input file in read binary mode
            with open(input_file_path, 'rb') as input_file:
                # Create a ZipFile object in write mode
                with zipfile.ZipFile(output_zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                    # Add the input file to the ZIP archive with its filename
                    zip_file.write(input_file_path, arcname=file_name)

            messagebox.showinfo("Success", f"File '{file_name}' compressed successfully to '{output_zip_path}'")

        except FileNotFoundError:
            messagebox.showerror("Error", f"Input file '{input_file_path}' not found.")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

def main():
    root = tk.Tk()
    app = FileCompressorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
