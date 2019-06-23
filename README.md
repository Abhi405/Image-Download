# Image-Download

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
