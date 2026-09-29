def swap_file_content(file1_path, file2_path):
    with open(file1_path, "rb") as f1, open(file2_path, "rb") as f2:
        data1 = f1.read()
        data2 = f2.read()

    with open(file1_path, "wb") as f1, open(file2_path, "wb") as f2:
        f1.write(data2)
        f2.write(data1)


swap_file_content('binary_file_1.jpg', 'binary_file_2.jpg')
