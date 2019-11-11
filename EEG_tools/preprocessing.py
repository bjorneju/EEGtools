

# importing required packages
import mne


# Functions

### IO functions

def load_data(path,filename):

    '''
        Description:

        Inputs:

        Outputs: 
    '''

    fullpath= path + "/" + filename
    print(fullpath)
    temp = []

    #try:
    if '.fif' in fullpath:
        temp = mne.io.read_raw_fif(fullpath,preload=True)
    elif '.vhdr' in fullpath:
        temp = mne.io.read_raw_brainvision(fullpath,preload=True)
    elif '.cnt' in fullpath:
        temp = mne.io.read_raw_cnt(fullpath,preload=True)
    elif '.edf' in fullpath:
        temp = mne.io.read_raw_edf(fullpath,preload=True)
    elif '.bdf' in fullpath:
        temp = mne.io.read_raw_edf(fullpath,preload=True)
    elif '.gdf' in fullpath:
        temp = mne.io.read_raw_edf(fullpath,preload=True)
    elif '.egi' in fullpath:
        temp = mne.io.read_raw_egi(fullpath,preload=True)
    elif '.mff' in fullpath:
        temp = mne.io.read_raw_egi(fullpath,preload=True)
    elif '.set' in fullpath:
        temp = mne.io.read_raw_eeglab(fullpath,preload=True)
    elif '.nxe' in fullpath:
        temp = mne.io.read_raw_eximia(fullpath,preload=True)
    elif '.fif' in fullpath:
        temp = mne.io.read_raw_brainvision()
    elif '.fif' in fullpath:
        temp = mne.io.read_raw_brainvision()
    else:
        try:
            temp = mne.io.read_raw_bti(fullpath,preload=True)
        except:
            try:
                temp = mne.io.read_raw_ctf(fullpath,preload=True)
            except:
                try:
                    temp = mne.io.read_raw_kit(fullpath,preload=True)
                except:
                    print("Doesn't seem like the data file you provided worked!!")
                    print(fullpath)

    return temp.load_data()
