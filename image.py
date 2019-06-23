"""
 In this I have used requests library to invoke the HTTP GET method essentially for retrieving data from 
the url.

I have used urllib.request basically to retrieve the image from the given url.

I have used Beautiful soup essentially for parsing a web page to find all the images on that page having
the tag 'img'.

Then user enters the keyword and then I have manipulated the keyword so as to form relevant url finally.

I made the url using the keyword and using beautiful soup parsing through the content of the web page
using 'img' tag I found the source of all the images and just took one image by giving the specified
relevant index.

After finding the url of the image which needs to be downloaded I have used a function to retrieve this 
image.
In the function I give url of image and name as arguments and create a full path indicating the name which will be 
given to the downloaded image and the format it will be saved in.
Finally using  urllib.request.urlretrieve I have retrieved the image using the url in the same directory
with specific name and format.
""" 



import requests
import urllib.request
from bs4 import BeautifulSoup

# Function to download the image

def image_downloading():
    
    user_keyword = input('Enter the keyword:')  # user enters the keyword

    # Manipulating the keyword to fit the url

    file1 = user_keyword.split(' ')

    sep = '-'

    file_name = sep.join(file1)


    url = "https://all-free-download.com/free-photos/" + file_name +".html" # url after adding the keyword
    r = requests.get(url)
    html_content = r.text

    soup = BeautifulSoup(html_content, "html.parser")  # to parse through the webpage

    url_1 = soup.find_all('img')[1]['src']  # finding source of all the images using 'img' tag

    
    # Function to download or retrieve image

    def retrieve_image(url_final, name):
        full_path = str(name)+'.jpg'  # giving full path name of image to be saved
        urllib.request.urlretrieve(url_final, full_path)  # image is retrieved and saved in the same directory
        

    
    image_name = input('Write the name of the image to be saved as:') # user enters the name of image to be saved as
    retrieve_image(url_1, image_name) # calling the retrieving function

image_downloading()  # calling the image downloading function  


