import pickle

FILENAME = 'ClubInfo.dat'


# LOAD & SAVE

def load_info(FILENAME):
    try:
        infile = open(FILENAME, 'rb')
        club_dic = pickle.load(infile)
        infile.close()

    except FileNotFoundError:
        club_dic = {}

    return club_dic


def save_info(FILENAME, club_dic):
    outfile = open(FILENAME, 'wb')
    pickle.dump(club_dic, outfile)
    outfile.close()


