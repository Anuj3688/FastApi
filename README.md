# FastApi

Just a play around code which uses fastapi to solve some of the 
day to day problems or use cases that I see. Here I have built an api setup for Tea Factory and tea. The data is
being stored in sqlite database since I was more focused on solving
the problem at hand.

I have created a file handling api which will take data in csv file
post that process it and store. Apart from that build a relation
between Factory and Tea in such a way that Factory cannot be added if
the tea details is not already present.

Used the router feature of fastapi to split similar api's in differed
groups so that it look crystal clear and people can easily understand which api
is related to which flow.
