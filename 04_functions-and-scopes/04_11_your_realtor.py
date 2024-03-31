# Write a function that prints out nicely formatted information about a
# real estate advertisement. The information can vary for every advertisement, which
# is why your function should be able to take an arbitrary amount of
# keyword arguments, and display them all in a list form with some 
# introductory information.


#home_info = 'Address="1514 Brompton Ln",City="Crystal Lake",State="IL",Zip="60014",Bedrooms="2",Total_baths="2",Full_baths="1",Square_ft="1556",Acres=".2",Year_built="2007",Heating="Yes",Cooling="Yes",hoa="No"'



def listing(**home_info):
    listing_items = []
    print("Here are the details for your listing:")
    for k,v in home_info.items():
        print(f"{k}: {v:>20}")
        

        
listing(Address="1514 Brompton Ln",City="Crystal Lake",State="IL",Zip="60014",Bedrooms="2",Total_baths="2",Full_baths="1",Square_ft="1556",Acres=".2",Year_built="2007",Heating="Yes",Cooling="Yes",hoa="No")

