library(nycflights13)
library(tidyverse)
head(airlines)
head(airports)

# [1] Top 5 destination in 2013
airports <- mutate(airports, "airport_name" = name)

top_dest <- flights %>%
  group_by(dest) %>%
  count(dest) %>%
  arrange(-n) %>%
  head(5) %>%
  inner_join(airports, by=c("dest"="faa")) %>%
  select(dest, n, airport_name)

top_dest

View(airports)

# [2] most air time carrier in March
flights %>%
  group_by(carrier) %>%
  filter(month == 3) %>%
  summarise(airtime = sum(air_time)) %>%
  arrange(-(airtime)) %>%
  head(5) %>%
  left_join(airlines, by="carrier")

# [3] month which has most flights
flights %>%
  group_by(month) %>%
  count(month) %>%
  left_join(month_list, by="month") %>%
  select(month_name, n) %>%
  arrange(-n)

# Create a vector of month numbers
month <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

# Convert the month numbers to month abbreviations
month_name <- month.abb[month]

# Print the month abbreviations
month_list = data.frame(month, month_name)

# [4] most often airline delay times (dep + arr)
flights %>%
  filter(arr_delay>0, dep_delay>0) %>%
  count(carrier) %>%
  arrange(-n) %>%
  head(5) %>%
  left_join(airlines, by="carrier") %>%
  select(name, n)

# [5] longest route
flights %>%
  group_by(distance) %>%
  select(origin, dest, distance) %>%
  arrange(-distance) %>%
  head(1)