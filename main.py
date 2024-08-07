import matplotlib.pyplot as plt
import networkx as nx
import tkinter as tk
import os


def convert_to_txt(file_name):
    txt = open(f"{file_name}", "w")
    text_list = []
    for line in text_list:
        txt.write(line)
    return "\n".join(text_list)

if __name__ == '__main__':
    foldername = "\\Users\\mrtur\\PycharmProjects\\WriteAlign1.0\\main"
    files_in_folder = os.listdir(foldername)
    print(files_in_folder)
    new_file = open("newtestfile.txt", "w")
    for file in files_in_folder:
        handle = open(f"C:\\Users\\mrtur\\PycharmProjects\\WriteAlign1.0\\main\\{file}", "r")
        for line in handle:
            new_file.write(line)
        handle.close()
    new_file.close()

