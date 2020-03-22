#! /usr/bin/awk -f
BEGIN{
  if(1) system("wget -O rawTrending 'https://twitter.com/i/trends'");
  #if(1) system("sed -i 's/\\\n /\\n/g' rawTrending");
  while(getline < "rawTrending" > 0){
    gsub(/\\n/, "ABCDEFG",$0)
    gsub("ABCDEFG", "\n", $0)
    print $0 > "trendingLineBreaks"
  }
  while(getline < "trendingLineBreaks" > 0){
    if($0 ~ "data-trend-name"){
      print $0 > "rawTrendinga"
    }
    if($0 ~ "Tweets"){
      print $0 > "rawTrendinga"
    }
  }

  if(1) system("awk 'ORS=NR%2?FS:RS' rawTrendinga > 'finalTrending'");
    while(getline < "finalTrending" > 0){
      #need to do the opposite of this: 
      gsub(/data-trend-name=/, "", $0);
      gsub(/\\\"/, "", $0);
      print $0 > "cleanTrending"
      #print substr($0, 23) > "cleanTrending"
      #system("cut -c -22 'finalTrending' > 'cleanTrending'");
    }
}
