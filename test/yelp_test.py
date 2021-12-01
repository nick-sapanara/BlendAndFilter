from yelpapi import YelpAPI
yelp_api = YelpAPI("jgAIlOyDcteIC-QzduVUg5N-PgCgKcM5_Oi2F_gp0KYCE5xSwxGftWhWdby7QTMsJ0ihq9EVXqxP7zS7nwp5wV2xZ6Eyt2iRtr0ustfVipE8ZEdL4RCpZYQMmj6mYXYx", timeout_s=3.0)
search_results = yelp_api.search_query(term='coffee', location='brooklyn, ny', sort_by='rating', limit=5)
for i in range(5):
    print(search_results['businesses'][i]['name'])