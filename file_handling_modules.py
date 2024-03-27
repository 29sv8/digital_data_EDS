# Description: 
#   A module containing functions for the retrieval of files from external sources.
# Author:
#   Sanne Vreugdenhil
# Date of creation:
#   27-03-2024

def download_from_url(url, filename):
    """
    Description
        ----
        This function uses the urllib.request module to download a file from a given URL link.
        The file is downloaded into the current directory if you provide a just a filename. 
        A filepath (absolute or relative) can also be provided instead.
        ----
    Parameters
        ----
        url
            >> the url link from which to download the file
        filename
            >> the name the file is to be called in the current working directory
            >> a filepath (absolute or relative) can be provided instead of a filename
        ----
    Returns
        ----
        urllib.request.urlretrieve returns a tuple of the filename and some information
        out
            >> the filename
        response
            >> the information
        Prints the message that the file was downloaded succesfully and the information.
        ----
    """
    import urllib.request
    out, response = urllib.request.urlretrieve(url, filename)
    print(f"Successfully downloaded {out}\n")
    print(response)
    return out, response
 
 