# TextRank:
Inspired by Pagerank algorithm used by Google Search to rank websites in  their search engine results. TextRank is a graph-based ranking algorithm for NLP. For keyphrase extraction, it builds a graph using some set of text units as vertices and then runs the algorithm on a graph. This method allows us to select sentences or phrases for 
the summary so as in incorporate diversity as well as a ranking system for how likely it is for the text unit to be a part of the summary. 

## Features and their weights:
This is a completely unsupervised approach compared to the supervised approaches that we use in the baselines.

## Results on Cheng data: 
<b>(scores mentioned are based on truth labels and not ROUGE)</b>

<!-- | Measure | Percentage|
| --------------- | ----------------- | 
| Precision | 38% |
| Recall | 85.6% |
| F1 score | 52.8% | -->

## Code Execution:
```bash
./run.sh <path/to/file>
```

## Sample Output

### Sample Text Document: 

* @entity1 's agent expects to go ' around the world ' discussing his client as interest in the @entity6 midfielder increases ahead of the summer transfer window
* @entity8 , who has confirmed that he held talks with @entity10 earlier this season , admits that he could receive 20 phone calls a day about the @entity13 international as clubs prepare to strengthen their squads before the start of next season
* city are keen to sign the @entity21 midfielder as they look to reshape their squad but @entity23 insists no decision has been made and that the 23 - year - old could even remain at the @entity26
* @entity6 midfielder has attracted interest from @entity10 , @entity29 and @entity30 @entity31 tussles with @entity33 's @entity32 during @entity6 's 1 - 1 draw at the @entity26 speaking to @entity35 , @entity23 said : ' for the moment , there are no formal discussions
* of course in the next few weeks i will be going around the world to talk about the situation with @entity1 but this is just informal information
* ' i will talk to everybody but @entity1 is very , very happy with @entity6 and the way they have treated him since he arrived from @entity46 last year
* ' there are still five games to play and hopefully they can make sure of a place in the @entity51 next season so it is a little bit too early to be making any decisions
* he has a four - year contract at @entity6 so we will have to see what they want to do
* ' i have met the people from @entity10 and we know each other
* i 've never spoken to anyone from @entity62 but a lot of other clubs have been in touch to find out some general information
* ' @entity68 champions @entity29 and @entity69 giants @entity30 are both interested in @entity31 , who is expected to cost around £ 40million after joining @entity6 from @entity46 for £ 18m in january last year
* @entity31 has scored 10 league goals and registered 17 assists so far this season , helping @entity74 's side to second place in the @entity68 table
* @entity77 celebrates with @entity31 after the @entity79 's equaliser against @entity33 on sunday @entity31 has been in superb form this season , scoring 10 goals and providing 17 assists in the @entity68

### Predicted Summary: (Top 3 Sentences with the highest scores)

* city are keen to sign the @entity21 midfielder as they look to reshape their squad but @entity23 insists no decision has been made and that the 23 - year - old could even remain at the @entity26 .
* @entity8 , who has confirmed that he held talks with @entity10 earlier this season , admits that he could receive 20 phone calls a day about the @entity13 international as clubs prepare to strengthen their squads before the start of next season .
* ' there are still five games to play and hopefully they can make sure of a place in the @entity51 next season so it is a little bit too early to be making any decisions .


### Actual Summary: (Highlight of the article)

* @entity8 will go ' around the world ' to talk about @entity1
* the @entity6 midfielder is wanted by @entity10 and @entity29
* @entity23 has admitted having talks with @entity10 chiefs this season
* but he has not spoken to @entity62 about a move for his client
* @entity31 remains happy at @entity6 and could yet remain at the club
