#! /usr/bin/awk -f
# date
BEGIN{
  if(1) system("wget -O rawTrending 'https://twitter.com/i/trends'");
  #if(1) system("sed -i 's/\\\n /\\n/g' rawTrending");
  while(getline < "rawTrending" > 0){
    gsub(/\\n/, "ABCDEFG",$0)
    gsub("ABCDEFG", "\n", $0)
    #gsub("u003c", "", $0)
    print $0 > "trendingLineBreaks"
  }
  if(1) system("sed -i '/u003c/d' trendingLineBreaks");
  
  noTweetCount = 0;
  while(getline < "trendingLineBreaks" > 0){
    #print $0;
    if($0 ~ "data-trend-name"){
      if(noTweetCount == 1){
   	print "          999 Tweets" > "rawTrendinga"
	noTweetCount = 0;
      }
      noTweetCount = 1;
      print $0 > "rawTrendinga"
    }

    else if($0 ~ "Tweets"){
     # print $0;
      noTweetCount = 0;
      print $0  > "rawTrendinga"
    }
  }

  if(1) system("awk 'ORS=NR%2?FS:RS' rawTrendinga > 'finalTrending'");
  #Add the timestamp
  if(1) system("date '+%s' >> '../../public_html/cgi-bin/masterTrending'");

    while(getline < "finalTrending" > 0){
      #get rid of extra characters so the output is: topic_name 12.5k
      gsub(/data-trend-name=/, "", $0);
      gsub(/\\\"/, "", $0);
      gsub(/Tweets/, "", $0);
      gsub(/ /, "_", $0);
      gsub("_$", "", $0);
      gsub("_{11}", " ", $0);
      gsub("_{4}", "", $0);
      print $0 >> "../../public_html/cgi-bin/masterTrending"
    }
}
