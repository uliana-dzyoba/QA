from filesystem import FileSystem


def main():
    fs = FileSystem()
    fs.create_directory("root\\notes")
    fs.create_directory("root\\notes\\lectures")
    fs.create_text_file("root\\notes\\writing_prompt.txt")
    fs.write_text_file("root\\notes\\writing_prompt.txt", "Magic is abundant, everywhere, and used as currency.")
    fs.write_text_file("root\\notes\\writing_prompt.txt", "Main character…lacks any magical powers—or maybe just the obvious ones.")
    fs.create_text_file("root\\notes\\lectures\\law.txt")
    fs.write_text_file("root\\notes\\lectures\\law.txt", "Tort of battery has a wide definition.")
    fs.create_directory("root\\tech")
    fs.create_directory("root\\tech\\execs")
    fs.create_directory("root\\tech\\office")
    fs.create_binary_file("root\\tech\\execs\\program.exe")
    fs.create_binary_file("root\\tech\\execs\\library.bin")
    fs.create_buffer_file("root\\tech\\office\\printer_queue.bfr")
    fs.push_buffer_file("root\\tech\\office\\printer_queue.bfr", "image12.jpg")
    fs.push_buffer_file("root\\tech\\office\\printer_queue.bfr", "report.doc")




if __name__ == '__main__':
    main()


