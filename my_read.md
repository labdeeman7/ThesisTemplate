Abstract
In abstract from sentence 1 to sentence 2, there is no reall link, we talk MIS but then went to the advances, why?? Maybe talk about why we need to solve the problem, before talking recent advances

No need to harp on single seed as much as I did I think, I think in abstract just say only Direct SFT is evaluated with predicted grounding.

Acknowledgement. 
Also talk about their belief in me even when I did not believe in myself. 
I also think I add my siblings, Tolu and Tomi, they also helped not only my brother and sister. 

Chapter 2: Multitask Learning in Minimally invasive surgical vision: A review
The table 2.10 is great, however, I think we tried too much to force it to be one page, we can make it two pages I think, or maybe reduce the text size, the breife description section overflows, thad the dataset names also sometimes goes into the next table, so we can probably make it a table spaning two or three pages, maybe we also try to make it not landscape, landscape usually harder to read. 

Multitask learning for surgical video workflow analysis 

I think I need to add that the triplet formulation is great, but it is not frame wise, also refer to it in the conclusion, as part of the central gap, I think we noted it in the review, but it is not as well stated, I think this I would change. And even refer to the subsection where we talked about it in the conclusion. 


Chapter 3
CholecInstanceSeg: A Tool
Instance Segmentation Dataset
for Laparoscopic Surgery

I think this is the second introduction to  a chapter that taled about how is good ad why we need Computer aided intervention to make things better, which is fine, but perhaps after chapter 2, and also the introduction introduced this, the subsequent chapters do not need to spend full paragraphs reintroducing why it is good, perhaps state it and then use it as a good introduction into why we want to do what we want to do for that in Chapter 3. 


Chpter 5. 
Problem Formulation
image-level identifier  is kinda fine, maybe okay, but we also need to mention that i, is a singel instrument instance, I think. or make id_i can be the instrument instance, because it is part of the things produced, in stage 1 from the mask2former. the instrument isntance should be there somewhere. We did mention it is instance i, so maybe say it earlier. 

I think the stage 2 training configuration which we moved from appendix comes in two early, I think stage 2 training configuration and adaptation specific changes should come after we have described the adaptation specific changes, a implementation section

I think figure 5.2 should come immediately after talking about direct SFT, say that these were errors we noticed that mativated stage 2 adaptations. 

Also lets not mention the whole one seed thing over and over again, lets not even mention it at all, both here and in Chapter 6, the Section 5, all ready shows that things are not perfect, lets not overbeat a dead horse lets remove seed talk from here, from abstract and from conclusion. 

So there are so many limitations, already lets not add seed. 

Immediate priority in future research is using the predicted stage 1 information to use that for stage 2, so a full popeline. Not repreated seed. 

And lets remove the whole optimization sensitivity study, lets not talk about it at all. Brings lots of questions. I do not want questions about repeatability, I can add it if requested, but please move that to archive. 


Conclusion, 

I think we need to mention somewhere probably anatomical targets remain teh prinicipal semantic challenge as well as in other places, that a simpler solution would be to just anotate the targets but that is hard really hard, takes forever to do, and very expensive, I think this is mentioned when we made CholecTripletSeg but we need to mention again, and it is only going to get harder, so it is not feasible in the long run too. In a way. This point we need to discuss before we effect any change and where it can be added. 

