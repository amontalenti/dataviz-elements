import pymongo
import datetime
import pandas as pd

def _get_data(collection, start_date, end_date, n):
    """Return domains, the total number of pageviews they refer, and max pageviews per day."""
    if n:
        records = collection.aggregate([{"$match": {"date": {"$gte": start_date, "$lte": end_date}}}, 
                                       {"$group": {"_id": "$referring_domain", "total_pvs": {"$sum": "$hourly_pvs.total"}, "max_daily_pvs": {"$max": "$hourly_pvs.total"}}}, 
                                  {"$sort": {"total_pvs": -1}}, {"$limit": n+1}])
    else:
        records = collection.aggregate([{"$match": {"date": {"$gte": start_date, "$lte": end_date}}}, 
                                      {"$group": {"_id": "$referring_domain", "total_pvs": {"$sum": "$hourly_pvs.total"}, "max_daily_pvs": {"$max": ("$hourly_pvs.total", "$date")}}}, 
                                      {"$sort": {"total_pvs": -1}}])
    assert isinstance(records["result"], list), "Call to mongo did not return list of documents"
    return (records["result"][0], records["result"][1:])

#def _make_records(start_date, end_date, prior_start, prior_end, collection, n=1000):
def _make_records(start_date, end_date, collection, n=1000):
    all_domains, others = _get_data(collection, start_date, end_date, n)
    #top_n = pd.DataFrame.from_records(others)
    # get sum of totals column
    print "all_domains", all_domains
    print others[0]
    # compute prior_start
    # compute prior_end
    """
    prev = pd.DataFrame.from_records(_get_data(collection, prior_start, prior_end, None)) 
    current_top_domains = top_n._id.tolist()
    prior_data = prev[prev._id.isin(current_top_domains)]
    sorted_current = top_n.sort("_id")
    sorted_prev = prior_data.sort("_id")
    all_data = {"domain": sorted_current._id, "total": sorted_current.total_pvs, "max": sorted_current.max_daily_pvs, "prior_total": sorted_prev.total_pvs, "prior_max": sorted_prev.max_daily_pvs} 
    return pd.DataFrame(all_data)[:n]
    """

def rank_by_totalpvs(start, num_days, ollection):
    end = start + datetime.timedelta(num_days)
    """
    data = make_records(start, end, prior_start, prior_end, collection)
    return data.sort("total", ascending=False)
    """
    data = _make_records(start, end, collection)
    return data

def rank_by_maxdailyviews(start, end, prior_start, prior_end, collection):
    data = _make_records(start, end, prior_start, prior_end, collection)
    #return data.sort("max", ascending=False)
    return data

def rank_by_fastestgrowth(start, end, prior_start, prior_end, collection):
    data = _make_records(start, end, prior_start, prior_end, collection, None)
    data["total_delta"] = data.total - data.prior_total
    #return data.sort("total_delta", ascending=False)
    return data

if __name__ == "__main__":
    conn = pymongo.MongoClient()
    db = conn.parsely_insights
    collection = db.refdomain_destinations
    start = datetime.datetime.strptime("2013-07-01", "%Y-%m-%d")
    num_days = 30
    rank_by_totalpvs(start, num_days, collection) 
    #print rank_by_fastestgrowth(data).head()
