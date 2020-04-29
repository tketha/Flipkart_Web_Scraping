from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = "https://www.flipkart.com/search?q=iphone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_6_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_2_6_na_na_ps&as-pos=2&as-type=RECENT&suggestionId=iphone%7CMobiles&requestId=4ec5718d-76be-4247-beb7-ded45e0a51c5&as-searchtext=iphone"


uClient = uReq(my_url) #uReq which opens up the connection & this grab the webpage then it is loaded
page_html = uClient.read() #read() dump all the data which is gathered and stored in a variable page_html
uClient.close() #close the connection

page_soup = soup(page_html, 'html.parser')

containers = page_soup.findAll("div", {"class" : "_3O0U0u"}) #page_soup helped to parse my html
#print(len(containers))

#print(soup.prettify(containers[0])) #pretiffy() is a fn which is used to beautify/structured/organized html format

#Scrap name of 1st phone
container = containers[0]#loop to traverse these elements; here it contails 1st ele; containers is main div class where all ele present
#print(container.div.img["alt"]) # in container we have div inside div we have img which contain attribute "alt"

#Scrap price of 1st phone
price = container.findAll("div", {"class" : "col col-5-12 _2o7WAb"})
#print(price[0].text) #text is written bcz it doesn't have any tags

#Scrap ratings of 1st phone
ratings = container.findAll("div", {"class" : "hGSR34"})
#print(ratings[0].text)

filename = "products.csv"
f = open(filename,"w")

headers = "Product_Name,Pricing,Rating\n"
f.write(headers)

for container in containers:
    product_name = container.div.img['alt']

    price_container = container.findAll("div", {"class" : "col col-5-12 _2o7WAb"})
    price = price_container[0].text.strip()

    rating_container = container.findAll("div", {"class" : "hGSR34"})
    rating = rating_container[0].text

    # print("product name: " + product_name)
    # print("Price: " + price)
    # print("Ratings: " + rating)

    #string parsing
    trim_price = ''.join(price.split(','))
    #print(trim_price)
    rm_rupee = trim_price.split("₹")
    #print(rm_rupee)
    add_rs_price = "Rs." + rm_rupee[1]
    #print(add_rs_price)
    final_price = add_rs_price[0:]
    #print(final_price)

    print(product_name.replace(",", "|") + "," + final_price + "," + rating + "\n")
    f.write(product_name.replace(",", "|") + "," + final_price + "," + rating + "\n")

f.close()