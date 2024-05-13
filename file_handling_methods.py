# Description: 
#   A module containing functions for the retrieval of files from external 
#   sources. The functions defined in this module may be extended and updated
#   over time.
# Author:
#   Sanne Vreugdenhil
# Date of creation:
#   27-03-2024


# URL ==========================================================================
def download_from_url_a(url, filename):
    """
    Description
        ----
        This function uses the urllib.request module that is included in Python 
        (version 3.10.9) to download a file from a given URL link. The file is 
        downloaded into the current working directory if only a filename is 
        provided, or into a specified exisiting directory (absolute or relative 
        filepath). 
        This function was tested in a Jupyter notebook.
        ----
    Parameters
        ----
        url
            >> the url link from which to download the file
        filename
            >> the name the file is to be called in the current working 
            directory
            >> OR a filepath (absolute or relative) of an existing folder 
    Returns
        ----
        urllib.request.urlretrieve returns a tuple of the filename and some 
        information.
        out
            >> the filename
        response
            >> the information
        Prints the message that the file was downloaded succesfully and the 
        information and downloads the file in the current working directory (
        if only the filename was specified) or the directory that was 
        specified.
        ----
    Versioning
        ----
        Python: 3.10.9
        urllib included in Python version
        ----
    """
    import urllib.request
    # store tuple outcome of urlretrieve into 2 variables:
    out, response = urllib.request.urlretrieve(url, filename) 
    print(f"Successfully downloaded {out}\n")
    print(response)
 
def download_from_url_b(url, filename):
    """
    IMPORTANT NOTE: 
    download requests module into your environment before using this function
    Description
        ----
        This function uses the requests module to download a file from a given 
        URL link. The file is downloaded into the current working directory if 
        only a filename is provided, or into a specified existing directory
        (absolute or relative filepath). 
        This function was tested in a Jupyter notebook.
        ----
    Parameters
        ----
        url
            >> the url link from which to download the file
        filename
            >> the name the file is to be called in the current working 
            directory
            >> OR a filepath (absolute or relative) of an existing folder
        ----
    Returns
        ----
        Prints a statement that the file was succesfully created and downloads
        the file to the current working directory (if only filename specified)
        or the directory that was specified.
        ----
    Versioning
        ----
        Python: 3.10.9
        requests: 2.31.0
        ----
    """
    import requests 
    r = requests.get(url) # access url
    # write content of the opened file into a new file:
    with open(filename, "wb") as f:
        f.write(r.content)
    print(f"The file {filename} was succesfully created.")
# ==============================================================================


# FTP ==========================================================================
def check_ftp_content(
    server, username="anonymous", password="anonymous", dir=""
    ):
    """
    Description
        ----
        This function uses the ftplib module that is included in Python (
        version 3.10.9) to view the contents of a specified FTP server.
        When accessing a public server, username and password are usually both 
        "anonymous". When a username and password are not provided, this 
        function automatically uses "anonymous" as both username and password. 
        The function makes use of an encrypted connection in order to be able 
        to access public servers. 
        If no directory is specified, the contents of the home directory of the
        FTP server are listed, else the contents of the specified directory are
        listed.
        NOTE 28-03-2024: this function has NOT been tested with a non-public
        FTP server yet!
        ----
    Parameters
        ----
        server
            >> the address of the FTP server you are reaching
        username (optional)
            >> username for the FTP server, if not provided = "anonymous"
        password (optional)
            >> password for the FTP server, if not provided = "anonymous"
        dir (optional)
            >> the name or path of the directory within the FTP server
        ----
    Returns
        ----
        If no directory is specified, the function returns the listed contents 
        of the home directory of the FTP server, else it lists the contents of
        the specified directory within the FTP server
        ----
    Versioning
        ----
        Python: 3.10.9
        ftplib included in Python version
    """
    import ftplib
    ftp = ftplib.FTP_TLS(server)
    ftp.login() 
    ftp.prot_p() 
    if dir != "":
        ftp.cwd(dir)
        ftp.retrlines('LIST')
    else:
        ftp.retrlines('LIST')
    ftp.quit()

def file_from_ftp(
    server, dir, filename, username="anonymous", password="anonymous"
    ):
    """
    Description
        ----
        This function uses the ftplib module that is included in Python (
        version 3.10.9) to download a specific file from a FTP server. The file
        is always downloaded to the current working directory, it is not 
        possible to specify a directory. Use os.rename() to move the file
        to the desired directory.
        When dowloading files from a public server, username and password are
        usually both "anonymous". When a username and password are not provided,
        this function automatically uses "anonymous" as both username and
        password. The function makes use of an encrypted connection in order
        to be able to download from public servers.
        NOTE 28-03-2024: this function has NOT been tested with a non-public
        FTP server yet!
        ----
    Parameters
        ----
        server
            >> the address of the FTP server you are reaching
        dir
            >> the name of the directory in which the file(s) you are 
            downloading is located (can ba a path)
        filename
            >> the name of the file that you are downloading
        username
            >> username for the FTP server, if not provided = "anonymous"
        password
            >> password for the FTP server, if not provided = "anonymous"
        ----
    Returns
        ----
        Prints a statement that the file was succesfully downloaded and 
        downloads the file to the current working directory.
        ----
    Versioning
        ----
        Python: 3.10.9
        ftplib included in Python version
        ----
    """
    import ftplib 
    ftp = ftplib.FTP_TLS(server) # access server through encrypted session
    ftp.login(username, password) # login on server
    ftp.prot_p() # explicitely call for protected transfer
    ftp.cwd(dir) # go to the directory of the file
    # Download the file 
    with open(filename, "wb") as out:
        ftp.retrbinary(f"RETR {filename}", out.write)
    ftp.quit() # quit the ftp server
    print(f"The file {filename} was succesfully downloaded.")
# ==============================================================================


# ZIP ==========================================================================
def extract_zip(file):
    """
    Description
        ----
        This function uses the zipfile module that is included in Python (
        version 3.10.9) to extact files from a zip. This function extracts
        the files from the zip and places them into the current working 
        directory. This function then uses the the build-in os module to 
        create a new directory and move the files into that new directory.
        The only thing that it needs to work is the path to the zipfile.
        ----
    Parameters
        ----
        file
            >> the path to the zipfile
        ----
    Returns
        ----
        Creates a folder into the current working directory with the files 
        from the zip.
        ----
    Versioning
        ----
        Python: 3.10.9
        zipfile included in Python version
        os included in Python version
        ----
    """
    import zipfile # import module for opening zip files
    import os      # import os to create a new directory to append zipfiles to
    
    zip = open(file, "rb")          # open the zipfile 
    zipShape = zipfile.ZipFile(zip) # read the zipfile
    
    files = [] # create a list to append files from inside the zip to
    
    for filename in zipShape.namelist(): # obtain filenames and name files
        filename = f"{filename}"             # get actual filename
        out = open(filename, "wb")  
        out.write(zipShape.read(filename))
        out.close()
        files.append(filename)               # append filenames to the list
    
    folder_name = filename.split(".")[0] # create a directory name
    os.mkdir(folder_name)                # create a new directory
    for file in files:
        os.rename(f"{file}", f"{folder_name}/{file}") # move files to dir
# ==============================================================================


# TAR ==========================================================================
def files_to_tar_gz(files, tar_name, dir_path=""):
    """Description
        ----
        This function uses the tarfile module that is included in Python (
        version 3.10.9) to create a tar archive with given files. To do so
        it uses the w:gz mode for gzipped compression. The names of the files
        need to be provided in a list, and the to be name of the archive must
        be provided as well. If files in the current working directory need to 
        be archived and compressed, a dir_path should not be provided. If files
        in another directory need to be archived, you do need to provide a path.
        An alternative for providing a dir_path, is providing the filenames as 
        a path. (e.g. ["hancock/hancock.dbf", "hancock/hancock.shp", 
        "hancock/hancock/shx"], note that this way is not officially tested but 
        should work nonetheless). 
        Please note that the new compressed archive file is always created in 
        the current working directory. 
        ----
    Parameters
        ----
        files
            >> a list of file names (or paths) that need to be archived and 
            compressed
        tar_name
            >> the name of the new tar.gz file, provide the name without the 
            file extension!
        dir_path
            >> the name(s) of the directory(s) that lead to the files to be 
            archived are located
        ----
    Returns
        ----
        Creates a gzipped tar archive in the currnt working directory.
        ----
    Versioning
        ----
        Python: 3.10.9
        tarfile included in Python version
        ----
    
    """
    import tarfile
    tar = tarfile.open(f"{tar_name}.tar.gz", "w:gz")
    for file in files:
        if folder_name != "":
            file_path = f"{dir_path}/{file}"
        else:
            file_path = file
        tar.add(file_path)
    tar.close()