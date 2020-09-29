# Natural_Language_Processing

Code Link - https://github.com/anubhavkmr8/Natural_Language_Processing/blob/master/English2Hindi.py

Programming Language - Python

Used Rule Based Approach to design the English to Hindi Translation.

Following Steps were followed - 
Step 1 - Traverse the input english_string character by character. 
Step 2 - If the current character is vowel :-
If the last character is “a” then this sounds "ा". For eg. aaina => अइना
If the character is “a” and it is not the first character then this does not contribute anything. ( Raman => रमन)
If this character is preceded by another vowel or it is the first character of the string then it is mapped with the corresponding eng2hin_vowels dictionary character.
Else it is mapped with the  corresponding eng2hin_vowels_half dictionary character.
Step 3 - If the current character is not vowel it is mapped with corresponding character either present either in eng2hin_sonorants or eng2hin_consonents dictionary. Here we also check if this character is not followed by any vowel then this character is treated as half. (Bachcha => बच्चा).



For SMT we needed the Linux environment exclusively as windows subsystem for linux doesn’t support hindi language instead of showing hindi words it just shows blank boxes.

I installed the moses and splitted the parallel corpus into separate en-hi.mined.hi and en-hi.mined.en. https://github.com/anubhavkmr8/Natural_Language_Processing/blob/master/nlp_assignment.rar

Did the Tokenisation, truecasing and cleaning.
Trained the language model and translation system.
For testing we didn’t have a separate dataset so didn’t tune.
And then testing was done but as already mentioned about the wsl problem could not verify the result.

Commands for all these steps are - https://github.com/anubhavkmr8/Natural_Language_Processing/blob/master/smt.txt


