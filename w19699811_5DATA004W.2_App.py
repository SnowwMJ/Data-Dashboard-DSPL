import streamlit as st # to connect to streamlit and do streamlit functions like write and display
import pandas as pd # to ingest and manipulate my datasets 
import matplotlib.pyplot as plt # for visulisations

st.sidebar.title("Navigation Bar") # due to my dashbaord being multi paged, im making it so the functionality fully revolves around the naivgation bar with if statements as st.navigation requires many 
page = st.sidebar.radio("Look at:", ["The Crime Age Threshold", "Crime Map Of Englad & Wales", "Drug Related Crimes", "Weapon Based Homicides"]) # this displays the different sidebar options for each page to be combined with an of statement


if page == "The Crime Age Threshold": # the very fist page, if it is selected from the sidebar, the code runs displaying everything for the current page 
    st.title("Analytics on Crime in England & Wales") # main title to capture my main aim and direction of talk
    st.header("Dashboard Overview") # small header to give an overall breakdown of what my dashbaord is about 
    st.write("Crime in England & Wales is a topic with alot of different factors. In my dashboard I will cover variables such as; knife crime, gun crime, crime involving substance abuse & crime involing age groups")

    df_aged_16_over = pd.read_csv("Crime_Aged 16+.csv") # ingesting the first dataset which is my main talking point and comparison (count)
    df_aged_16_over_percentage = pd.read_csv("16plus percentage.csv") # percentage for the dataset
    df_aged_16_under = pd.read_csv("Crime Aged under 16.csv") # percentage for under dataset

    year_cols = [col for col in df_aged_16_over.columns if "_count" in col] # making a variable that holds all the year features because i cant manually remove count in excel without errors
    totals_per_year = df_aged_16_over[year_cols].sum() # collecting the sum of the years columns each in the main data
    totals_per_year.index = totals_per_year.index.str.replace("_count", "").str.strip() # now removing count so the function has already applied before its removed treated as a string (when i removed it in excel it gave me negatives for the colums)

    col1, col2 = st.columns(2) # this lets me put 2 charts next to eachother which is important because of 8 flatfiles 

    with col1: # coding the first 
       st.subheader("Total Victims Yearly Aged 16+") # first chart being made with matplot

       fig, ax = plt.subplots(figsize=(15, 8)) # displaying the dimensions of the chart
       totals_per_year.plot(kind='line', marker='o', ax=ax) # setting as line chart
       ax.set_title("Total Homicides per Year", fontsize = 20) # title and font size set
       ax.set_xlabel("Year", fontsize = 18) # labeling and font size set
       ax.set_ylabel("Victim Count", fontsize = 18) # labeling and font size set
       ax.grid(True) # giving it a grid so its easier it read and see key intersections with the x and y axis 
       
       plt.xticks(rotation=45, fontsize = 14) # rotating the x axis so that the labels are easier to read and don tlook clustered
       plt.yticks(fontsize=14) # making the size more readable as its tiny otherwise 
    
       ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x):,}')) # formatting the axis so the values are neat, not too big and have commas so easier to distingusih: 4000 -> 4,000
    
       st.pyplot(fig, use_container_width=True) # displaying the chart with it being set expand so its not smaller

    with col2:
       st.subheader("Total Victims Yearly Aged Below 16")
       df_aged_16_under.columns = df_aged_16_under.columns.str.strip() # removing empty gaps and spaces with strip

       year_cols_under = [col for col in df_aged_16_under.columns if "_count" in col] # same method as above but for the second dataset now since they were in the same sheet
       totals_under = df_aged_16_under[year_cols_under].sum() # creating the sum again of the years ie each column
       totals_under.index = totals_under.index.str.replace("_count", "").str.strip() # removing count here explained above 

       fig, ax = plt.subplots(figsize=(15, 8))  # setting the size of the chart
       totals_under.plot(kind='line', marker='o', ax=ax)  # creating it as a line chart
       ax.set_title("Total Homicides per Year", fontsize=20) # setting title
       ax.set_xlabel("Year", fontsize=18) 
       ax.set_ylabel("Victim Count", fontsize=18)
       ax.grid(True)

       plt.xticks(rotation=45, fontsize=14)  # rotatting so its easier to read
       plt.yticks(fontsize=14) # making sure font isnt too small

       ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x):,}')) # formatting 

       st.pyplot(fig, use_container_width=True) # plotting at proper size 
    

    st.write("The charts above show victims of homocides between two age brackets of 16+ and under 16. This is telling us clearly that while adult crime has higher fluctuations and an overall higher count of crimes, the crime victims who are younger than 16 has much larger spikes and amount on avergae to higher than 500 cases per year which is a devastating amount considering they are below 16.")
    
    col3, col4 = st.columns(2) # using the column function again to have two displays etc next to each other 

    with col3:
       if st.button("Average Percetnage Victims 16+"): # creating a button to display the average percentage. the average percentage was calcuated in excel since I had alot of errors having it run here
          st.subheader("Average Percentage") # title for display
          st.subheader("23.4%") # displaying the results from excel here 

    with col4:
       if st.button("Average Percetnage Victims Under 16"): # repeating the above here for the second percentage
         st.subheader("Average Percentage")
         st.subheader("31.04%") # used subheader for the display as .write was makign it too small and the fontsize was not helping the problem

    st.write("Showing the percentages reveals an interesting statistic that victims under the age of 16 tend to on average have a higher risk of being a victim to homocides than someone aged 16+ by nearly 10%." \
    " This reveals a darker truth towards the crime of england and wales that younger people are more involved in violent crimes.") # explaining the information presented

    if st.button("Solutions For Age Based Crime"): # these buttons will be on every page to display solutions so the pages keep a simplar design at face value, therefore a if statement is used 
        st.write("Possible solutions regarding knife crime include:\n" \
      "-  Increased awareness in educational institutes\n" \
      "-  Increased awareness for parents\n" \
      "-  Social media monitoring\n" \
      "-  Police trust building with the youth" \
      "-  Hotspot identification as lower income areas tend to have overall more crime")
        # adiotnal information and clairification on the solutions 
        st.write("There are many solutions revolving around tackling crmie based on age and no single solution alone itself will fix all the problems. These need to be all implemented together in greater numbers across England & Wales to bring national awareness to this growing problem. Parents especially should be constantly aware of who" \
        "their children are in contact with and should be more willing to help with guidance. Monitoring social media would also help identify what groups online are activally trying to manipulate younger people into getting involved with criminal activity.")
        
     
elif page == "Crime Map Of Englad & Wales": # second page which is all to do with map display

   df_map = pd.read_csv("Lat and Lon locations.csv") # loading the map dataset which is complete with the lat and lon so it works in the map function

   st.title("Maps Of Homocides in England & Wales") # title

   df_map = df_map.dropna(subset=["Latitude", "Longitude"]) # making sure theres no NAN values as when running without ,i get erros for NAN values being present
   df_map = df_map.rename(columns={"Latitude": "lat", "Longitude": "lon"}) # renaming the columns to lat and lon now they dont have NAN values 

   st.subheader("Crime Locations") # labelling
   st.map(df_map[['lat', 'lon']]) # creating the map now using my map and its lat and lon columns 

   st.write("This map displays the locations (cities and more specific area) where homocidies have happened the most in England and Wales & the police stations registering these crimes. Highlighted areas include London, Manchester, Birmingham," \
   " and other densely populated regions, indicating a higher frequency of violent crimes in these areas. This  suggests a correlation between population density & homicide rates, where larger cities may experience more frequent incidents due to socioeconomic disparities & gang crime being more common in those cities")

   if st.button("Possible Solutions"): # this will be a button to display solutions for the user 
      st.write("Solutions here would be gathering more data on common hotspots for gang violence, drug dealing and seeing if they corelate with homicde locations from key cities highlighted here and other maps. From this data then, more surveillance could be implemented as well other measures such as more stop & searches")



elif page == "Drug Related Crimes": # page name 
   df_drug_related = pd.read_csv("Drug Related Crime.csv") # ingesting data
   
   x = df_drug_related['Year'] # setting x axis values i want from the data
   y = df_drug_related['Drug Homicide Count'] # same here for y axis

   st.title("Homicides Related To Drugs") # title of page
   st.subheader("This Chart Displays Any Homicides Relating To Drugs Yearly") # exposition on the chart

   fig, ax = plt.subplots(figsize=(12, 8)) # making it bigger as its a solo chart and not being columned with another 
   plt.bar(x, y, color='red') # sticking with the red and black asthetic 
   ax.set_facecolor('black') # this makes the plot itself (background) black
   fig.patch.set_facecolor('black') # this is what makes the entire background black
   ax.set_xlabel("Year", color='white', fontsize = 13)
   ax.set_ylabel("Count of Drug Related Homicides", color='white', fontsize = 13)
   ax.set_title("Yearly Count of Homicides Related To Drugs", color='white', fontsize = 13) # seeting titles colours

   ax.tick_params(axis='x', colors='white', rotation=45) # rotation and setting everything as white to be readable in the black background
   ax.tick_params(axis='y', colors='white')
   
   st.pyplot(plt.gcf()) # displaying the plot, gcf sows the current plot 

   st.write("Eyeballing this display tells us that since 2013, the count of yearly homicides involving drugs, has exponentially increased from around 230 drug relatecd homicides in 2013 to around 315 10 years later." \
   " These crimes started to spike from 2016 onwards & reached an all time high of 350 in 2022. The numbers did slightly decrease fom 2020 - 2021 most likely due to covid-19 indicating this problem is very prevelant and needs to be addressed as without the national lockdowns, the count would be higher.")

   st.dataframe(df_drug_related) # displaying the data as a dataframe since it only has 3 columns and is easier to udnerstand 
   st.write("The upwards trend is reflected also in the proportion of homicides that involved drug users or dealers. Both these displays could indicate a strengthening link between drug-related activity &  lethal violence, possibly due to growing issues such as county lines drug trafficking, drug gangs, or shifts in drug market dynamics in the UK." \
   " Gangs involved in drugs especially has been a prevelant issue & one which has been started to be tackled more day by day by the police.")

   if st.button("Possible Solutions"): # soluions button and using \n to list them
      st.write("Possible solutions regarding drug related homicides include:\n" \
      "-  Invest in drug rehabilitation\n" \
      "-  Police focusing on distributors\n" \
      "-  Understand Socioeconomic Causes")
      st.write("These soltuions tackle the main suggested causes of drug related homicides as drug addicition isnt a talked about enough problem & helping people open up can aid mentally the people struggling. Furthermore, a lot of police raids target drug users (Which isn't wrong) however there needs to be a bigger focus on suppliers and" \
      " distributers to stop the spread and helping control drug gangs. Investment in treatment, education, & social support combined with smarter enforcement strategies offers a sustainable path forward.")


elif page == "Weapon Based Homicides":  # final page which has been changed now to include both knife crime and fire arm crime.

   # df_knife_crime = pd.read_csv("c:/Users/HP/Dataset 8 files/Knife crime 2014 - 2024.csv")  ingesting final data files 
   df_knife_crime = pd.read_csv("Knife crime 2014 - 2024.csv")
   df_type_knife = pd.read_csv("Knife crime with type of knife reported.csv")
   df_firearm_crime = pd.read_csv("Crime involving Firearm.csv")

   st.title("Weapon Based Crimes") # page titleset
   st.write("Weapon based crimes have been a prominant problem since the 2010s with it increasing year by year. These tabs wil display the amount of knife crimes reported yearly, type of knife used, and firearm crime")

   tab1, tab2, tab3 = st.tabs(["Knife Crime Over Years", "Knife Type Usage", "Firearm Involvement"]) # this will give my page 3 tabs to pick from to explore all types of weapon crime wihout having extra pages 

   with tab1: # first tab will be a line chart to display knife related crimes over the years 
      df_knife_crime.columns = df_knife_crime.columns.str.strip() # removing all possible extra spaces
      year_cols = [col for col in df_knife_crime.columns if "Apr" in col] # creating a pure years column var

      totals_knife = df_knife_crime[year_cols].sum() # summing the count 

      st.subheader("Knife-Crime Over The Past Decade")

      fig1, ax1 = plt.subplots(figsize=(10, 5)) # setting figure
      totals_knife.plot(kind='line', marker='o', color = "red", ax=ax1) # setting line chart
      ax1.set_facecolor('black') # this makes the plot itself (background) black
      fig1.patch.set_facecolor('black')
      ax1.set_title("Knife-Related Homicides (2014-2024)", color='white', fontsize = 13)
      ax1.set_ylabel("Count", color='white', fontsize = 13)
      ax1.set_xlabel("Year", color='white', fontsize = 13)
      plt.xticks(rotation=45, color='white')
      plt.yticks(color = "white")
      ax1.grid(True) # grid being added because pure black makes the line chart hard to interpret 
      st.pyplot(fig1) # displaying fig

      st.write("Knife crime since the early 2010s, has increased slowly year by year before spiking in 2017-2018. This is followed by gradual decline before starting to rise again in 2024. This trend highlights the fluctuating yet persistent nature of knife-related violence even despite the short term decreases. The 2018 spike would be attributed to the increase & glorification of gang violence through social media " \
      "which is still a prevlant issue to this day. Law enforcement has, in the last few years, been starting to monitor online traffic regarding criminal activity and this corelates with the dips after the peak.")
     
      if st.button("General Knife Crime Solutions"): # solutions button
          st.write("Possible solutions regarding knife crime include:\n" \
      "-  Increased awareness in educational institutes\n" \
      "-  Increased awareness for parents\n" \
      "-  Social media monitoring\n" \
      "-  Understand root causes")
          
          st.write("These solutions tie in with making sure young people are aware of knife crime as previously we saw how theres a substancial number of young people involved with these crimes.")
       

   with tab2: # second tab will revolve around the types of knives used
     df_type_knife.columns = df_type_knife.columns.str.strip() # removing extra emoty sppaces

     st.subheader("Type of Sharp Instrument Used")

     fig2, ax2 = plt.subplots(figsize=(10, 10)) # 10 10 is the most clear i can get others are too small and numbers and labels unreadable
     ax2.set_title("Knife Types Used in Homicides (2022-2024)")# title
     ax2.pie(df_type_knife["Total"],  #setting the total to be the count
       autopct="%1.1f%%") # setting percentages 
     
     ax2.legend( # creating legend as the categrocial row names are too big 
       labels=df_type_knife["Type of sharp instrument"], # setting what the legend will take the cat values form
       title="Knife Type",
       loc="center left",
       bbox_to_anchor=(1, 0, 0.5, 1)) # coords for the legends placement 

     st.pyplot(fig2) # displaying
        
     st.write("This pie chart displays the type of knife or sharp instrument used in violent homicides over the past 2 years. The eye catching statistic is the percentage of kitchen knives used in violent homicides being responsible for nearly half of these crimes. Additionally, alot of knives which arent legal such as zombie knives, rambo knives etc.. are being used" \
     " even though they are illegal to posses in England & Wales.")

     if st.button("Knife Control Solutions"): # button for the solutiosn 
          st.write("Possible solutions regarding knife crime type being used:\n" \
        "-  Investigating how illegal knives such as zombie knives are being smuggled into the country\n" \
        "-  Parents awareness for knives from home being used most commonly\n" \
        "-  Social media monitoring as some weapons are flaunted online\n" \
        "-  More stop and searches in known violent areas")
          
          st.write("Law enforcement understanding from where & how these knives are being smuggled into England & Wales would be crucial in stopping alot of these attacks but furthermore, parental surveillance and more stop and searches would also be a starting point for change as nearly 50% of knife based homicides are being comitted using kitchen knives. Restrictions on purchases ( such as needing to be an older age etc..) would also greatly help this crisis")
        

   with tab3: # final tab all on firearm to complete the weapons page 
      df_firearm_crime.columns = df_firearm_crime.columns.str.strip() # removing null spaces

      st.subheader("Homicides Involing a Firearm")

      fig3, ax3 = plt.subplots(figsize=(10, 5)) # setting size
      df_firearm_crime.set_index("Year")[["Licensed firearm", "Unlicensed firearm", "Unknown if licensed firearm"]].plot(kind="bar", stacked=True, ax=ax3) # setting the values i want for the stacked chart
      ax3.set_title("Firearm Involvement in Homicides by Year") # title
      ax3.set_ylabel("Homicide Count") # label y
      ax3.set_xlabel("Year") # label x
      plt.xticks(rotation=45) # rottion so it is easier to read
      st.pyplot(fig3) # displaying the figure 

      st.write("Clear straight away from this display is that unlicensed firearms are the main used firearms in homicides of course due to tracing them back to a culprit being very hard.")

      if st.button("Firearm Solutions"): # button for solutions 
           st.write("Possible solutions regarding firearm crime include:\n" \
      "-  Crackdowns on smugglers and suppliers of firearms\n" \
      "-  Responding with more urgency to these crimes and not delaying investigations\n" \
      "-  Increased surveillance")
           # final writing statement for the solution 
           st.write("A lot of these solutions would intertwine with illegal knife importation and law enforcement having to crackdown heavily on the imports and identifying the smugglers before this issue grows as currently it is on a steady decline but if neglected further, can possibly start to increase again.")
          
         
         



   


   
    
    
