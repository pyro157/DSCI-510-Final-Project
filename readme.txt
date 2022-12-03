the first part of data is stored in the form of csv files under Data folder.
get_accident_data(year: str)
This function takes an string argument '2018', '2019', '2020' because only these three years of data are saved in the Data folder.
it will return a dataframe from accident.csv of that year.

get_realtime_accident_data(response_limit: str)
This function makes an API request to the server, getting responses from the server and return responses in json format.
the argument takes only integers and will return that amount of most recent data.

count_accident_by_state(year: str)
This function will take the year and return a dictionary of number of accidents in each state.

link to github repository
https://github.com/pyro157/DSCI-510-Final-Project.git