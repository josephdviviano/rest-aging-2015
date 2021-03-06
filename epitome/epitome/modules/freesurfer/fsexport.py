#!/usr/bin/env python

# Freesurfer T1 Export
# takes the processed T1 from freesurfer to use as a standard anatomical
# this is slow, but provides the highest-quality registration target.
# this also allows us to take advantage of the high-quality freesurfer
# segmentations for nuisance time series regression, if desired

import os, sys
import fnmatch
import subprocess
import shlex

import epitome as epi

def bash_command(cmd):
    # pipe = subprocess.Popen(shlex.split(cmd), 
    #                               stdout=subprocess.PIPE,
    #                               stderr=subprocess.PIPE,
    #                               shell=True,
    #                               executable='/bin/bash')
    # out, err = pipe.communicate()
    # result = out.decode()
    # print('Result: ', result)
    os.system("""/bin/bash -c '""" + cmd + """'""")

def run_commands(path, directory, expt, subj, session):
    
    subjID = str(expt) + '_' + str(subj) + '_' + str(session)
    dir_i = os.path.join(path, 'FREESURFER/SUBJECTS', subjID, 'mri')
    dir_o = os.path.join(directory, session)

    # convert freesurfer T1 to NII
    if os.path.isfile(dir_o + '/anat_T1_fs.nii.gz') == False:
        cmd = ('mri_convert ' +
               '--in_type mgz ' +
               '--out_type nii ' +
               '-odt float ' +
               '-rt nearest ' + 
               '--input_volume ' + dir_i + '/brain.mgz ' + 
               '--output_volume ' + dir_o + '/anat_T1_fs.nii.gz')
        print cmd
        bash_command(cmd)

    # orient to RAI orientation
    if os.path.isfile(dir_o + '/anat_T1_brain.nii.gz') == False:
        cmd = ('3daxialize ' +
               '-prefix ' + dir_o + '/anat_T1_brain.nii.gz ' +
               '-axial '  + dir_o + '/anat_T1_fs.nii.gz')
        bash_command(cmd)
    
    # convert MGZ APARC atlas to NII
    if os.path.isfile(dir_o + '/anat_aparc_fs.nii.gz') == False:
        cmd = ('mri_convert ' + 
               '--in_type mgz ' +
               '--out_type nii ' +
               '-odt float ' +
               '-rt nearest ' + 
               '--input_volume ' + dir_i + '/aparc+aseg.mgz ' +
               '--output_volume ' + dir_o + '/anat_aparc_fs.nii.gz')
        bash_command(cmd)
    
    # orient to RAI orientation
    if os.path.isfile(dir_o + '/anat_aparc_brain.nii.gz') == False:
        cmd = ('3daxialize ' +
               '-prefix ' + dir_o + '/anat_aparc_brain.nii.gz ' +
               '-axial '  + dir_o + '/anat_aparc_fs.nii.gz')
        bash_command(cmd)

    # convert MGZ APARC2009 atlas to NII
    if os.path.isfile(dir_o + '/anat_aparc2009_fs.nii.gz') == False:
        cmd = ('mri_convert ' +
               '--in_type mgz ' +
               '--out_type nii ' +
               '-odt float ' +
               '-rt nearest ' + 
               '--input_volume ' + dir_i + '/aparc.a2009s+aseg.mgz ' + 
               '--output_volume ' + dir_o + '/anat_aparc2009_fs.nii.gz')
        bash_command(cmd)

    # orient to RAI orientation
    if os.path.isfile(dir_o + '/anat_aparc2009_brain.nii.gz') == False:
        cmd = ('3daxialize ' +
               '-prefix ' + dir_o + '/anat_aparc2009_brain.nii.gz ' + 
               '-axial '  + dir_o + '/anat_aparc2009_fs.nii.gz')
        bash_command(cmd)

def T1_export(path, expt):
    
    # get subject numbers
    subjects = epi.utilities.get_subj(os.path.join(path, expt))
 
    # get directory of sessions
    for subj in subjects:
        directory = os.path.join(path, expt, subj, 'T1')
        
        # get all sessions
        for session in os.listdir(directory):
            if os.path.isdir(os.path.join(directory, session)) == True:
                #export all FREESURFER data per session
                run_commands(path, directory, expt, subj, session)

if __name__ == "__main__":
    T1_export(sys.argv[1], sys.argv[2])
