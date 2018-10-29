# Naive Bayes:

## Features and their weights:
| Features | Learned Weights|
| ----------- | ---------- | 
| Class Priors |  [ 0.41469828,  0.38525965,  0.20004207] |  

Theta =  [
            [  1.34263311,   2.75037769,   0.97571239,  19.31056766, 21.84443449,   8.55280738],
            [  1.65492704,   4.10690546,   2.67279624,  32.70667046, 14.32934332,  12.63740534],
            [  1.42011271,   3.22876426,   1.57733797,  23.98790809, 17.80195719,   9.9989353 ]
         ]

Sigma =  [
            [   1.83475972,    3.51395267,    2.26251264,  116.55232012, 207.37672246,   23.5682712 ],
            [   2.98482622,    8.51124486,    9.36077274,  438.24841698, 178.52283444,   63.66841889],
            [   2.08999781,    4.46458595,    3.52514001,  166.35604399, 178.19108311,   30.16031335]
         ]

## Results on Cheng data: 
<b>(scores mentioned are based on truth labels and not ROUGE)</b>

| Measure | Percentage|
| --------------- | ----------------- | 
| Precision | 38% |
| Recall | 85.6% |
| F1 score | 52.8% |

## Sample Output

### Sample Text Document: 

* -- think your @entity2 status updates are pretty dramatic ? if you act soon , you may entice a troupe of improv artists to stage them for the world
* " @entity11 , " happening live until 9 a.m. thursday , is taking the magical , mundane and sometimes mystifying world of @entity2 posts to the stage in a 24 - hour performance
* sponsored by online security company @entity13 , the experimental project lets @entity2 users volunteer their profiles
* if selected , a post from their page will be acted out during the event , which began wednesday morning at a @entity21 theater and is streaming live on @entity13 's facebook page
* so , for example , this post -- " just bought a tent
* " -- ends up featuring a @entity27 look - alike dancing as a gospel choir belts out those words , with feeling
* a dance troupe interprets a photo of chicken wings on a grill
* and an opera singer renders " is it just me , or does @entity21 smell like grape soda tonight ? " like @entity36
* " we believe it 's truly an experimental way to capture people 's attention in a relevant way , " said @entity40 , @entity13 's vice president of worldwide consumer marketing
* the name of the project is a play on the name of a @entity13 advertising campaign , " stuff
* " actors ( from improv to @entity54 ) , singers , musicians , poets , sculptors , puppeteers and balloon artists all have been among those taking the stage so far
* as of 3 p.m. et , 150 live skits had been performed at @entity21 's @entity62
* tapping into the city 's rich improv - comedy tradition , performers draw a post and have only a few moments to decide what they 'll do onstage
* " the performers are doing it on the fly , " @entity40 said
* they were hoping to work in 1,000 skits by thursday morning
* the folks watching and commenting on @entity75 's page seemed amused
* " this is strangely , strangely addicting , " one user wrote
* ridiculous , silly , and just awesome , " said another
* the page had more than 170,000 likes as of late wednesday afternoon .

### Predicted Summary: (Top 3 Sentences with the highest scores)

* if selected , a post from their page will be acted out during the event , which began wednesday morning at a @entity21 theater and is streaming live on @entity13 's facebook page
* " @entity11 , " happening live until 9 a.m. thursday , is taking the magical , mundane and sometimes mystifying world of @entity2 posts to the stage in a 24 - hour performance
* " actors ( from improv to @entity54 ) , singers , musicians , poets , sculptors , puppeteers and balloon artists all have been among those taking the stage so far

### Actual Summary: (Highlight of the article)

* -- think your @entity2 status updates are pretty dramatic ? if you act soon , you may entice a troupe of improv artists to stage them for the world
* " @entity11 , " happening live until 9 a.m. thursday , is taking the magical , mundane and sometimes mystifying world of @entity2 posts to the stage in a 24 - hour performance
* sponsored by online security company @entity13 , the experimental project lets @entity2 users volunteer their profiles
* if selected , a post from their page will be acted out during the event , which began wednesday morning at a @entity21 theater and is streaming live on @entity13 's facebook page
