The data for the setting of sentiment aspect-based opinion mining is collected by scrapping methods from the Airbnb system. The text reviews that are scrapped are actually open to view for the public or Airbnb users. The data collection consists of two databases of two countries: Netherlands and United Kingdom. The dataset of the Netherlands consists of 34.028 listings. \\ Will this change?

The format of data for each of these listings is shown in the figure below. What I can get from the JSON file is 
* The ID of the listing    **_id** or **review_vote:listing_id**
* The name and ID of the host    **reviewee:host_name** and **reviewee:id**
* The ID of the review    **review_id**
* Reviewer name and ID    **reviewer:host_name** and **reviewer:id**
* The text data    **comments**

![](https://github.com/AntigoniKourou/Thesis/blob/master/logos/review_data_example.png)
![width=3cm]( https://github.com/AntigoniKourou/Thesis/blob/master/logos/actual_review.png)
