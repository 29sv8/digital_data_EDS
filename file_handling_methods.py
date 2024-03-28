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
    return out, response
 
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
        version 3.10.9) to download a specific file from a FTP server.
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
        downloads the file to the current working directory (if only filename 
        specified) or the directory that was specified.
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