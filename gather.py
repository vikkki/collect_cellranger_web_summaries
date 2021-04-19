import os,shutil
cfolder = os.getcwd()
print("Current working dir is " + cfolder)

def get_count_result_folder_list(cfolder):
    folders_list = next(os.walk(cfolder, followlinks = False))[1]
    result_folder_list = []
    for folder in folders_list:
        if os.path.isfile(cfolder + "/" + folder + "/outs/web_summary.html"):
            result_folder_list.append(folder)
    return result_folder_list

def gether_summaries(cfolder):
    if not os.path.exists(cfolder + "/cellranger_web_summaries"):
        print("Creating folder...")
        os.makedirs(cfolder + "/cellranger_web_summaries")
        print("Done.")
    else:
        print("Summary folder exists, Ready.")
    flist = get_count_result_folder_list(cfolder)
    for folder in flist:
        shutil.copyfile(cfolder + "/" + folder + "/outs/web_summary.html", cfolder + "/cellranger_web_summaries/" + folder + "_web_summary.html")
        print(folder + " Coppied.")

gether_summaries(cfolder)
