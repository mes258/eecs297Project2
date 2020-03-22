#! /usr/bin/awk -f

BEGIN {
  do {
    system("./twitterTrends.cgi");
    exit_code = system("sleep 1800 && exit 27")
    print "exit_code: " exit_code
  } while (exit_code != 0.0078125 && exit_code != 0)
}