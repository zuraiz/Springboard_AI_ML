import os
import pandas as pd


def get_list_of_files(dir_name):
    # create a list of files and sub directories
    # names in the given directory
    list_of_file = os.listdir(dir_name)
    all_files = list()
    list_of_file.sort()
    # iterate over all the entries
    for entry in list_of_file:
        # create full path
        full_path = os.path.join(dir_name, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(full_path):
            all_files = all_files + get_list_of_files(full_path)
        else:
            if full_path.endswith(".txt"):
                all_files.append(full_path)
    return all_files


def produce_one_file(list_of_files):
    dflist = [pd.read_csv(f, header=None) for f in list_of_files]
    concatdf = pd.concat(dflist, axis=0)
    return concatdf


def get_image(dir_name):
    file_list = get_list_of_files(dir_name)
    concatdf = produce_one_file(file_list)
    concatdf.columns = ['FrameNum', 'x', 'y', 'w', 'h', 'Timestamp', 'hr', 'min', 'sec']
    for col in concatdf.columns:
        concatdf[col] = concatdf[col].map(lambda x: x.split('=')[1])

    hist = concatdf['min'].hist()
    figure = hist.get_figure()
    file_name = 'hist.png'
    figure.savefig('static/people_photo/hist.png', dpi=200)

    # df_cm = pd.DataFrame(array)
    # svm = sn.heatmap(df_cm, annot=True, cmap='coolwarm', linecolor='white', linewidths=1)
    # figure = svm.get_figure()
    # figure.savefig('static/people_photo/svm_conf.png', dpi=400)
    return file_name
