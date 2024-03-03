# Project Inspiration

### **What was your inspiration for the project?**

The renewable energy track inspired this project, and we wanted to create an impactful product that solved an environmental problem. Currently, in the US, the percentage of power production from renewable energy sources is low, approximately 21.4%, while wind only makes up 10%. The main issue with wind turbines is the location, which requires consistent fast wind speed in flat terrain locations. This program precisely solves that; not only does it streamline efficiency and power calculations for our clients, but it also provides current MLS listings of land sorted by size (in acres). The client can alter this parameter based on the turbine we suggest is best for their location and how many they want.

# Project Description

### **What does your project do?**

ZephyroTech takes a client input of address, their property constraints, and a testing period to perform all calculations. It starts by taking the user input, which is reverse geocoded for longitude and latitude, using Google API and extracting location insights. Google API finds the county that the address is in, which is then crosschecked in Attom API to ensure accurate information. Once the county is confirmed to be accurate, it is inputted into live updating weather API, which extracts wind data for that county, such as wind speed and direction. Once this information is gathered, the program pulls turbine-specific data from a CSV of all active US wind projects containing turbine data, specifically turbine radius. This information calculates power and energy output for the specific area the client requested. Lastly, it tests over 300 models of turbines from various manufacturers before identifying the one with the highest energy output and officially recommending it.

# Project Development

### **How did you build your project?**

Our project has a backend built purely out of Python and a frontend made with HTML. We started by brainstorming ideas and following inspiration before finding data sources. This proved challenging for our creation process as we could not find a comprehensive data set with enough points to analyze. Soon, we found the US National Wind Turbine dataset, which gave us much more information. From here, we identified the parameters to extract and tried running data analysis with R before realizing we had to do it in Python. This was a significant setback; we wasted much time and now had to learn the Pandas library. After solving this, we pulled live API from WeatherAPI, Google, and Attom for wind data, geocoding, and MLS data to achieve other project goals. From here, we had to get help understanding how to create some front end; we had no experience with frontend coding whatsoever and had to ask an on-campus expert for guidance. As a result, our front end served primarily to submit data, not for aesthetic purposes, which greatly upset us. 

# Challenges Faced

### **What challenges did you run into?**

We encountered two significant challenges: frontend development (HTML/CSS/JS) and API documentation. We had minimal experience with HTML before going into this hackathon. Still, we had absolutely no experience in integrating a program into a website, and failure after failure led us to struggle to create a front end. We utilized our on-campus resources, including an expert on this field specifically, but due to time constraints, we were forced to utilize a basic form. Secondly, we ran into many issues with API documentation, as this was our first time working with an API of any sort. MLS data with Attom proved to be a monumental challenge to wrangle with, especially considering the specific syntax and JSON output needed and the often poor/inaccurate data due to the inaccessibility of publicly available data. Through several hours of experimentation and many Google searches, we grasped how to use API efficiently to create a live-updating program. 

# Accomplishments

### **What accomplishments are you proud of?**

We are proud of how the backend came together. This project started with just wind calculations, grew to reverse geocoding, and finally evolved into incorporating MLS real estate data. The incorporation of each and every part and having it all run functionally was a huge success. 

# Lessons Learned

### **What did you learn?**

This project helped us to learn three major things: API requests, the pandas library, and essential HTML & python integration. API requests especially took us a long time, as we had to learn the request process and individual documentation for three different sources, all of which were integral to the successful outcome of our project.

# Future Steps

### **What are the next steps for your project?**

This project has much room for growth and improvement, from expanding data sources to international locations to implementing machine learning to identify potential US sites for wind farms. We plan to grow this by extracting geographical attributes from existing wind farm locations and making them into a reference dataset. That can be used to train an algorithm to scan existing US land for sale and rank it on its ability to support wind energy infrastructure. Integrating artificial intelligence into such a mass scale would also like to create a more appealing front end that looks professional and supports international users. One of our primary goals for growth is to grow this in other countries, but most importantly, we want to grow it for application in offshore wind farms. Offshore farms have a much higher efficiency, and by harnessing that, we could exponentially increase the environmental benefits of wind energy. 