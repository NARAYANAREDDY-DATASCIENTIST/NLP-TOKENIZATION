# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 14:38:40 2020

@author: NARAYANA REDDY DATA SCIENTIST
"""
# TOKENIZATION OF SENTENCES/PARAGRAPHS

import nltk
nltk.download()
nltk.download('punkt')

paragraph="""A movie to watch,I regret that I have never had the chance to watch it before
             but I'm also equally glad that I've watched this movie at the right time.
             The movie was quite relatable to my life just like everyone,not that I had been
             to jail,no.... but similar to that I was exiled within my fear.Recent times had
             been so hard that made me fed up and presented a feeling to stop trying.
             But this movie taught me that with persistence and hopefulness wonders can 
             be attained....
             The movie was a bit sedative in the beginning just as the life of any prisoner 
             but it didn't lower my want to watch.Later in the latter part there was some 
             depressing moments which'll make you think that hope can do no good but a sudden
             shift in the climax will a bring the emotions of urge when the prisoner tastes
             the freedom.Freedom for us is just a mere aspect but for those who never had it 
             so far and when they finally get it,they respect it and doesn't persuade it from
             others.
             I would like to thank to two of those Warner bros movies which made realize the
             ultimate truth of hope,which are Man of steel(hope never dies)and
             Shawshank Redemption(hope is a good thing,may be the best of things.....). 
             I had been wondering why they named this movie as Shawshank Redemption
             then I figured that the innocent has finally escaped himself not only from the
             jail and even from those evil thoughts or should I say overcome,truly 
             a redemption"""
             
              
#TOKENIZE INTO SENTENCES
             
sentences=nltk.sent_tokenize(paragraph)  

# TOKENIZE INTO WORDS
words=nltk.word_tokenize(paragraph)           