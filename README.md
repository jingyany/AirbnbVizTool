# Visualization and Analysis of Seattle Airbnb Hosts  ---- Project Functional Specification

## I. Background

Airbnb is an online community marketplace that connects people looking to rent their homes with people who are looking for accommodations. Airbnb users include hosts and travelers: hosts list and rent out their unused spaces, and travelers search for and book accommodations in 192 countries worldwide. 

This project aims to analyze the listing data of airbnb to adress some business problems related to Airbnb. When travelers plan to book a place on Airbnb, they will consider the location, room types, pricing, host introduction, reviews from other guests and availability of the place. We will use cutting edge techniques like machine learning models and data visualization to address guests' questions like what factors influence the listing price most? what will be the estimated price per night and availability during holidays like christmas or thanksgiving? will weather be a factor to influence the listing price? Which area has higher listing price? Instead of looking for those information by clicking on each listing, users can look at our data visualization and find all informations they need before booking a place to stay.


## II. Users

### Target User:  

our target users are the guests of Airbnb who interested in 

1. understanding how  the price per night comes up with different factors 

2. comparing prices within different areas on the map 

3. interacting with our visualization tool to explore more information they want

### Computer experience require:  

1.The users should know how to select or click a button on Computer 

2.The users should know  Zoom, Hover and Select Tool on map view

3.The users should better has experiences of using any visualization tool before 

4.The users should have Python experience if they wanted to uderstanding our coding part 

### Domain knowledge : 

1.The users should have some knowledge on Linear Regression if they were interesting on understanding which facotrs influence price most 

2. The users should have expereince with Machin learning Model and Python if they were interesting on understanding how we select features and how we fit the models 


### Users' Benefit: 

The users could see which factors influence the price most , and predicting the price per night base on their own preference. For example, The users could compare the price between holiday and non-holiday and then make decision by their budget. Also, The Users could have idea which areas have higher price and which areas have lower idea and this could also help them make decision by their budget. 


## III. Use Cases

### Overview:

[![Screen Shot 2017-05-11 at 9.42.11 AM.png](https://s14.postimg.org/r4pe6ifht/Screen_Shot_2017-05-11_at_9.42.11_AM.png)](https://postimg.org/image/za7g4o3ql/)

### 1. Map Area

**(1) Pan Tool**

Activating the pan tool allows the users to pan the map by left-dragging a mouse or dragging a finger across the map region.


**(2) Reset Tool**

Clicking the reset tool button allows users to restore the map to the original view.

**(3) Wheel Zoom Tool**

Activating the wheel zoom tool allows users to zoom the map in and out, centered on the current mouse location.

**(4) Hover Tool**

Activating the hover tool pops up a tooltip showing host's basic information when the cursor is over a point. The information of the tooltip includes host name, host address, property type, room type, accommodates, number of bedrooms, number of bathrooms and daily rent price. An example of using hover tool is as below:

[![QQ图片20170511151622.png](https://s28.postimg.org/woi5zxazx/QQ_20170511151622.png)](https://postimg.org/image/kze6byk15/)

**(5) Tap Selection Tool**

The tap selection tool allows users to select at a single point on the map by clicking a left mouse button, or tapping with a finger and then present host detailed information on the right side of the map.


### 2. Selection Area

**(1) Room Type Check Box**

Room Type check box allows users to select hosts with specific property type to present on the map. The default selection is all three property type. If a user only wants to see hosts providing private room, he just needs to only tick private room option. An example is shown below. Map only shows hosts that provide private room, representing by red points on the map.

[![QQ图片20170511151900.png](https://s7.postimg.org/cv0wsj07v/QQ_20170511151900.png)](https://postimg.org/image/vncrw3wlz/)

**(2) Neighborhood Dropdown Menu**

Neighborhood Dropdown Menu allows users to select hosts in specific neighborhood to present on map. For example, if users only want to see hosts in Queen Ann, he would click the dropdown menu and choose Queen Ann.


### 3. Selected Host Detailed Information

Clicking a single point on map will show the selected host’s detailed information in this area. Presenting information includes:

(1) Host Basic Information: host name, address, amenities etc.

(2) House Picture: presents users with room pictures, house pictures etc. Arrows on the picture allow users to see last / next picture.

(3) Calendar: shows host’s rent calendar.

(4) Rent Price Histogram and Customer Rating Histogram: shows distribution of each host’s rent price and customer rating filtered with conditions users made in Selection Area, colors out the selected host in the histogram. It allows users to compare the selected host with other hosts that have the same room type in the same neighborhood. 

### 4. Selected Neighbourhood with Room Type Filter Statistic Analysis

Rent Price Histogram and Customer Rating Histogram shows distribution of each neighbourhood’s average rent price and average customer rating filtered with room type condition users made in Selection Area, colors out the selected neighbourhood in the histogram. It allows users to compare the selected neighbourhood with other neighbourhoods in Seattle that have the same room type.


### 5. Rent Price Estimate

**(1) Feature Inputs**

The most relevant features to pricing predictions will be listed in this field, which allows users to select the features they desired and input the range of a specific featur.


**(2) Estimate Start Button**

Clicking the button will put all inputs in Feature Inputs area into a machine learning model, and run out an estimate rent price for users to consider about.




## References:
Folger, Jean. "The Pros and Cons of Using Airbnb." Investopedia. N.p., 06 Mar. 2017. Web. 11 May 2017.
